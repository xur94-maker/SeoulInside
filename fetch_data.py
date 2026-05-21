import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

def strip_namespaces(raw_bytes):
    raw_bytes = raw_bytes.replace(b'content:encoded', b'content_encoded')
    raw_bytes = re.sub(rb'\s+xmlns(?::[a-zA-Z0-9_]+)?="[^"]*"', b'', raw_bytes)
    raw_bytes = re.sub(rb"\s+xmlns(?::[a-zA-Z0-9_]+)?='[^']*'", b'', raw_bytes)
    return raw_bytes

def fetch_rss(url, max_items=8):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read()
        raw = strip_namespaces(raw)
        root = ET.fromstring(raw)
        items = []
        for item in root.iter('item'):
            title = (item.findtext('title') or '').strip()
            link = (item.findtext('link') or '').strip()
            date = (item.findtext('pubDate') or '').strip()
            desc = (item.findtext('content_encoded') or item.findtext('description') or '').strip()
            desc = re.sub(r'<[^>]+>', '', desc).strip()[:200]
            if title and link:
                items.append({'title': title, 'link': link, 'date': date, 'desc': desc})
            if len(items) >= max_items:
                break
        return items
    except Exception as e:
        print(f'RSS error: {e}')
        return []

def fetch_substack_posts(substack_url='https://seoulinside.substack.com', max_items=10, full_archive=False):
    try:
        feed_url = f'{substack_url}/feed'
        req = urllib.request.Request(feed_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read()
        raw = strip_namespaces(raw)
        root = ET.fromstring(raw)
        items = []
        latest = None
        # max_items를 크게 늘려서 아카이브용 전체 글 수집 (예: 30개)
        limit = 60 if full_archive else max_items
        for i, item in enumerate(root.iter('item')):
            title = (item.findtext('title') or '').strip()
            link = (item.findtext('link') or '').strip()
            date = (item.findtext('pubDate') or '').strip()
            body = (item.findtext('content_encoded') or item.findtext('description') or '').strip()
            if title and link:
                post = {'title': title, 'link': link, 'date': date, 'body': body}
                items.append(post)
                if i == 0:
                    latest = post
            if len(items) >= limit:
                break
        return items, latest
    except Exception as e:
        print(f'Substack error: {e}')
        return [], None

def fetch_medium_rss(medium_user, max_items=8):
    rss_url = f'https://medium.com/feed/@{medium_user}'
    items = fetch_rss(rss_url, max_items=max_items)
    for item in items:
        if 'date' in item and item['date']:
            try:
                dt = datetime.strptime(item['date'], '%a, %d %b %Y %H:%M:%S %Z')
                item['date'] = dt.isoformat()
            except:
                pass
    return items

def fetch_stock(symbol, label, currency='USD'):
    try:
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=2d'
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        
        result = d['chart']['result'][0]
        meta = result['meta']
        price = meta.get('regularMarketPrice', 0)
        prev = meta.get('previousClose', price)
        
        change = price - prev
        pct = (change / prev * 100) if prev else 0
        
        cap_t = None
        try:
            url2 = f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=price'
            req2 = urllib.request.Request(url2, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req2, timeout=15) as r2:
                d2 = json.loads(r2.read())
            cap_raw = d2['quoteSummary']['result'][0]['price'].get('marketCap', {}).get('raw', None)
            if cap_raw:
                cap_t = round(cap_raw / 1_000_000_000_000, 2)
        except:
            pass
        
        return {
            'symbol': symbol,
            'label': label,
            'currency': currency,
            'price': round(price, 2),
            'change': round(change, 2),
            'pct': round(pct, 2),
            'capT': cap_t
        }
    except Exception as e:
        print(f'Stock error ({symbol}): {e}')
        return {'symbol': symbol, 'label': label, 'currency': currency, 'price': 0, 'change': 0, 'pct': 0, 'capT': None}

print('=== SeoulInside Data Collection Start ===')
data = {}

# 1. Substack: 일반용 10개 + 아카이브용 전체 (최대 60개)
print('[1/5] Fetching Substack posts...')
substack_posts_limited, latest_post = fetch_substack_posts('https://seoulinside.substack.com', max_items=10, full_archive=False)
substack_posts_full, _ = fetch_substack_posts('https://seoulinside.substack.com', max_items=60, full_archive=True)

data['myPosts'] = substack_posts_limited
data['substackArchive'] = substack_posts_full   # ← 아카이브용 전체 목록 추가!
if latest_post:
    data['latestPost'] = latest_post
print(f'  Substack (main): {len(data["myPosts"])} items')
print(f'  Substack (archive full): {len(data["substackArchive"])} items')

# 2. Medium
print('[2/5] Fetching Medium posts...')
medium_posts = fetch_medium_rss('Seoulinside', max_items=8)
data['mediumPosts'] = medium_posts
print(f'  Medium: {len(data["mediumPosts"])} items')

# 3. 글로벌 뉴스
print('[3/5] Fetching global news...')
global_news = fetch_rss('https://feeds.bbci.co.uk/news/world/rss.xml', max_items=5)
global_news += fetch_rss('https://rss.nytimes.com/services/xml/rss/nyt/World.xml', max_items=4)
data['globalNews'] = global_news[:8]
print(f'  Global: {len(data["globalNews"])} items')

# 4. 한국 뉴스
print('[4/5] Fetching Korea news...')
korea_news = fetch_rss('https://news.google.com/rss/search?q=South+Korea+economy&hl=en&gl=US&ceid=US:en', max_items=5)
korea_news += fetch_rss('https://news.google.com/rss/search?q=Samsung+SK+Hynix+semiconductor&hl=en&gl=US&ceid=US:en', max_items=5)
data['koreaNews'] = korea_news[:8]
print(f'  Korea: {len(data["koreaNews"])} items')

# 5. 주식
print('[5/5] Fetching stocks...')
data['worldStocks'] = [
    fetch_stock('NVDA', 'NVIDIA', 'USD'),
    fetch_stock('TSM', 'TSMC', 'USD'),
    fetch_stock('AMD', 'AMD', 'USD'),
    fetch_stock('INTC', 'Intel', 'USD'),
    fetch_stock('QCOM', 'Qualcomm', 'USD'),
    fetch_stock('ARM', 'ARM', 'USD'),
    fetch_stock('GOOGL', 'Google', 'USD'),
    fetch_stock('AAPL', 'Apple', 'USD'),
    fetch_stock('MSFT', 'Microsoft', 'USD'),
    fetch_stock('^GSPC', 'S&P 500', 'USD'),
    fetch_stock('^IXIC', 'NASDAQ', 'USD')
]
data['koreaStocks'] = [
    fetch_stock('005930.KS', 'Samsung', 'KRW'),
    fetch_stock('000660.KS', 'SK Hynix', 'KRW'),
    fetch_stock('005380.KS', 'Hyundai Motor', 'KRW'),
    fetch_stock('000270.KS', 'Kia', 'KRW'),
    fetch_stock('035420.KS', 'NAVER', 'KRW'),
    fetch_stock('^KS11', 'KOSPI', 'KRW'),
    fetch_stock('USDKRW=X', 'USD/KRW', 'FX')
]

data['updatedAt'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n✅ Done! Substack main: {len(data["myPosts"])}, Archive: {len(data.get("substackArchive", []))}, Medium: {len(data["mediumPosts"])}, Global: {len(data["globalNews"])}, Korea: {len(data["koreaNews"])}')
