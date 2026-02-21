import os
import re

PROJECTS_DIR = "projects"
README_PATH = "README.md"


def get_title(filepath):
    """md 파일의 첫 번째 # 제목을 추출"""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^#\s+(.+)", line.strip())
            if match:
                return match.group(1)
    return os.path.splitext(os.path.basename(filepath))[0]


def main():
    if not os.path.isdir(PROJECTS_DIR):
        return

    project_files = sorted(
        [f for f in os.listdir(PROJECTS_DIR) if f.endswith(".md")]
    )

    if not project_files:
        project_section = ""
    else:
        sections = []
        for f in project_files:
            filepath = os.path.join(PROJECTS_DIR, f)
            with open(filepath, "r", encoding="utf-8") as fh:
                content = fh.read().strip()
            sections.append(content)
        project_section = "\n\n---\n\n".join(sections)

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
