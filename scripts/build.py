#!/usr/bin/env python3
from __future__ import annotations

import html
import os
import re
import shutil
from pathlib import Path

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
    {
        "source": ROOT / "docs" / "flashcard-plan.md",
        "output": DIST / "flashcards" / "index.html",
        "title": "CCAR-P Flashcard Plan",
        "asset_prefix": "../",
        "home_href": "../",
        "objectives_href": "../objectives/",
    },
    {
        "source": ROOT / "flashcards" / "source" / "README.md",
        "output": DIST / "flashcards" / "source" / "index.html",
        "title": "CCAR-P Flashcard Source",
        "asset_prefix": "../../",
        "home_href": "../../",
        "objectives_href": "../../objectives/",
    },
    {
        "source": ROOT / "docs" / "sources-and-verification.md",
        "output": DIST / "verification" / "index.html",
        "title": "CCAR-P Sources & Verification",
        "asset_prefix": "../",
        "home_href": "../",
        "objectives_href": "../objectives/",
    },
    {
        "source": ROOT / "docs" / "concepts" / "README.md",
        "output": DIST / "concepts" / "index.html",
        "title": "CCAR-P Concept Notes",
        "asset_prefix": "../",
        "home_href": "../",
        "objectives_href": "../objectives/",
    },
    {
        "source": ROOT / "docs" / "concepts" / "d1-solution-design.md",
        "output": DIST / "concepts" / "d1-solution-design" / "index.html",
        "title": "D1 — Solution Design & Architecture",
        "asset_prefix": "../../",
        "home_href": "../../",
        "objectives_href": "../../objectives/",
    },
    {
        "source": ROOT / "docs" / "concepts" / "d2-models-prompting-context.md",
        "output": DIST / "concepts" / "d2-models-prompting-context" / "index.html",
        "title": "D2 — Models, Prompting & Context",
        "asset_prefix": "../../",
        "home_href": "../../",
        "objectives_href": "../../objectives/",
    },
    {
        "source": ROOT / "docs" / "concepts" / "d3-integration.md",
        "output": DIST / "concepts" / "d3-integration" / "index.html",
        "title": "D3 — Integration",
        "asset_prefix": "../../",
        "home_href": "../../",
        "objectives_href": "../../objectives/",
    },
    {
        "source": ROOT / "docs" / "concepts" / "d4-evaluation-testing-optimization.md",
        "output": DIST / "concepts" / "d4-evaluation-testing-optimization" / "index.html",
        "title": "D4 — Evaluation, Testing & Optimization",
        "asset_prefix": "../../",
        "home_href": "../../",
        "objectives_href": "../../objectives/",
    },
    {
        "source": ROOT / "docs" / "concepts" / "d5-governance-safety-risk.md",
        "output": DIST / "concepts" / "d5-governance-safety-risk" / "index.html",
        "title": "D5 — Governance, Safety & Risk",
        "asset_prefix": "../../",
        "home_href": "../../",
        "objectives_href": "../../objectives/",
    },
    {
        "source": ROOT / "docs" / "concepts" / "d6-stakeholder-lifecycle.md",
        "output": DIST / "concepts" / "d6-stakeholder-lifecycle" / "index.html",
        "title": "D6 — Stakeholder & Lifecycle",
        "asset_prefix": "../../",
        "home_href": "../../",
        "objectives_href": "../../objectives/",
    },
    {
        "source": ROOT / "docs" / "concepts" / "d7-developer-productivity.md",
        "output": DIST / "concepts" / "d7-developer-productivity" / "index.html",
        "title": "D7 — Developer Productivity",
        "asset_prefix": "../../",
        "home_href": "../../",
        "objectives_href": "../../objectives/",
    },
]


REFERENCES_DIR = ROOT / "docs" / "references"
for source in sorted(REFERENCES_DIR.glob("*.md")):
    if source.name == "README.md":
        output = DIST / "references" / "index.html"
        title = "CCAR-P References"
        asset_prefix = "../"
        home_href = "../"
        objectives_href = "../objectives/"
    else:
        output = DIST / "references" / source.stem / "index.html"
        title = source.stem.replace("-", " ").title()
        asset_prefix = "../../"
        home_href = "../../"
        objectives_href = "../../objectives/"

    PAGES.append({
        "source": source,
        "output": output,
        "title": title,
        "asset_prefix": asset_prefix,
        "home_href": home_href,
        "objectives_href": objectives_href,
    })


