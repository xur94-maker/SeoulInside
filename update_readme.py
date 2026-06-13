"""
update_readme.py
─────────────────
RSS 피드(seoulinside.substack.com)에서 최신 글을 가져와:
  1. README.md 의 BLOG-POST-LIST 섹션을 자동 갱신 (제목 + 요약 포함 → SEO)
  2. index.html 이 읽는 data.json 의 myPosts / latestPost 를 갱신
"""

import json
import re
import html
import feedparser
from datetime import datetime, timezone
from pathlib import Path

# ── 설정 ──────────────────────────────────────────────
FEED_URL      = "https://seoulinside.substack.com/feed"
README_PATH   = "README.md"
DATA_JSON     = "data.json"
MAX_POSTS     = 10   # README 목록 & data.json myPosts 개수
SUMMARY_CHARS = 150  # README에 넣을 요약 최대 글자수
START_TAG     = "<!-- BLOG-POST-LIST:START -->"
END_TAG       = "<!-- BLOG-POST-LIST:END -->"
# ──────────────────────────────────────────────────────


# ── RSS 가져오기 ───────────────────────────────────────
def strip_html(raw: str) -> str:
    """HTML 태그 제거 후 공백 정리"""
    clean = re.sub(r"<[^>]+>", " ", raw)
    clean = html.unescape(clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean


def fetch_entries(feed_url: str, max_n: int) -> list[dict]:
    feed = feedparser.parse(feed_url)
    results = []
    for entry in feed.entries[:max_n]:
        # 본문 HTML (data.json latestPost용)
        body_html = ""
        if hasattr(entry, "content"):
            body_html = entry.content[0].get("value", "")
        elif hasattr(entry, "summary"):
            body_html = entry.summary

        # 요약 텍스트 (README SEO용) — summary 우선, 없으면 본문 앞부분
        summary_raw = entry.get("summary", body_html)
        summary_text = strip_html(summary_raw)
        if len(summary_text) > SUMMARY_CHARS:
            summary_text = summary_text[:SUMMARY_CHARS].rsplit(" ", 1)[0] + "…"

        results.append({
            "title":   entry.get("title", "제목 없음"),
            "link":    entry.get("link", ""),
            "date":    entry.get("published", ""),
            "summary": summary_text,
            "body":    body_html,
        })
    return results


def format_date(raw: str) -> str:
    """'Wed, 11 Jun 2025 10:00:00 +0000' → '2025.06.11'"""
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z"):
        try:
            return datetime.strptime(raw, fmt).strftime("%Y.%m.%d")
        except ValueError:
            continue
    return raw[:10] if raw else ""


# ── 1. README 갱신 ─────────────────────────────────────
def build_readme_block(entries: list[dict]) -> str:
    """
    각 글을 제목 + 날짜 + 요약 형태로 렌더링.
    구글이 제목과 요약 텍스트를 모두 인덱싱할 수 있어 SEO에 효과적.
    """
    lines = []
    for e in entries:
        date = format_date(e["date"])
        date_str = f" `{date}`" if date else ""
        lines.append(f"### [{e['title']}]({e['link']}){date_str}")
        if e["summary"]:
            lines.append(f"{e['summary']}")
        lines.append("")  # 빈 줄로 구분

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines.append(f"> 🔄 마지막 업데이트: {updated}")
    return "\n".join(lines)


def update_readme(block: str) -> None:
    path = Path(README_PATH)
    if not path.exists():
        print(f"⚠️  {README_PATH} 파일이 없습니다. 건너뜁니다.")
        return

    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(START_TAG)}.*?{re.escape(END_TAG)}", re.DOTALL
    )
    replacement = f"{START_TAG}\n{block}\n{END_TAG}"

    if not pattern.search(text):
        print("⚠️  README에 태그 없음 — 파일 끝에 추가합니다.")
        new_text = text.rstrip() + f"\n\n{replacement}\n"
    else:
        new_text = pattern.sub(replacement, text)

    if new_text == text:
        print("README 변경 없음.")
        return

    path.write_text(new_text, encoding="utf-8")
    print("✅ README.md 갱신 완료")


# ── 2. data.json 갱신 ─────────────────────────────────
def update_data_json(entries: list[dict]) -> None:
    data_path = Path(DATA_JSON)

    existing: dict = {}
    if data_path.exists():
        try:
            existing = json.loads(data_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    my_posts = [
        {"title": e["title"], "link": e["link"], "date": e["date"]}
        for e in entries
    ]

    latest = entries[0] if entries else None
    latest_post = (
        {"title": latest["title"], "link": latest["link"],
         "date": latest["date"], "body": latest["body"]}
        if latest
        else existing.get("latestPost", {})
    )

    existing.update({
        "myPosts":    my_posts,
        "latestPost": latest_post,
        "updatedAt":  now_str,
    })

    data_path.write_text(
        json.dumps(existing, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("✅ data.json 갱신 완료")


# ── 메인 ──────────────────────────────────────────────
if __name__ == "__main__":
    print(f"📡 RSS 가져오는 중: {FEED_URL}")
    entries = fetch_entries(FEED_URL, MAX_POSTS)

    if not entries:
        print("❌ 게시물을 가져오지 못했습니다. 피드를 확인해주세요.")
        raise SystemExit(1)

    print(f"📝 {len(entries)}개 게시물 발견:")
    for i, e in enumerate(entries, 1):
        print(f"  {i}. {e['title']}")

    update_readme(build_readme_block(entries))
    update_data_json(entries)

    print("\n🎉 완료!")
