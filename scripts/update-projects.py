import os
import re

PROJECTS_DIR = "projects"
README_PATH = "README.md"


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
        project_section += '\n\n<p align="right"><sub>🔄 프라이빗 레포에서 GitHub Actions로 자동 동기화됨</sub></p>'

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
