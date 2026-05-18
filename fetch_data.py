import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone


def fetch_rss(url, max_items=8):
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/rss+xml, application/xml, text/xml, */*",
        })
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read()

        # 모든 네임스페이스 제거 후 파싱
        raw = re.sub(rb'<([a-zA-Z]+):[a-zA-Z]+', lambda m: m.group(0), raw)
        raw = re.sub(rb' xmlns[^"]*"[^"]*"', b'', raw)
        raw = re.sub(rb' xmlns[^\']*\'[^\']*\'', b'', raw)

        # 네임스페이스 태그 단순화
        raw = raw.replace(b'content:encoded', b'content_encoded')
        raw = raw.replace(b'dc:creator', b'dc_creator')
        raw = raw.replace(b'dc:date', b'dc_date')
        raw = raw.replace(b'media:content', b'media_content')
        raw = raw.replace(b'media:thumbnail', b'media_thumbnail')
        raw = raw.replace(b'atom:link', b'atom_link')

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
        print(f'  RSS 오류 ({url[:60]}): {e}')
        return []


def fetch_substack(feed_url, max_items=8):
    """서브스택 전용 RSS 파서"""
    try:
        req = urllib.request.Request(feed_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/rss+xml, application/xml, text/xml, */*",
        })
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read()

        # 네임스페이스 제거
        raw = raw.replace(b'content:encoded', b'content_encoded')
        raw = raw.replace(b'dc:creator', b'dc_creator')
        raw = raw.replace(b'dc:date', b'dc_date')
        raw = raw.replace(b'atom:link', b'atom_link')
        raw = re.sub(rb' xmlns[^=]*="[^"]*"', b'', raw)

        root = ET.fromstring(raw)

        posts = []
        latest_body = None
        latest_title = None
        latest_link = None
        latest_date = None

        for i, item in enumerate(root.iter('item')):
            title = (item.findtext('title') or '').strip()
            link  = (item.findtext('link')  or '').strip()
            date  = (item.findtext('pubDate') or '').strip()
            body  = (item.findtext('content_encoded') or
                     item.findtext('description') or '').strip()

            desc = re.sub(r'<[^>]+>', '', body).strip()[:200]

            if title and link:
                posts.append({'title': title, 'link': link, 'date': date, 'desc': desc})

            # 최신 포스트 전문 저장
            if i == 0 and body:
                latest_title = title
                latest_link  = link
                latest_date  = date
                # 서브스택 구독 푸터 제거
                body = re.sub(r'<div class="subscription-widget.*', '', body, flags=re.DOTALL)
                latest_body = body

            if len(posts) >= max_items:
                break

        latest = None
        if latest_title and latest_body:
            latest = {'title': latest_title, 'link': latest_link,
                      'date': latest_date, 'body': latest_body}

        print(f'  서브스택: {len(posts)}개 파싱됨')
        return posts, latest

    except Exception as e:
        print(f'  서브스택 오류: {e}')
        return [], None


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
        print(f'  주가 오류 ({symbol}): {e}')
        return {'symbol': symbol, 'label': label, 'price': 0, 'change': 0, 'pct': 0}


# ── 수집 시작 ─────────────────────────────────────────────────
print('=== SeoulInside 데이터 수집 시작 ===')
data = {}
SUBSTACK_FEED = 'https://seoulinside.substack.com/feed'

# 1) 서브스택 (전용 파서)
print('[1/5] 서브스택 수집 중...')
data['myPosts'], data['latestPost'] = fetch_substack(SUBSTACK_FEED, max_items=8)

# 2) 글로벌 뉴스
print('[2/5] 글로벌 뉴스 수집 중...')
global_news  = fetch_rss('https://feeds.bbci.co.uk/news/world/rss.xml', max_items=5)
global_news += fetch_rss('https://rss.nytimes.com/services/xml/rss/nyt/World.xml', max_items=4)
data['globalNews'] = global_news[:8]
print(f'  글로벌: {len(data["globalNews"])}개')

# 3) 한국 관련 기사
print('[3/5] 한국 관련 기사 수집 중...')
korea_news  = fetch_rss('https://news.google.com/rss/search?q=South+Korea+economy&hl=en&gl=US&ceid=US:en', max_items=5)
korea_news += fetch_rss('https://news.google.com/rss/search?q=Samsung+SK+Hynix+semiconductor&hl=en&gl=US&ceid=US:en', max_items=5)
data['koreaNews'] = korea_news[:8]
print(f'  한국: {len(data["koreaNews"])}개')

# 4) 주식
print('[4/5] 주가 수집 중...')
data['worldStocks'] = [
    fetch_stock('NVDA',  'NVIDIA'),
    fetch_stock('TSM',   'TSMC'),
    fetch_stock('AMD',   'AMD'),
    fetch_stock('INTC',  'Intel'),
    fetch_stock('QCOM',  'Qualcomm'),
    fetch_stock('ARM',   'ARM'),
    fetch_stock('^GSPC', 'S&P 500'),
    fetch_stock('^IXIC', 'NASDAQ'),
]
data['koreaStocks'] = [
    fetch_stock('005930.KS', '삼성전자'),
    fetch_stock('000660.KS', 'SK하이닉스'),
    fetch_stock('035420.KS', 'NAVER'),
    fetch_stock('USDKRW=X',  'USD/KRW'),
]

# 5) 완료
print('[5/5] 저장 중...')
data['updatedAt'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

lp = data['latestPost']
print(f'\n✅ 완료! ({data["updatedAt"]})')
print(f'   서브스택: {len(data["myPosts"])}개 | 최신글: {lp["title"][:40] if lp else "없음"}')