AUDIT_DIR = ROOT / "docs" / "audit"
for source in sorted(AUDIT_DIR.glob("*.md")):
    if source.name == "README.md":
        output = DIST / "audit" / "index.html"
        title = "CCAR-P Notes Audit"
        asset_prefix = "../"
        home_href = "../"
        objectives_href = "../objectives/"
    else:
        output = DIST / "audit" / source.stem / "index.html"
        title = source.stem.replace("-", " ").title()
        asset_prefix = "../../"
        home_href = "../../"
        objectives_href = "../../objectives/"

    PAGES.append({
        "source": source,
        "output": output,
        "title": title,
        "asset_prefix": asset_prefix,
        "home_href": home_href,
        "objectives_href": objectives_href,
    })

PAGE_OUTPUT_BY_SOURCE = {
    page["source"].resolve(): page["output"].resolve()
    for page in PAGES
}

CURRENT_SOURCE: Path | None = None
CURRENT_OUTPUT: Path | None = None

CODE_TOKEN = re.compile(r"`([^`]+)`")
LINK_TOKEN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_TOKEN = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_TOKEN = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    return text[end + 5:] if end != -1 else text


def inline(text: str) -> str:
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"\x00{len(placeholders) - 1}\x00"

    def code_sub(match: re.Match[str]) -> str:
        return stash(f"<code>{html.escape(match.group(1))}</code>")

    def link_sub(match: re.Match[str]) -> str:
        label = html.escape(match.group(1))
        href_raw = match.group(2)

        # Resolve Markdown-source links to their generated Pages route. This
        # preserves correct links both in the GitHub source tree and in the
        # clean directory-style static site.
        if (
            "://" not in href_raw
            and not href_raw.startswith("#")
            and CURRENT_SOURCE is not None
            and CURRENT_OUTPUT is not None
        ):
            md_match = re.match(r"^(.*?\.md)([#?].*)?$", href_raw)
            if md_match:
                source_href = md_match.group(1)
                suffix = md_match.group(2) or ""
                target_source = (CURRENT_SOURCE.parent / source_href).resolve()
                target_output = PAGE_OUTPUT_BY_SOURCE.get(target_source)

                if target_output is not None:
                    target_dir = (
                        target_output.parent
                        if target_output.name == "index.html"
                        else target_output
                    )
                    relative = os.path.relpath(
                        target_dir,
                        CURRENT_OUTPUT.parent,
                    ).replace(os.sep, "/")
                    if relative == ".":
                        relative = "./"
                    elif not relative.endswith("/"):
                        relative += "/"
                    href_raw = relative + suffix

        href = html.escape(href_raw, quote=True)
        return stash(f'<a href="{href}">{label}</a>')

    text = CODE_TOKEN.sub(code_sub, text)
    text = LINK_TOKEN.sub(link_sub, text)
    text = html.escape(text)
    text = BOLD_TOKEN.sub(r"<strong>\1</strong>", text)
    text = ITALIC_TOKEN.sub(r"<em>\1</em>", text)

    for index, value in enumerate(placeholders):
        token = f"\x00{index}\x00"
        text = text.replace(html.escape(token), value).replace(token, value)
    return text


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return len(cells) >= 2 and all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells
    )


