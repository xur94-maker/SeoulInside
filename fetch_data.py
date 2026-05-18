import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

# ── 헬퍼 함수 ────────────────────────────────────────────────
def fetch_rss(url, max_items=8):
    """RSS URL을 가져와서 항목 리스트 반환"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            root = ET.fromstring(r.read())
        items = []
        for item in root.iter("item"):
            title = (item.findtext("title") or "").strip()
            link  = (item.findtext("link")  or "").strip()
            date  = (item.findtext("pubDate") or "").strip()
            desc  = (item.findtext("description") or "").strip()
            # 태그 제거 (간단 버전)
            import re
            desc = re.sub(r"<[^>]+>", "", desc)[:200]
            if title and link:
                items.append({"title": title, "link": link, "date": date, "desc": desc})
            if len(items) >= max_items:
                break
        return items
    except Exception as e:
        print(f"  오류 ({url[:60]}): {e}")
        return []

def fetch_stock(symbol, label):
    """Yahoo Finance에서 주가 가져오기"""
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        meta = data["chart"]["result"][0]["meta"]
        price = meta.get("regularMarketPrice", 0)
        prev  = meta.get("previousClose", price)
        change = price - prev
        pct    = (change / prev * 100) if prev else 0
        return {
            "symbol": symbol,
            "label": label,
            "price": round(price, 2),
            "change": round(change, 2),
            "pct": round(pct, 2),
        }
    except Exception as e:
        print(f"  주가 오류 ({symbol}): {e}")
        return {"symbol": symbol, "label": label, "price": 0, "change": 0, "pct": 0}

# ── 수집 ─────────────────────────────────────────────────────
print("=== SeoulInside 데이터 수집 시작 ===")

data = {}

# 1) 내 서브스택 글
print("[1/4] 서브스택 RSS 수집 중...")
data["myPosts"] = fetch_rss("https://seoulinside.substack.com/feed", max_items=8)

# 2) 주요 글로벌 뉴스 (Reuters + AP)
print("[2/4] 글로벌 뉴스 수집 중...")
global_news = []
global_news += fetch_rss("https://feeds.reuters.com/reuters/topNews", max_items=5)
global_news += fetch_rss("https://rss.ap.org/feeds/APTop25News.rss", max_items=4)
data["globalNews"] = global_news[:8]

# 3) 한국 관련 해외 기사 (Google News RSS - Korea)
print("[3/4] 한국 관련 기사 수집 중...")
korea_feeds = [
    "https://news.google.com/rss/search?q=Korea+economy&hl=en&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=South+Korea+stock+Samsung&hl=en&gl=US&ceid=US:en",
]
korea_news = []
for feed in korea_feeds:
    korea_news += fetch_rss(feed, max_items=5)
data["koreaNews"] = korea_news[:8]

# 4) 주식 시황
print("[4/4] 주가 수집 중...")
world_stocks = [
    fetch_stock("AAPL",  "Apple"),
    fetch_stock("NVDA",  "NVIDIA"),
    fetch_stock("TSLA",  "Tesla"),
    fetch_stock("MSFT",  "Microsoft"),
    fetch_stock("AMZN",  "Amazon"),
    fetch_stock("^GSPC", "S&P 500"),
    fetch_stock("^IXIC", "NASDAQ"),
]
korea_stocks = [
    fetch_stock("005930.KS", "삼성전자"),
    fetch_stock("000660.KS", "SK하이닉스"),
    fetch_stock("005380.KS", "현대차"),
    fetch_stock("035420.KS", "NAVER"),
    fetch_stock("USDKRW=X",  "USD/KRW"),
]
data["worldStocks"] = world_stocks
data["koreaStocks"] = korea_stocks

# 5) 업데이트 시각
data["updatedAt"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# ── 저장 ─────────────────────────────────────────────────────
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ 완료! data.json 생성됨 ({data['updatedAt']})")
print(f"   내 글: {len(data['myPosts'])}개")
print(f"   글로벌 뉴스: {len(data['globalNews'])}개")
print(f"   한국 기사: {len(data['koreaNews'])}개")
print(f"   세계 주식: {len(data['worldStocks'])}개")
print(f"   한국 주식: {len(data['koreaStocks'])}개")
