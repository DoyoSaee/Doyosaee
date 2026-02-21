# 프로필 README 자동 동기화 가이드

이 가이드를 각 프라이빗 레포에서 Claude Code에게 전달하면 자동 동기화를 설정해줍니다.

---

## 사전 준비 (한 번만 하면 됨)

### GitHub Personal Access Token (PAT) 생성
1. GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens**
2. **Token name**: `readme-sync`
3. **Repository access** → Only select repositories → 프로필 레포(`DoyoSaee/Doyosaee`) + 동기화할 프라이빗 레포들 선택
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

## 개별 레포용 설정 (이미지 포함)

아래 내용을 Claude Code에게 전달하세요:

```
이 레포의 README.md가 변경될 때마다 내 GitHub 프로필 레포(DoyoSaee/Doyosaee)의
projects/ 폴더에 자동으로 동기화하는 GitHub Actions 워크플로우를 만들어줘.
이미지도 함께 복사하고 경로를 변환해줘.

아래 내용으로 .github/workflows/sync-readme.yml 파일을 생성해줘:

name: Sync README to Profile

on:
  push:
    branches: [main]
    paths:
      - 'README.md'
      - 'public/img/**'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout this repo
        uses: actions/checkout@v4

      - name: Checkout profile repo
        uses: actions/checkout@v4
        with:
          repository: DoyoSaee/Doyosaee
          token: ${{ secrets.PROFILE_README_TOKEN }}
          path: profile-repo

      - name: Copy README and images
        run: |
          REPO_NAME="이레포이름"
          cp README.md profile-repo/projects/${REPO_NAME}.md
          mkdir -p profile-repo/projects/images/${REPO_NAME}
          if [ -d "public/img" ]; then
            cp -r public/img/* profile-repo/projects/images/${REPO_NAME}/
          fi
          sed -i "s|\./public/img/|projects/images/${REPO_NAME}/|g" profile-repo/projects/${REPO_NAME}.md

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

## 터보레포(모노레포)용 설정 (이미지 포함)

아래 내용을 Claude Code에게 전달하세요:

```
이 터보레포의 README.md가 변경될 때마다
내 GitHub 프로필 레포(DoyoSaee/Doyosaee)의 projects/ 폴더에
자동으로 동기화하는 GitHub Actions 워크플로우를 만들어줘.
이미지도 함께 복사하고 경로를 변환해줘.

아래 내용으로 .github/workflows/sync-readme.yml 파일을 생성해줘:

name: Sync README to Profile

on:
  push:
    branches: [main]
    paths:
      - 'README.md'
      - 'public/img/**'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout this repo
        uses: actions/checkout@v4

      - name: Checkout profile repo
        uses: actions/checkout@v4
        with:
          repository: DoyoSaee/Doyosaee
          token: ${{ secrets.PROFILE_README_TOKEN }}
          path: profile-repo

      - name: Copy README and images
        run: |
          REPO_NAME="이레포이름"
          cp README.md profile-repo/projects/${REPO_NAME}.md
          mkdir -p profile-repo/projects/images/${REPO_NAME}
          if [ -d "public/img" ]; then
            cp -r public/img/* profile-repo/projects/images/${REPO_NAME}/
          fi
          sed -i "s|\./public/img/|projects/images/${REPO_NAME}/|g" profile-repo/projects/${REPO_NAME}.md

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

## 동작 확인
1. 프라이빗 레포에서 README.md 수정 후 push
2. 해당 레포 → Actions 탭에서 워크플로우 실행 확인
3. 프로필 레포의 `projects/` 폴더에 파일이 생성되었는지 확인
4. 프로필 레포의 `projects/images/` 폴더에 이미지가 복사되었는지 확인
5. 프로필 README의 Private Repo README 섹션에 내용이 자동 추가되었는지 확인
