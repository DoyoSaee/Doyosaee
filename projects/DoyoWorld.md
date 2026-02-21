# DoyoWorld Monorepo

풀사이클 엔지니어링을 지향하는 모노레포입니다. 홈랩 인프라(K3s) 구축부터 웹/모바일 앱 배포까지, 서비스의 전체 라이프사이클을 담고 있습니다.

**빌드**: Turborepo | **패키지 매니저**: pnpm 9 | **Node**: >= 18

---

## Projects Overview

| # | 프로젝트 | 설명 | 상태 |
|---|----------|------|------|
| 01 | [**FirstWing**](#01-firstwing--프로토타입) | 모노레포 구축 및 초기 PoC | 완료 |
| 02 | [**DevPulse**](#02-devpulse--ai-기술-뉴스-플랫폼) | AI 기반 기술 뉴스 요약 플랫폼 (Web + API + Mobile) | 운영 중 |
| 03 | [**ThirdWing**](#03-thirdwing--판금-업체-mvp) | 레이저 판금 업체 생산관리 MVP (Web + API) | 실험 |
| 04 | [**ForthWing**](#04-forthwing--멀티-벤더-이커머스) | 멀티 벤더 이커머스 마켓플레이스 (Web + API + Mobile) | 개발 중 |

---

## 01. FirstWing — 프로토타입

> 모노레포 환경 구축 및 Next.js 초기 개념 검증(PoC)

| App | 설명 | 기술 스택 |
|-----|------|-----------|
| [**FirstWing**](./apps/01-FirstWing) | 프로토타입 웹앱 | Next.js 14, React 18, TailwindCSS, ApexCharts |

<p align="center">
  <img src="./public/img/firstwing.png" alt="FirstWing" width="200">
</p>

Turborepo + pnpm 워크스페이스 기반 모노레포의 첫 번째 앱으로, TailAdmin 템플릿을 활용한 대시보드 프로토타입입니다.

---

## 02. DevPulse — AI 기술 뉴스 플랫폼

> n8n + Gemini AI로 RSS 뉴스를 자동 수집/요약하여 모바일에서 제공하는 플랫폼

<p align="center">
  <img src="./public/img/devpulse.png" alt="DevPulse App" width="50%">
  <br>
  <em>DevPulse 모바일 화면</em>
</p>

| App | 설명 | 기술 스택 |
|-----|------|-----------|
| [**SecondWing**](./apps/02-01-SecondWing) | 프론트엔드 (PWA) | Next.js 16, Tailwind, Shadcn UI, Apollo Client, GraphQL |
| [**SecondWind**](./apps/02-02-SecondWind) | 백엔드 API | NestJS 11, GraphQL (Apollo), Prisma, PostgreSQL |
| [**SecondWave**](./apps/02-03-SecondWave) | 모바일 하이브리드 앱 | Expo 54, React Native, WebView Bridge |

**핵심 기능**:
- n8n 워크플로우: RSS 수집 → 중복 필터 → 본문 추출 → Gemini AI 3줄 요약 → DB 저장
- Mobile-First PWA + 무한 스크롤 뉴스 피드
- Redis 캐싱으로 API 응답 최적화
- Expo + WebView 하이브리드 앱 (Play Store 배포 완료)
- Web↔Native Bridge 양방향 통신 (햅틱, 푸시 알림)

<p align="center">
  <img src="./public/img/devpulsen8n.png" alt="n8n Workflow" width="100%">
  <br>
  <em>n8n 자동화 파이프라인</em>
</p>

---

## 03. ThirdWing — 판금 업체 MVP

> 레이저 판금 업체 PM으로서 레거시 대신 빠르게 구현한 생산관리 MVP

| App | 설명 | 기술 스택 |
|-----|------|-----------|
| [**ThirdWing**](./apps/03-01-ThirdWing) | 프론트엔드 | Next.js 14, Radix UI, React Query, Axios, Lucide |
| [**ThirdWind**](./apps/03-02-ThirdWind) | 백엔드 API | NestJS 11, GraphQL (Apollo), Prisma, PostgreSQL |

레이저 판금 업체에서 PM 역할을 수행하며, 레거시 소스 대신 Radix UI + React Query 조합으로 빠르게 MVP를 구현한 프로젝트입니다.

---

## 04. ForthWing — 멀티 벤더 이커머스

> 멀티 벤더 마켓플레이스 + 생산 관리 통합 엔터프라이즈 플랫폼

| App | 설명 | 기술 스택 |
|-----|------|-----------|
| [**ForthWing**](./apps/04-01-ForthWing) | 프론트엔드 (이커머스 웹) | Next.js 16, TailwindCSS, NextAuth, React Query, Zustand |
| [**ForthWind**](./apps/04-02-ForthWind) | 백엔드 API | NestJS 11, Prisma, PostgreSQL, JWT, MinIO, AWS SES |
| [**ForthWave**](./apps/04-03-ForthWave) | 모바일 앱 (예정) | Expo 54, React Native |

### 공개 페이지 (비회원)

<p align="center">
  <img src="./public/img/forthwing/00.비회원 메인화면.png" alt="도요몰 랜딩" width="80%">
  <br>
  <em>도요몰 랜딩 — 인기 상품 캐러셀 + 카테고리 바로가기 + 신상품 인피니티 스크롤</em>
</p>

<p align="center">
  <img src="./public/img/forthwing/01.비회원 메인에서 권한메뉴접근시.png" alt="로그인 프롬프트" width="80%">
  <br>
  <em>비회원이 보호 메뉴 접근 시 로그인 오버레이 (이메일 + Google OAuth)</em>
</p>

### 인증 시스템

<p align="center">
  <img src="./public/img/forthwing/02.일반로그인화면.png" alt="로그인" width="45%">
  <img src="./public/img/forthwing/03.일반회원가입.png" alt="회원가입" width="45%">
  <br>
  <em>로그인 / 일반 회원가입</em>
</p>

### 벤더(사업자) 승인 가입 플로우

<p align="center">
  <img src="./public/img/forthwing/04-1.사업자회원가입요청.png" alt="사업자 가입 신청" width="45%">
  <img src="./public/img/forthwing/04-2.사업자회원가입요청 확인.png" alt="사업자 가입 접수" width="45%">
  <br>
  <em>사업자 가입 신청 → 접수 확인</em>
</p>

<p align="center">
  <img src="./public/img/forthwing/05-0.AWS ses 이메일.png" alt="AWS SES 이메일" width="60%">
  <br>
  <em>관리자 승인 후 AWS SES로 가입 링크 이메일 발송</em>
</p>

### 관리자 패널

<p align="center">
  <img src="./public/img/forthwing/05-1.관리자 신청관리메뉴.png" alt="관리자 벤더 신청 관리" width="80%">
  <br>
  <em>사업자 가입 신청 관리 — 승인/거절/기한연장/재송신</em>
</p>

<p align="center">
  <img src="./public/img/forthwing/06.관리자 카테고리.png" alt="카테고리 관리" width="80%">
  <br>
  <em>카테고리 관리 — 대분류/소분류 트리 구조 CRUD</em>
</p>

<p align="center">
  <img src="./public/img/forthwing/08.관리자 메뉴권한관리.png" alt="메뉴 권한 관리" width="80%">
  <br>
  <em>역할별 메뉴 권한 관리 (관리자/판매자/고객)</em>
</p>

### 벤더(판매자) 상품 관리

<p align="center">
  <img src="./public/img/forthwing/09.기업 상품등록.png" alt="상품 등록" width="45%">
  <img src="./public/img/forthwing/11.기업 상품수정.png" alt="상품 수정" width="45%">
  <br>
  <em>상품 등록 / 수정 — 카테고리 선택, 할인 설정, MinIO 이미지 업로드</em>
</p>

<p align="center">
  <img src="./public/img/forthwing/10.기업 내상품.png" alt="내 상품 목록" width="80%">
  <br>
  <em>내 상품 목록 — 상태 필터 (판매중/비활성/품절/단종) + 검색</em>
</p>

**구현 현황**:

| Phase | 기능 | 상태 |
|-------|------|------|
| Phase 1 | 인증 (NextAuth JWT), 벤더 승인 가입 (AWS SES), 동적 메뉴 시스템 | 완료 |
| Phase 2 | 카테고리 관리, 상품 CRUD, MinIO 이미지 업로드, 공개 페이지 (랜딩/목록/상세) | 완료 |
| Phase 3 | 장바구니, 주문, 결제 (아임포트) | 예정 |
| Phase 4 | 쿠폰, 포인트 시스템 | 예정 |
| Phase 5+ | 리뷰/문의, FCM 알림, 정산, 생산 관리 | 예정 |

---

## Shared Packages

| 패키지 | 설명 |
|--------|------|
| [**@repo/eslint-config**](./packages/eslint-config) | 공유 ESLint 설정 (base, next-js, react-internal) |
| [**@repo/typescript-config**](./packages/typescript-config) | 공유 TypeScript 기본 설정 |
| [**@repo/ui**](./packages/ui) | 공유 React UI 컴포넌트 라이브러리 |

---

## Infrastructure

### Home Lab Server (MiniPC)

| 항목 | 사양 |
|------|------|
| CPU | AMD Ryzen 5 6600H (6C/12T, 3.3~4.5GHz) |
| RAM | 24GB DDR5 4800 |
| SSD | 512GB NVMe PCIe 4.0 |
| OS | Ubuntu 24.04 + K3s |
| 원격 접속 | RustDesk |

### K3s 서비스 현황

| 서비스 | 서브도메인 | 설명 |
|--------|-----------|------|
| FirstWing | `firstwing.doyosae.com` | 프로토타입 (Next.js) |
| DevPulse Web | `devpulse.doyosae.com` | 뉴스 웹앱 (Next.js PWA) |
| DevPulse API | `api-devpulse.doyosae.com` | 뉴스 API (NestJS GraphQL) |
| MinIO S3 | `s3.doyosae.com` | 오브젝트 스토리지 |
| MinIO Console | `s3-admin.doyosae.com` | 스토리지 관리 UI |
| n8n | `n8n.doyosae.com` | 자동화 워크플로우 |
| Portainer | `portainer.doyosae.com` | 컨테이너 관리 |
| PostgreSQL | — (내부) | 메인 데이터베이스 |
| Redis | — (내부) | 캐시 / 큐 |
| MongoDB | — (내부) | 문서 DB |
| DrawDB | `drawdb.doyosae.com` | DB 스키마 설계 도구 |
| Draw.io | `drawio.doyosae.com` | 다이어그램 도구 |

**네트워크**: Cloudflare Tunnel (포트포워딩 없이 HTTPS 외부 접속)
**도메인**: `doyosae.com` (가비아 구매 → Cloudflare 이관)
**CI/CD**: GitHub Actions + Self-hosted Runner + GHCR

---

## Monorepo Structure

```
DoyoWorld/
├── apps/
│   ├── 01-FirstWing/          # 프로토타입 (Next.js 14)
│   ├── 02-01-SecondWing/      # DevPulse Web (Next.js 16 + GraphQL)
│   ├── 02-02-SecondWind/      # DevPulse API (NestJS + GraphQL)
│   ├── 02-03-SecondWave/      # DevPulse Mobile (Expo + WebView)
│   ├── 03-01-ThirdWing/       # 대시보드 실험 (Next.js 14 + Radix UI)
│   ├── 03-02-ThirdWind/       # 대시보드 API (NestJS + GraphQL)
│   ├── 04-01-ForthWing/       # 이커머스 Web (Next.js 16 + TailAdmin)
│   ├── 04-02-ForthWind/       # 이커머스 API (NestJS + REST + Prisma)
│   └── 04-03-ForthWave/       # 이커머스 Mobile (Expo)
├── packages/
│   ├── eslint-config/         # 공유 ESLint 설정
│   ├── typescript-config/     # 공유 TypeScript 설정
│   └── ui/                    # 공유 UI 컴포넌트 라이브러리
├── turbo.json                 # Turborepo 빌드 파이프라인
└── pnpm-workspace.yaml        # pnpm 워크스페이스 정의
```

---

## Getting Started

```bash
# 의존성 설치
pnpm install

# 개별 앱 개발 서버
pnpm --filter first-wing dev     # 01 FirstWing
pnpm --filter second-wing dev    # 02 DevPulse Web
pnpm --filter second-wind dev    # 02 DevPulse API
pnpm --filter third-wing dev     # 03 ThirdWing
pnpm --filter forth-wing dev     # 04 ForthWing (이커머스)
pnpm --filter forth-wind dev     # 04 ForthWind (이커머스 API)

# 전체 빌드
pnpm build
```

---

## Tech Stack

| 영역 | 기술 |
|------|------|
| Frontend | Next.js 14~16, React 18~19, TailwindCSS, Shadcn UI, Radix UI |
| State | Zustand, React Query (TanStack), Apollo Client |
| Backend | NestJS 11, GraphQL (Apollo Server), REST, Prisma 5 |
| Auth | NextAuth v5, JWT, Passport.js, AWS SES |
| Database | PostgreSQL 16, Redis 7, MongoDB |
| Storage | MinIO (S3 호환, Self-hosted) |
| Mobile | Expo 54, React Native, WebView Bridge |
| Infra | K3s, Docker, Cloudflare Tunnel, GitHub Actions |
| AI/자동화 | Gemini AI, n8n 워크플로우 |
| CI/CD | GitHub Actions, Self-hosted Runner, GHCR |
| Dev Tools | Turborepo, pnpm 9, RustDesk |