def render_markdown(text: str) -> str:
    lines = strip_front_matter(text).splitlines()
    out: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        if stripped.startswith("```"):
            language = stripped[3:].strip()
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            class_name = (
                f' class="language-{html.escape(language)}"' if language else ""
            )
            out.append(
                f'<pre><code{class_name}>{html.escape(chr(10).join(code))}</code></pre>'
            )
            continue

        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            out.append("<hr>")
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2)
            slug = re.sub(
                r"[^a-z0-9]+",
                "-",
                re.sub(r"<[^>]+>", "", title).lower(),
            ).strip("-")
            out.append(f'<h{level} id="{slug}">{inline(title)}</h{level}>')
            index += 1
            continue

        if stripped.startswith(">"):
            quote: list[str] = []
            while index < len(lines) and lines[index].lstrip().startswith(">"):
                quote.append(lines[index].lstrip()[1:].lstrip())
                index += 1
            out.append(f'<blockquote><p>{inline(" ".join(quote))}</p></blockquote>')
            continue

        if (
            index + 1 < len(lines)
            and "|" in stripped
            and is_table_separator(lines[index + 1])
        ):
            headers = split_table_row(line)
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append(split_table_row(lines[index]))
                index += 1

            out.append('<div class="table-wrap"><table><thead><tr>')
            for cell in headers:
                out.append(f"<th>{inline(cell)}</th>")
            out.append("</tr></thead><tbody>")
            for row in rows:
                out.append("<tr>")
                for cell in row:
                    out.append(f"<td>{inline(cell)}</td>")
                out.append("</tr>")
            out.append("</tbody></table></div>")
            continue

        unordered = re.match(r"^[-*+]\s+(.+)$", stripped)
        ordered = re.match(r"^\d+[.)]\s+(.+)$", stripped)
        if unordered or ordered:
            is_ordered = bool(ordered)
            tag = "ol" if is_ordered else "ul"
            out.append(f"<{tag}>")

            while index < len(lines):
                current = lines[index].strip()
                item_match = (
                    re.match(r"^\d+[.)]\s+(.+)$", current)
                    if is_ordered
                    else re.match(r"^[-*+]\s+(.+)$", current)
                )
                if not item_match:
                    break

                item = item_match.group(1)
                task = re.match(r"^\[([ xX])\]\s*(.*)$", item)
                if task:
                    checked = " checked" if task.group(1).lower() == "x" else ""
                    out.append(
                        f'<li class="task"><input type="checkbox" disabled{checked}> '
                        f"{inline(task.group(2))}</li>"
                    )
                else:
                    out.append(f"<li>{inline(item)}</li>")
                index += 1

            out.append(f"</{tag}>")
            continue

        paragraph = [stripped]
        index += 1
        while index < len(lines):
            next_line = lines[index].strip()
            if not next_line:
                break
            if next_line.startswith(("#", "```", ">")):
                break
            if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", next_line):
                break
            if re.match(r"^[-*+]\s+", next_line) or re.match(
                r"^\d+[.)]\s+", next_line
            ):
                break
            if (
                index + 1 < len(lines)
                and "|" in next_line
                and is_table_separator(lines[index + 1])
            ):
                break
            paragraph.append(next_line)
            index += 1

        out.append(f'<p>{inline(" ".join(paragraph))}</p>')

    return "\n".join(out)


def page_template(
    *,
    title: str,
    body: str,
    asset_prefix: str,
    home_href: str,
    objectives_href: str,
) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Community study material for the Claude Certified Architect – Professional exam.">
  <meta name="color-scheme" content="light dark">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{asset_prefix}style.css">
</head>
<body>
  <div class="site">
    <header>
      <h1>CCAR-P Exam Prep</h1>
      <nav aria-label="Primary">
        <a href="{home_href}">Home</a>
        <a href="{objectives_href}">Exam Objectives</a>
        <a href="{home_href}concepts/">Concept Notes</a>
        <a href="{home_href}references/">References</a>
        <a href="{home_href}audit/">Audit</a>
        <a href="{home_href}flashcards/">Flashcard Plan</a>
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

    # Publish generated study artifacts alongside the flashcard-plan page.
    flashcard_dist = DIST / "flashcards"
    flashcard_dist.mkdir(parents=True, exist_ok=True)
    for priority in ("p0", "p1"):
        for suffix in (".nut", "-api.json"):
            source = ROOT / "flashcards" / f"ccar-p-{priority}{suffix}"
            if source.exists():
                shutil.copy2(source, flashcard_dist / source.name)

    source_batches = ROOT / "flashcards" / "batches"
    if source_batches.exists():
        batch_dist = flashcard_dist / "batches"
        batch_dist.mkdir(parents=True, exist_ok=True)
        for priority in ("p0", "p1"):
            for source in sorted(source_batches.glob(f"{priority}-*.json")):
                shutil.copy2(source, batch_dist / source.name)

    global CURRENT_SOURCE, CURRENT_OUTPUT

    for page in PAGES:
        output: Path = page["output"]
        output.parent.mkdir(parents=True, exist_ok=True)
        source: Path = page["source"]
        CURRENT_SOURCE = source.resolve()
        CURRENT_OUTPUT = output.resolve()
        body = render_markdown(source.read_text(encoding="utf-8"))
        output.write_text(
            page_template(
                title=page["title"],
                body=body,
                asset_prefix=page["asset_prefix"],
                home_href=page["home_href"],
                objectives_href=page["objectives_href"],
            ),
            encoding="utf-8",
        )

    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(PAGES)} pages into {DIST}")


if __name__ == "__main__":
    main()
