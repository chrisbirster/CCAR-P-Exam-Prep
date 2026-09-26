#!/usr/bin/env python3
from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

PAGES = [
    {
        "source": ROOT / "content" / "home.md",
        "output": DIST / "index.html",
        "title": "CCAR-P Exam Prep",
        "asset_prefix": "",
        "home_href": "./",
        "objectives_href": "objectives/",
    },
    {
        "source": ROOT / "docs" / "exam-objectives.md",
        "output": DIST / "objectives" / "index.html",
        "title": "CCAR-P Exam Objectives",
        "asset_prefix": "../",
        "home_href": "../",
        "objectives_href": "./",
    },
]

def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    return text[end + 5:] if end != -1 else text

def render_markdown(text: str) -> str:
    body = markdown.markdown(
        strip_front_matter(text),
        extensions=["fenced_code", "tables", "sane_lists"],
        output_format="html5",
    )
    body = re.sub(
        r"<li>\[ \]\s*",
        '<li><input type="checkbox" disabled> ',
        body,
    )
    body = re.sub(
        r"<li>\[[xX]\]\s*",
        '<li><input type="checkbox" checked disabled> ',
        body,
    )
    body = re.sub(
        r"<h1>(Domain|D)([^<]*?)</h1>",
        lambda m: f"<h1>{m.group(1)}{m.group(2)}</h1>",
        body,
    )
    return body

def page_template(*, title: str, body: str, asset_prefix: str, home_href: str, objectives_href: str) -> str:
    safe_title = html.escape(title)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Community study material for the Claude Certified Architect – Professional exam.">
  <meta name="color-scheme" content="light dark">
  <title>{safe_title}</title>
  <link rel="stylesheet" href="{asset_prefix}style.css">
</head>
<body>
  <div class="site">
    <header>
      <h1>CCAR-P Exam Prep</h1>
      <nav aria-label="Primary">
        <a href="{home_href}">Home</a>
        <a href="{objectives_href}">Exam Objectives</a>
        <a href="https://github.com/chrisbirster/CCAR-P-Exam-Prep">GitHub</a>
      </nav>
    </header>
    <main>
      <article>
{body}
      </article>
    </main>
    <footer>
      Independent community study resource. Not affiliated with or endorsed by Anthropic.
      Verify exam details against Anthropic's current official materials.
    </footer>
  </div>
</body>
</html>
"""

def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    shutil.copy2(ROOT / "site" / "style.css", DIST / "style.css")

    for page in PAGES:
        source = page["source"]
        output = page["output"]
        output.parent.mkdir(parents=True, exist_ok=True)

        markdown_text = source.read_text(encoding="utf-8")
        body = render_markdown(markdown_text)
        rendered = page_template(
            title=page["title"],
            body=body,
            asset_prefix=page["asset_prefix"],
            home_href=page["home_href"],
            objectives_href=page["objectives_href"],
        )
        output.write_text(rendered, encoding="utf-8")

    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(PAGES)} pages into {DIST}")

if __name__ == "__main__":
    main()
