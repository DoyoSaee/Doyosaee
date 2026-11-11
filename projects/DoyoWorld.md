# DoyoWorld Monorepo

풀사이클 엔지니어링을 지향하는 모노레포입니다. 홈랩 인프라(K3s) 구축부터 웹/모바일 앱 배포까지, 서비스의 전체 라이프사이클을 다루고 있습니다.

**빌드**: Turborepo | **패키지 매니저**: pnpm 9 | **Node**: >= 18

**네이밍**: `세대번호-역할` — **Wing** = 프론트엔드, **Wind** = 백엔드 API, **Wave** = 모바일. 06세대는 역할명(GpuStation / FocusVision)을 그대로 씀. 06-03은 pnpm 워크스페이스 밖의 Python(uv) 앱.

---

## Projects Overview

| # | 프로젝트 | 설명 | 상태 |
|---|----------|------|------|
| 01 | [**FirstWing**](#01-firstwing--프로토타입) | 모노레포 구축 및 초기 PoC | 완료 |
| 02 | [**DevPulse**](#02-devpulse--ai-기술-뉴스-플랫폼) | AI 기반 기술 뉴스 요약 플랫폼 (Web + API + Mobile) | 운영 중 |
| 03 | [**ThirdWing**](#03-thirdwing--판금-업체-mvp) | 레이저 판금 업체 생산관리 MVP (Web + API) | 실험 |
| 04 | [**ForthWing**](#04-forthwing--멀티-벤더-이커머스) | 멀티 벤더 이커머스 마켓플레이스 (Web + API + Mobile) | 개발 중 |
| 05 | [**FifthWing**](#05-fifthwing--웹-3d-인테리어-룸플래너-둥지) | 웹 3D 인테리어 룸플래너 "둥지" (Web + API) | 운영 중 |
| 06 | [**GpuStation · 집중 트래커**](#06-gpustation--집중-트래커) | 원격 GPU PC 제어·모니터링 대시보드 + ESP32-CAM·로컬 VLM 집중 모니터 (Web + API + Python) | 운영 중 |

---

## 01. FirstWing — 프로토타입

> 모노레포 환경 구축 및 Next.js 초기 개념 검증(PoC)

| App | 설명 | 기술 스택 |
|-----|------|-----------|
| [**FirstWing**](./apps/01-FirstWing) | 프로토타입 웹앱 | Next.js 14, React 18, TailwindCSS, ApexCharts |

<p align="center">
  <img src="projects/images/DoyoWorld/firstwing.png" alt="FirstWing" width="200">
</p>

Turborepo + pnpm 워크스페이스 기반 모노레포의 첫 번째 앱으로, TailAdmin 템플릿을 활용한 대시보드 프로토타입입니다.

---

## 02. DevPulse — AI 기술 뉴스 플랫폼

> n8n + Gemini AI로 RSS 뉴스를 자동 수집/요약하여 모바일에서 제공하는 플랫폼

<p align="center">
  <img src="projects/images/DoyoWorld/devpulse.png" alt="DevPulse App" width="50%">
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
- Expo + WebView 하이브리드 앱 (Play Store 배포 완료)
- Web↔Native Bridge 양방향 통신 (햅틱, 푸시 알림)

<p align="center">
  <img src="projects/images/DoyoWorld/devpulsen8n.png" alt="n8n Workflow" width="100%">
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
  <img src="projects/images/DoyoWorld/forthwing/00.비회원 메인화면.png" alt="도요몰 랜딩" width="80%">
  <br>
  <em>도요몰 랜딩 — 인기 상품 캐러셀 + 카테고리 바로가기 + 신상품 인피니티 스크롤</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/01.비회원 메인에서 권한메뉴접근시.png" alt="로그인 프롬프트" width="80%">
  <br>
  <em>비회원이 보호 메뉴 접근 시 로그인 오버레이 (이메일 + Google OAuth)</em>
</p>

### 인증 시스템

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/02.일반로그인화면.png" alt="로그인" width="45%">
  <img src="projects/images/DoyoWorld/forthwing/03.일반회원가입.png" alt="회원가입" width="45%">
  <br>
  <em>로그인 / 일반 회원가입</em>
</p>

### 벤더(사업자) 승인 가입 플로우

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/04-1.사업자회원가입요청.png" alt="사업자 가입 신청" width="45%">
  <img src="projects/images/DoyoWorld/forthwing/04-2.사업자회원가입요청 확인.png" alt="사업자 가입 접수" width="45%">
  <br>
  <em>사업자 가입 신청 → 접수 확인</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/05-0.AWS ses 이메일.png" alt="AWS SES 이메일" width="60%">
  <br>
  <em>관리자 승인 후 AWS SES로 가입 링크 이메일 발송</em>
</p>

### 관리자 패널

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/05-1.관리자 신청관리메뉴.png" alt="관리자 벤더 신청 관리" width="80%">
  <br>
  <em>사업자 가입 신청 관리 — 승인/거절/기한연장/재송신</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/06.관리자 카테고리.png" alt="카테고리 관리" width="80%">
  <br>
  <em>카테고리 관리 — 대분류/소분류 트리 구조 CRUD</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/08.관리자 메뉴권한관리.png" alt="메뉴 권한 관리" width="80%">
  <br>
  <em>역할별 메뉴 권한 관리 (관리자/판매자/고객)</em>
</p>

### 벤더(판매자) 상품 관리

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/09.기업 상품등록.png" alt="상품 등록" width="45%">
  <img src="projects/images/DoyoWorld/forthwing/11.기업 상품수정.png" alt="상품 수정" width="45%">
  <br>
  <em>상품 등록 / 수정 — 카테고리 선택, 할인 설정, MinIO 이미지 업로드</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/forthwing/10.기업 내상품.png" alt="내 상품 목록" width="80%">
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

## 05. FifthWing — 웹 3D 인테리어 룸플래너 (둥지)

> 브라우저에서 방을 직접 그려 3D 집으로 세우고 가구를 배치하는 룸플래너 · 🔗 [dungji.doyosae.com](https://dungji.doyosae.com)

| App | 설명 | 기술 스택 |
|-----|------|-----------|
| [**FifthWing**](./apps/05-01-FifthWing) | 프론트엔드 (3D 룸플래너) | Next.js, React 19, React Three Fiber, drei, three.js, Zustand |
| [**FifthWind**](./apps/05-02-FifthWind) | 백엔드 API (방 저장/공유·모델 재호스팅) | NestJS, code-first GraphQL, Prisma, PostgreSQL, MinIO |

<p align="center">
  <img src="projects/images/DoyoWorld/fifthwing/dungji1.png" alt="둥지 랜딩" width="80%">
  <br>
  <em>둥지 — 방을 3D로 꾸미는 룸플래너 랜딩</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/fifthwing/dungji2.png" alt="방 조립 에디터" width="80%">
  <br>
  <em>방 조립 에디터 — 사각형 방 + 자유 선을 혼용해 하나의 집으로 결합(면적·높이 실시간)</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/fifthwing/dungji3.png" alt="가구 찾기(Poly Pizza 공유 카탈로그)" width="45%">
  <img src="projects/images/DoyoWorld/fifthwing/dungji4.png" alt="탑다운 배치 뷰" width="45%">
  <br>
  <em>가구 찾기(Poly Pizza 공유 카탈로그) / 탑다운 배치 뷰</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/fifthwing/dungji5.png" alt="방 내부 3D 편집" width="45%">
  <img src="projects/images/DoyoWorld/fifthwing/dungji6.png" alt="저장된 방 갤러리" width="45%">
  <br>
  <em>방 내부 3D 편집 / 저장된 방 갤러리</em>
</p>

**핵심 기능 / 기술 하이라이트** — 상세: [케이스 스터디](./docs/dungji-case-study.md)
- **방 조립 에디터** — 사각형 방과 자유 선을 **혼용**해 하나의 집으로 결합(polygon-clipping 정확 합집합, 대각선 보존). 평면도에서 선 그어 **벽/칸막이** 세우기 + 벽·바닥 **재질(색)**.
- **폴리곤 방 클램프 알고리즘**(`clampFootprint`, 직접 구현) — 선분 거리 + 폴리곤 와인딩 기반 안쪽 법선 OBB 클램프로 **오목 방에서도** 가구가 벽을 안 뚫고 딱 붙음.
- **공유 glTF 카탈로그** — Poly Pizza 검색을 백엔드로 프록시(키 은닉)하고, 담은 모델의 glb·썸네일을 자체 **MinIO에 재호스팅 + DB 등록** → 모든 사용자가 공유, 외부 API 사용 최소화.
- **3D 상호작용** — 이벤트 레이 배치·드래그, 비례 리사이즈·자유 배치·고도(공중/매립), drei `<Html>` 플로팅 인스펙터, **모바일 터치(포인터 이벤트)** 지원.
- **로그인리스 소유권** — editToken(sha256 해시·timing-safe)으로 회원가입 없이 저장 + 공유 링크(`/s/slug`, 편집/읽기전용 분기). 핵심 로직 TDD.
- **풀스택·셀프호스팅** — NestJS code-first GraphQL + Prisma + PostgreSQL + MinIO, 홈랩 k3s + Cloudflare 터널 + GitHub Actions CI/CD.

---

## 06. GpuStation · 집중 트래커

> 원격지 GPU PC(RTX 3060)를 전원(ESP32 릴레이·MQTT)부터 서비스·지표까지 한 화면에서 다루는 대시보드, 그 위에 올린 **ESP32-CAM + 로컬 비전 모델(Ollama Qwen2.5-VL 3B)** 집중 모니터. 대시보드 `gpu.doyosae.com`(Cloudflare Access 뒤) · 상세: [케이스 스터디](./docs/focus-tracker-case-study.md) · [측정 기록](./docs/focus-tracker-eval.md)

| App | 설명 | 기술 스택 |
|-----|------|-----------|
| [**GpuStationFrontend**](./apps/06-01-GpuStationFrontend) | 대시보드 (상태·전원·종료 예약·24h 지표·집중 시계판·카메라 관리) | Next.js, React, SVG/Canvas |
| [**GpuStationBackend**](./apps/06-02-GpuStationBackend) | 중계 API (MQTT ↔ 익산 에이전트·Tasmota 릴레이, 06-03 프록시) | NestJS, MQTT(Mosquitto), WebSocket |
| [**FocusVisionBackend**](./apps/06-03-FocusVisionBackend) | 카메라 수신·추론 워커·저장 + ESP32-CAM 펌웨어 | Python(uv), LangGraph, Ollama, SQLite, Arduino C++ |

<p align="center">
  <img src="projects/images/DoyoWorld/focus/01-gpustation-main-metrics.png" alt="GpuStation 메인" width="45%">
  <img src="projects/images/DoyoWorld/focus/02-dial-log-open.png" alt="집중 시계판" width="45%">
  <br>
  <em>GpuStation 메인(상태·전원·종료 예약·최근 24시간 GPU 지표) / 집중 시계판(오전·오후, 지금 상태, 합계, 확인 기록)</em>
</p>

<p align="center">
  <img src="projects/images/DoyoWorld/focus/03-camera-page-live.png" alt="카메라 관리" width="45%">
  <img src="projects/images/DoyoWorld/focus/04-esp32-cam-hardware.jpg" alt="ESP32-CAM" width="45%">
  <br>
  <em>카메라 관리(1초 실화면·wifi 원격 등록·명령) / ESP32-CAM 실물</em>
</p>

**핵심 기능 / 기술 하이라이트**
- **측정으로 모델 결정** — 직접 라벨한 99장으로 클라우드(Claude Haiku)와 로컬(Qwen2.5-VL 3B/7B)·프롬프트 3종을 정밀도·재현율·지연·비용 한 표로 비교. 3B + 짧은 프롬프트가 로컬 중 최고(정밀도 1.0·재현율 0.86·2.2초/장·VRAM 4GB), 사진 반출 없음·비용 0을 이유로 로컬 선택.
- **운영 데이터로 찾은 결함과 보정** — 설명문엔 "폰 사용"이라 쓰면서 불리언은 false인 프레임 20% → 설명문 규칙으로 되살려 재현율 0.86 → 1.00(정밀도 0.97). 한 장에 끊기던 판정은 30초 공백 허용 세션 + 1프레임 스무딩으로.
- **1초 실화면 / 10초 추론 분리** — 카메라는 1초마다 keep-alive로 푸시(최신 프레임만 메모리), 서버는 10초에 한 장만 저장·추론. 하루 8,640장을 비용 0으로 판정.
- **전원만 꽂으면 되는 카메라** — 아는 wifi 없으면 캡티브 포털, 서버 응답에 명령을 실어 돌려주는 피기백으로 wifi 등록·재시작 원격 제어, 하드웨어/소프트웨어 워치독.
- **네트워크 경계** — 카메라 수신만 토큰 헤더로 공개, 로컬 LLM은 Cloudflare Tunnel + Access 서비스 토큰, 대시보드는 Access 로그인. 익산 PC는 SSH 대신 MQTT 에이전트로 제어(전원 OFF/ON·서비스 토글·N분 뒤 종료 예약/취소·GPU 지표 1분 단위 시계열).

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

### K3s 서비스 현황 (2026-11 기준)

| 서비스 | 서브도메인 | 설명 |
|--------|-----------|------|
| FirstWing | `firstwing.doyosae.com` | 프로토타입 (Next.js) |
| DevPulse Web / API | `devpulse.doyosae.com` / `api-devpulse.doyosae.com` | 뉴스 웹앱 (Next.js PWA) / GraphQL API |
| 둥지 Web / API | `dungji.doyosae.com` / `api-dungji.doyosae.com` | 웹 3D 룸플래너 / GraphQL API |
| 도요몰 Web / API | `mall.doyosae.com` / `api-mall.doyosae.com` | 멀티 벤더 이커머스 / REST API |
| GpuStation Web / API | `gpu.doyosae.com` / `api-gpu.doyosae.com` | 원격 GPU 대시보드 (Cloudflare Access) |
| 집중 트래커 수신 | `focus-ingest.doyosae.com` | ESP32-CAM 프레임 수신 (토큰 인증, 추론 워커 동거) |
| Mosquitto | `mqtt.doyosae.com` | MQTT 브로커 (TLS, 익산 ESP32·에이전트) |
| MinIO S3 / Console | `s3.doyosae.com` / `s3-admin.doyosae.com` | 오브젝트 스토리지 (둥지 모델·썸네일, 도요몰 이미지) |
| n8n | `n8n.doyosae.com` | 자동화 워크플로우 (DevPulse 수집) |
| PostgreSQL | — (내부) | 앱 공용 데이터베이스 |
| Portainer | — (내부) | 컨테이너 관리 |

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
│   ├── 04-03-ForthWave/       # 이커머스 Mobile (Expo)
│   ├── 05-01-FifthWing/       # 3D 룸플래너 "둥지" Web (Next.js + React Three Fiber)
│   ├── 05-02-FifthWind/       # 3D 룸플래너 API (NestJS + Prisma)
│   ├── 06-01-GpuStationFrontend/  # 원격 GPU 대시보드 + 집중 시계판 (Next.js)
│   ├── 06-02-GpuStationBackend/   # MQTT 중계 API + 익산 에이전트 (NestJS, Python)
│   └── 06-03-FocusVisionBackend/  # 카메라 수신·로컬 VLM 추론·저장 + ESP32-CAM 펌웨어 (Python uv)
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
pnpm --filter fifth-wing dev     # 05 FifthWing (둥지 3D 룸플래너)
pnpm --filter fifth-wind dev     # 05 FifthWind (둥지 API)
pnpm --filter gpustation-frontend dev  # 06 GpuStation 대시보드
pnpm --filter gpustation-backend dev   # 06 GpuStation API

# 06-03 FocusVisionBackend (Python, pnpm 밖)
cd apps/06-03-FocusVisionBackend && uv sync && uv run pytest

# 전체 빌드
pnpm build
```

---

## Tech Stack

| 영역 | 기술 |
|------|------|
| Frontend | Next.js 14~16, React 18~19, TailwindCSS, Shadcn UI, Radix UI |
| 3D | React Three Fiber, drei, three.js |
| State | Zustand, React Query (TanStack), Apollo Client |
| Backend | NestJS 11, GraphQL (Apollo Server), REST, Prisma 5 |
| Auth | NextAuth v5, JWT, Passport.js, AWS SES |
| Database | PostgreSQL 16, SQLite (집중 트래커 판정·GPU 지표) |
| Storage | MinIO (S3 호환, Self-hosted) |
| Mobile | Expo 54, React Native, WebView Bridge |
| Infra | K3s, Docker, Cloudflare Tunnel, GitHub Actions |
| AI/자동화 | Gemini AI, n8n 워크플로우, Ollama Qwen2.5-VL(로컬 VLM), LangGraph, Claude Haiku(eval 베이스라인) |
| IoT | ESP32-CAM(Arduino C++), ESP32 릴레이(Tasmota), MQTT(Mosquitto) |
| CI/CD | GitHub Actions, Self-hosted Runner, GHCR |
| Dev Tools | Turborepo, pnpm 9, RustDesk, Claude Code |
