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
        print(f'  RSS 오류 ({url[:60]}): {e}')
        return []


def fetch_wordpress_news(url):
    """워드프레스 칠판 페이지에서 내용을 직접 읽어옴"""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,*/*",
        })
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read().decode('utf-8', errors='ignore')

        # <article> 또는 <div class="entry-content"> 안의 텍스트 추출
        # 워드프레스는 보통 entry-content 클래스에 본문이 있음
        match = re.search(r'class="entry-content"[^>]*>(.*?)</div>', raw, re.DOTALL)
        if not match:
            match = re.search(r'<article[^>]*>(.*?)</article>', raw, re.DOTALL)

        if match:
            content = match.group(1)
            # HTML 태그 제거
            content = re.sub(r'<[^>]+>', '\n', content)
            # 빈 줄 정리
            lines = [l.strip() for l in content.splitlines() if l.strip()]
            content = '\n'.join(lines)
            print(f'  워드프레스 칠판: {len(lines)}줄 읽음')
            return content
        else:
            print('  워드프레스 칠판: 본문을 찾지 못함')
            return ''

    except Exception as e:
        print(f'  워드프레스 오류: {e}')
        return ''


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

WORDPRESS_NEWS_URL = 'https://seoulinside.wordpress.com/2026/05/18/news/'

# 1) 워드프레스 칠판 (서브스택 대체)
print('[1/5] 워드프레스 칠판 읽는 중...')
data['wordpressNews'] = fetch_wordpress_news(WORDPRESS_NEWS_URL)
data['wordpressNewsUrl'] = WORDPRESS_NEWS_URL

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

print(f'\n✅ 완료! ({data["updatedAt"]})')
print(f'   워드프레스 칠판: {len(data["wordpressNews"])}자 읽음')
print(f'   글로벌 뉴스: {len(data["globalNews"])}개')
print(f'   한국 뉴스: {len(data["koreaNews"])}개')
