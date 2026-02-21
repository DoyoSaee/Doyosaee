import os
import re

PROJECTS_DIR = "projects"
README_PATH = "README.md"


def parse_project(filepath):
    """md 파일에서 제목, 설명, 링크를 추출"""
    title = os.path.splitext(os.path.basename(filepath))[0]
    description = ""
    link = ""

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        stripped = line.strip()
        # 제목 추출
        match = re.match(r"^#\s+(.+)", stripped)
        if match and title == os.path.splitext(os.path.basename(filepath))[0]:
            title = match.group(1)
            continue
        # 링크 추출 (URL)
        url_match = re.search(r"(https?://[^\s\)]+)", stripped)
        if url_match and not link:
            link = url_match.group(1)
            continue
        # 설명 추출 (첫 번째 일반 텍스트 줄)
        if stripped and not description and not stripped.startswith(("#", "!", "[", "<", "---", "```", "|")):
            description = stripped

    return title, description, link


def main():
    if not os.path.isdir(PROJECTS_DIR):
        return

    project_files = sorted(
        [f for f in os.listdir(PROJECTS_DIR) if f.endswith(".md")]
    )

    if not project_files:
        project_section = ""
    else:
        cards = []
        for f in project_files:
            filepath = os.path.join(PROJECTS_DIR, f)
            title, description, link = parse_project(filepath)

            card = f'<table><tr><td>\n'
            card += f'<h3>{title}</h3>\n'
            if description:
                card += f'<p>{description}</p>\n'
            if link:
                card += f'<a href="{link}">{link}</a>\n'
            card += f'</td></tr></table>'
            cards.append(card)

        project_section = "\n<br>\n".join(cards)

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    pattern = r"(<!-- PROJECTS:START -->).*?(<!-- PROJECTS:END -->)"
    replacement = f"\\1\n{project_section}\n\\2"
    updated = re.sub(pattern, replacement, readme, flags=re.DOTALL)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"Updated {len(project_files)} projects in README.md")


if __name__ == "__main__":
    main()
