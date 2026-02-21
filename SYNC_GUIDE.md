# 프로필 README 자동 동기화 가이드

이 가이드를 각 프라이빗 레포에서 Claude Code에게 전달하면 자동 동기화를 설정해줍니다.

---

## 사전 준비 (한 번만 하면 됨)

### GitHub Personal Access Token (PAT) 생성
1. GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens**
2. **Token name**: `readme-sync`
3. **Repository access** → Only select repositories → 프로필 레포(`Doyosaee/Doyosaee`) + 동기화할 프라이빗 레포들 선택
4. **Permissions**:
   - 프로필 레포: `Contents: Read and Write`
   - 프라이빗 레포들: `Contents: Read`
5. 토큰 생성 후 복사해둘 것

### 각 프라이빗 레포에 Secret 등록
1. 프라이빗 레포 → Settings → Secrets and variables → Actions
2. **New repository secret** 클릭
3. Name: `PROFILE_README_TOKEN`
4. Value: 위에서 생성한 PAT 붙여넣기

---

## 개별 레포용 설정

아래 내용을 Claude Code에게 전달하세요:

```
이 레포의 README.md가 변경될 때마다 내 GitHub 프로필 레포(Doyosaee/Doyosaee)의
projects/ 폴더에 자동으로 동기화하는 GitHub Actions 워크플로우를 만들어줘.

아래 내용으로 .github/workflows/sync-readme.yml 파일을 생성해줘:

name: Sync README to Profile

on:
  push:
    branches: [main]
    paths:
      - 'README.md'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout this repo
        uses: actions/checkout@v4

      - name: Checkout profile repo
        uses: actions/checkout@v4
        with:
          repository: Doyosaee/Doyosaee
          token: ${{ secrets.PROFILE_README_TOKEN }}
          path: profile-repo

      - name: Copy README
        run: cp README.md profile-repo/projects/이레포이름.md

      - name: Update project list
        run: cd profile-repo && python3 scripts/update-projects.py

      - name: Commit and push
        run: |
          cd profile-repo
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add projects/ README.md
          git diff --staged --quiet || git commit -m "chore: sync README from 이레포이름"
          git push

"이레포이름" 부분을 이 레포의 실제 이름으로 바꿔줘.
```

---

## 터보레포(모노레포)용 설정

아래 내용을 Claude Code에게 전달하세요:

```
이 터보레포의 apps/과 packages/ 하위 README.md가 변경될 때마다
내 GitHub 프로필 레포(Doyosaee/Doyosaee)의 projects/ 폴더에
각각 자동으로 동기화하는 GitHub Actions 워크플로우를 만들어줘.

아래 내용으로 .github/workflows/sync-readme.yml 파일을 생성해줘:

name: Sync READMEs to Profile

on:
  push:
    branches: [main]
    paths:
      - 'apps/*/README.md'
      - 'packages/*/README.md'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout this repo
        uses: actions/checkout@v4

      - name: Checkout profile repo
        uses: actions/checkout@v4
        with:
          repository: Doyosaee/Doyosaee
          token: ${{ secrets.PROFILE_README_TOKEN }}
          path: profile-repo

      - name: Copy all READMEs
        run: |
          for readme in $(find apps packages -name "README.md" 2>/dev/null); do
            dir_name=$(basename $(dirname "$readme"))
            cp "$readme" "profile-repo/projects/${dir_name}.md"
          done

      - name: Update project list
        run: cd profile-repo && python3 scripts/update-projects.py

      - name: Commit and push
        run: |
          cd profile-repo
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add projects/ README.md
          git diff --staged --quiet || git commit -m "chore: sync READMEs from turborepo"
          git push
```

---

## 동작 확인
1. 프라이빗 레포에서 README.md 수정 후 push
2. 해당 레포 → Actions 탭에서 워크플로우 실행 확인
3. 프로필 레포의 `projects/` 폴더에 파일이 생성되었는지 확인
4. 프로필 README의 Projects 섹션에 링크가 자동 추가되었는지 확인
