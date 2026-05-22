import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone


def strip_namespaces(raw_bytes):
    raw_bytes = raw_bytes.replace(b'content:encoded', b'content_encoded')
    raw_bytes = raw_bytes.replace(b'dc:creator', b'dc_creator')
    raw_bytes = raw_bytes.replace(b'dc:date', b'dc_date')
    raw_bytes = raw_bytes.replace(b'atom:link', b'atom_link')
    raw_bytes = raw_bytes.replace(b'media:content', b'media_content')
    raw_bytes = raw_bytes.replace(b'media:thumbnail', b'media_thumbnail')
    raw_bytes = re.sub(rb'\s+xmlns(?::[a-zA-Z0-9_]+)?="[^"]*"', b'', raw_bytes)
    raw_bytes = re.sub(rb"\s+xmlns(?::[a-zA-Z0-9_]+)?='[^']*'", b'', raw_bytes)
    return raw_bytes


def fetch_rss(url, max_items=8):
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/rss+xml, application/xml, text/xml, */*",
        })
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read()

        raw = strip_namespaces(raw)
        root = ET.fromstring(raw)
        items = []
        for item in root.iter('item'):
            title = (item.findtext('title') or '').strip()
            link  = (item.findtext('link')  or '').strip()
            date  = (item.findtext('pubDate') or item.findtext('dc_date') or '').strip()
            desc  = (item.findtext('content_encoded') or
                     item.findtext('description') or '').strip()
            desc  = re.sub(r'<[^>]+>', '', desc).strip()[:200]
            if title and link:
                items.append({'title': title, 'link': link, 'date': date, 'desc': desc})
            if len(items) >= max_items:
                break
        return items
    except Exception as e:
        print(f'  RSS error ({url[:60]}): {e}')
        return []


def fetch_stock(symbol, label):
    try:
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d'
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
        })
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        meta   = d['chart']['result'][0]['meta']
        price  = meta.get('regularMarketPrice', 0)
        prev   = meta.get('previousClose', price)
        change = price - prev
        pct    = (change / prev * 100) if prev else 0
        return {'symbol': symbol, 'label': label,
                'price': round(price, 2), 'change': round(change, 2), 'pct': round(pct, 2)}
    except Exception as e:
        print(f'  Stock error ({symbol}): {e}')
        return {'symbol': symbol, 'label': label, 'price': 0, 'change': 0, 'pct': 0}


def parse_date(date_str):
    """pubDate 문자열에서 날짜만 추출 (예: Thu, 21 May 2026 → 2026-05-21)"""
    try:
        dt = datetime.strptime(date_str[:25].strip(), '%a, %d %b %Y %H:%M:%S')
        return dt.strftime('%Y-%m-%d')
    except Exception:
        return date_str[:10] if date_str else ''


def generate_list_md(posts):
    """Substack 포스트 목록으로 list.md 생성"""
    lines = []
    for p in posts:
        date = parse_date(p.get('date', ''))
        title = p.get('title', '').strip()
        link  = p.get('link', '').strip()
        lines.append(f'# {title} | {date}')
        lines.append(link)
        lines.append('')
    return '\n'.join(lines)


# ── Data Collection Start ─────────────────────────────────────────────────
print('=== SeoulInside Data Collection Start ===')
data = {}

SUBSTACK_RSS = 'https://seoulinside.substack.com/feed'

# 1) Substack RSS → list.md 자동 생성
print('[1/4] Fetching Substack posts...')
substack_posts = fetch_rss(SUBSTACK_RSS, max_items=20)
if substack_posts:
    list_md = generate_list_md(substack_posts)
    with open('list.md', 'w', encoding='utf-8') as f:
        f.write(list_md)
    print(f'  Substack: {len(substack_posts)} posts → list.md 생성 완료')
else:
    print('  Substack RSS 실패 — list.md 유지')

# 2) Global news
print('[2/4] Fetching global news...')
global_news  = fetch_rss('https://feeds.bbci.co.uk/news/world/rss.xml', max_items=5)
global_news += fetch_rss('https://rss.nytimes.com/services/xml/rss/nyt/World.xml', max_items=4)
data['globalNews'] = global_news[:8]
print(f'  Global: {len(data["globalNews"])} items')

# 3) Korea-related news
print('[3/4] Fetching Korea-related news...')
korea_news  = fetch_rss('https://news.google.com/rss/search?q=South+Korea+economy&hl=en&gl=US&ceid=US:en', max_items=5)
korea_news += fetch_rss('https://news.google.com/rss/search?q=Samsung+SK+Hynix+semiconductor&hl=en&gl=US&ceid=US:en', max_items=5)
data['koreaNews'] = korea_news[:8]
print(f'  Korea: {len(data["koreaNews"])} items')

# 4) Stocks
print('[4/4] Fetching stock prices...')
data['worldStocks'] = [
    fetch_stock('NVDA',   'NVIDIA'),
    fetch_stock('TSM',    'TSMC'),
    fetch_stock('AMD',    'AMD'),
    fetch_stock('INTC',   'Intel'),
    fetch_stock('QCOM',   'Qualcomm'),
    fetch_stock('ARM',    'ARM'),
    fetch_stock('GOOGL',  'Google'),
    fetch_stock('AAPL',   'Apple'),
    fetch_stock('MSFT',   'Microsoft'),
    fetch_stock('^GSPC',  'S&P 500'),
    fetch_stock('^IXIC',  'NASDAQ'),
]
data['koreaStocks'] = [
    fetch_stock('005930.KS', 'Samsung'),
    fetch_stock('000660.KS', 'SK Hynix'),
    fetch_stock('005380.KS', 'Hyundai'),
    fetch_stock('000270.KS', 'Kia'),
    fetch_stock('035420.KS', 'NAVER'),
    fetch_stock('^KS11',     'KOSPI'),
    fetch_stock('USDKRW=X',  'USD/KRW'),
]

# Done
data['updatedAt'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n✅ Done! ({data["updatedAt"]})')
print(f'   Substack posts: {len(substack_posts)} → list.md')
print(f'   Global news   : {len(data["globalNews"])} items')
print(f'   Korea news    : {len(data["koreaNews"])} items')
print(f'   World stocks  : {len(data["worldStocks"])} items')
print(f'   Korea stocks  : {len(data["koreaStocks"])} items')
