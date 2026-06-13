"""
update_readme.py
RSS 피드(seoulinside.substack.com)에서 최신 글을 가져와
README.md의 BLOG-POST-LIST 섹션을 자동으로 갱신합니다.
"""

import re
import feedparser
from datetime import datetime, timezone

# ── 설정 ──────────────────────────────────────────────
FEED_URL   = "https://seoulinside.substack.com/feed"
README     = "README.md"
MAX_POSTS  = 5
START_TAG  = "<!-- BLOG-POST-LIST:START -->"
END_TAG    = "<!-- BLOG-POST-LIST:END -->"
# ──────────────────────────────────────────────────────


def fetch_posts() -> list[dict]:
    feed = feedparser.parse(FEED_URL)
    posts = []
    for entry in feed.entries[:MAX_POSTS]:
        posts.append({
            "title": entry.get("title", "제목 없음"),
            "link":  entry.get("link", ""),
            "date":  entry.get("published", ""),
        })
    return posts


def format_date(raw: str) -> str:
    """'Wed, 11 Jun 2025 10:00:00 +0000' → '2025.06.11'"""
    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
    ):
        try:
            return datetime.strptime(raw, fmt).strftime("%Y.%m.%d")
        except ValueError:
            continue
    return raw[:10] if raw else ""


def build_block(posts: list[dict]) -> str:
    lines = []
    for p in posts:
        date = format_date(p["date"])
        date_str = f" `{date}`" if date else ""
        lines.append(f"- [{p['title']}]({p['link']}){date_str}")
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines.append(f"\n> 🔄 마지막 업데이트: {updated}")
    return "\n".join(lines)


def update_readme(block: str) -> None:
    with open(README, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = re.compile(
        rf"{re.escape(START_TAG)}.*?{re.escape(END_TAG)}",
        re.DOTALL,
    )
    replacement = f"{START_TAG}\n{block}\n{END_TAG}"

    if not pattern.search(text):
        print("⚠️  태그를 찾지 못했습니다. 파일 끝에 추가합니다.")
        new_text = text.rstrip() + f"\n\n{replacement}\n"
    else:
        new_text = pattern.sub(replacement, text)

    if new_text == text:
        print("변경 사항 없음 — README 이미 최신 상태입니다.")
        return

    with open(README, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("✅ README 업데이트 완료!")


if __name__ == "__main__":
    print(f"📡 RSS 가져오는 중: {FEED_URL}")
    posts = fetch_posts()

    if not posts:
        print("❌ 게시물을 가져오지 못했습니다. 피드를 확인해주세요.")
        raise SystemExit(1)

    print(f"📝 {len(posts)}개 게시물 발견:")
    for i, p in enumerate(posts, 1):
        print(f"  {i}. {p['title']}")

    block = build_block(posts)
    update_readme(block)
