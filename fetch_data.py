import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

# ── 헬퍼 함수 ────────────────────────────────────────────────

def fetch_rss(url, max_items=8):
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
            desc  = re.sub(r"<[^>]+>", "", desc)[:200]
            if title and link:
                items.append({"title": title, "link": link, "date": date, "desc": desc})
            if len(items) >= max_items:
                break
        return items
    except Exception as e:
        print(f"  오류 ({url[:60]}): {e}")
        return []


def fetch_latest_post_full(feed_url):
    """서브스택 최신 포스트 제목 + 전체 본문 HTML 가져오기"""
    try:
        req = urllib.request.Request(feed_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            raw = r.read()
        raw = raw.replace(b"content:encoded", b"content_encoded")
        root = ET.fromstring(raw)
        item = next(root.iter("item"), None)
        if item is None:
            return None
        title = (item.findtext("title") or "").strip()
        link  = (item.findtext("link")  or "").strip()
        date  = (item.findtext("pubDate") or "").strip()
        body  = (item.findtext("content_encoded") or
                 item.findtext("description") or "").strip()
        body = re.sub(r'<div class="subscription-widget.*', "", body, flags=re.DOTALL)
        return {"title": title, "link": link, "date": date, "body": body}
    except Exception as e:
        print(f"  최신 포스트 오류: {e}")
        return None


def fetch_stock(symbol, label):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            d = json.loads(r.read())
        meta   = d["chart"]["result"][0]["meta"]
        price  = meta.get("regularMarketPrice", 0)
        prev   = meta.get("previousClose", price)
        change = price - prev
        pct    = (change / prev * 100) if prev else 0
        return {"symbol": symbol, "label": label,
                "price": round(price, 2), "change": round(change, 2), "pct": round(pct, 2)}
    except Exception as e:
        print(f"  주가 오류 ({symbol}): {e}")
        return {"symbol": symbol, "label": label, "price": 0, "change": 0, "pct": 0}


# ── 수집 ─────────────────────────────────────────────────────
print("=== SeoulInside 데이터 수집 시작 ===")
data = {}
SUBSTACK_FEED = "https://seoulinside.substack.com/feed"

print("[1/5] 서브스택 RSS 수집 중...")
data["myPosts"]    = fetch_rss(SUBSTACK_FEED, max_items=8)
data["latestPost"] = fetch_latest_post_full(SUBSTACK_FEED)

print("[2/5] 글로벌 뉴스 수집 중...")
global_news  = fetch_rss("https://feeds.reuters.com/reuters/topNews", max_items=5)
global_news += fetch_rss("https://rss.ap.org/feeds/APTop25News.rss", max_items=4)
data["globalNews"] = global_news[:8]

print("[3/5] 한국 관련 기사 수집 중...")
korea_news  = fetch_rss("https://news.google.com/rss/search?q=Korea+economy&hl=en&gl=US&ceid=US:en", max_items=5)
korea_news += fetch_rss("https://news.google.com/rss/search?q=South+Korea+stock+Samsung&hl=en&gl=US&ceid=US:en", max_items=5)
data["koreaNews"] = korea_news[:8]

print("[4/5] 주가 수집 중...")
data["worldStocks"] = [
    fetch_stock("AAPL",  "Apple"),
    fetch_stock("NVDA",  "NVIDIA"),
    fetch_stock("TSLA",  "Tesla"),
    fetch_stock("MSFT",  "Microsoft"),
    fetch_stock("AMZN",  "Amazon"),
    fetch_stock("^GSPC", "S&P 500"),
    fetch_stock("^IXIC", "NASDAQ"),
]
data["koreaStocks"] = [
    fetch_stock("005930.KS", "삼성전자"),
    fetch_stock("000660.KS", "SK하이닉스"),
    fetch_stock("005380.KS", "현대차"),
    fetch_stock("035420.KS", "NAVER"),
    fetch_stock("USDKRW=X",  "USD/KRW"),
]

print("[5/5] 완료 처리 중...")
data["updatedAt"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

lp = data["latestPost"]
print(f"\n✅ 완료! data.json 생성됨 ({data['updatedAt']})")
print(f"   내 글 목록:  {len(data['myPosts'])}개")
print(f"   최신 포스트: {lp['title'][:50] if lp else '없음'}")
print(f"   글로벌 뉴스: {len(data['globalNews'])}개")
print(f"   한국 기사:   {len(data['koreaNews'])}개")
