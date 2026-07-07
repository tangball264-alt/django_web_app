# django_web_app

Django 프레임워크 학습 및 안정적인 백엔드 아키텍처 설계를 위한 포스트 관리 및 소개 웹 애플리케이션 토이 프로젝트입니다.
본 프로젝트는 **테스트 주도 개발(TDD)** 방법론을 엄격히 적용하여 작성되었으며, 지속적인 리팩토링과 모듈화를 통해 유지보수성을 극대화하는 방향으로 개발되었습니다.

개발 환경에서는 가볍고 독립적인 `SQLite3`를 활용하였으며, 운영 배포 환경에서는 대용량 데이터 처리에 적합한 `PostgreSQL`로 이전하여 데이터베이스 설계를 안정화했습니다.

---

## 🛠 기술 스택

### Backend

* **Framework:** Python, Django 5.2.5
* **WSGI Server:** Gunicorn 26.0.0
* **Database:** SQLite3 (Local Development) ➡️ PostgreSQL 2.9.12 (Production)
* **Authentication:** Django Auth, `django-allauth` (Google OAuth 2.0 연동)

### Frontend

* **Design:** Bootstrap 5 (`crispy-bootstrap5` 기반 폼 레이아웃 구성)
* **Icons & Fonts:** FontAwesome

### Tools & Libraries

* **Testing:** BeautifulSoup4 (크롤링 기반 웹 UI/UX 및 네비게이션 자동화 테스트)
* **Content & Media:** `django-markdownx` (마크다운 포스팅 지원), Pillow 11.3.0 (이미지 처리 라이브러리)

---

## 🌟 주요 기능

### 1. 블로그 및 포스트 관리 (CBV & FBV 혼용 아키텍처)

* **포스트 리스트 및 페이징:** 클래스 기반 뷰(CBV) 패턴을 활용한 목록 조회, 최신순 정렬 및 페이지네이션 기능 구현(`paginate_by = 5`).
* **동적 태그 파싱 시스템:** 포스트 작성/수정 시 입력된 문자열 스트링을 파싱하여 다대다(`ManyToManyField`) 관계의 태그 객체를 자동 생성 및 매핑(`slugify` 활용).
* **복합 검색 알고리즘:** 장고의 `Q` 객체를 활용하여 포스트의 제목과 태그를 유기적으로 관통하는 중복 없는 통합 검색 기능 구현(`PostSearch`).
* **분류 체계:** 슬러그(Slug) 필드를 활용한 RESTful 구조의 카테고리별/태그별 포스트 필터링 페이지를 함수형 뷰(FBV)로 직관적으로 구현.
* **마크다운 지원:** `django-markdownx` 라이브러리를 통해 마크다운 텍스트 편집 및 렌더링 환경 구축.

### 2. 소개 및 랜딩 페이지 (`single_pages` 앱)

* **최신 포스트 동적 연동:** 대문 페이지(`landing`) 방문 시 블로그 앱의 상위 3개 최신 포스트(`[:3]`)를 메인 화면에 컴포넌트 형태로 실시간 배치.
* **프로필 레이아웃:** 자기소개 및 포트폴리오 구성을 위한 정적 프로필 페이지 구성(`about_me`).

### 3. 댓글(Comment) 시스템 및 미디어 관리

* **댓글 CRUD 제어:** 포스트 상세 페이지 내 댓글 작성 폼 렌더링 및 소유권 검증 기반의 수정/삭제 기능 안전하게 구현.
* **파일 업로드 및 다운로드:** Pillow 라이브러리를 활용한 헤더 이미지 처리 및 첨부파일 업로드/웹 표준 다운로드 환경 구축.

### 4. 사용자 인증 및 보안 권한 통제

* **역할 기반 접근 제어:** `LoginRequiredMixin`, `UserPassesTestMixin`, `dispatch()` 커스텀 오버라이딩을 활용하여 비로그인 유저 및 일반 유저의 무단 접근 제한(Staff/Superuser 권한 확인 및 `PermissionDenied` 처리).
* **구글 소셜 로그인 인터페이스:** `django-allauth` 패키지를 도입하고 구글 클라우드 콘솔 API 승인 도메인 및 리다이렉트 URI 설정을 연동하여 소셜 인증 인프라 구현.

### 5. TDD 기반 품질 검증

* 장고 내장 `TestCase`와 `BeautifulSoup4` 크롤러를 통합 설계하여 네비게이션 동작, 권한별 UI 가시성 및 폼 유효성 자동 검증 완료.

---

## 📂 프로젝트 아키텍처 및 폴더 구조

```text
django_web_app (Root)
├── .data/                 # PostgreSQL 데이터 영속성 저장 볼륨 폴더
├── .staticfiles/          # collectstatic 명령어로 수집된 운영 환경용 정적 파일 폴더
├── blog/                  # 메인 블로그/포스트 관리 앱
│   ├── migrations/        # DB 마이그레이션 이력 관리 폴더
│   ├── static/            # 앱 전용 정적 파일 (blog-style.css 등)
│   ├── templates/         # HTML 템플릿 폴더 (base.html 확장 구조)
│   ├── admin.py           # Post, Category, Tag, Comment 어드민 등록
│   ├── models.py          # 주요 데이터 모델 정의
│   ├── tests.py           # TDD 기반 자동화 테스트 코드
│   ├── urls.py            # 앱 라우팅 설정
│   └── views.py           # CBV 및 FBV 기반 비드니스 로직 구현부
├── django_web_app/        # 프로젝트 최상위 설정 폴더
│   ├── settings.py        # 가상환경/환경변수 동적 분리 설정
│   └── urls.py            # 메인 URL 라우팅 및 미디어/마크다운 경로 지정
├── nginx/                 # Nginx 웹 서버 구성 폴더
│   └── nginx.conf         # 프록시 및 static/media 라우팅 설정 파일
├── single_pages/          # Landing 및 About Me 정적 페이지 앱
│   ├── static/            # single_pages 전용 정적 파일
│   ├── templates/         # landing.html 및 about_me.html 템플릿 폴더
│   ├── urls.py            # single_pages 라우팅 설정
│   └── views.py           # 최신글 연동 및 정적 페이지 렌더링 뷰
├── docker-compose.yml     # 멀티 컨테이너 오케스트레이션 설정 파일
├── Dockerfile             # Django 웹 애플리케이션 컨테이너 빌드 파일
├── init-letsencrypt.sh    # Let's Encrypt SSL 인증서 자동 발급 스크립트
├── manage.py              # Django 명령행 유틸리티
└── requirements.txt       # 의존성 패키지 목록 파일

```

---

## 💻 로컬 개발 환경 설치 및 실행 방법

### 1. 저장소 복사 및 가상환경 설정

```bash
# 레포지토리 클론 (SSH 키 이용)
git clone git@github.com:사용자계정/django_web_app.git
cd django_web_app

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Mac/Linux 환경
# venv\Scripts\activate   # Windows 환경

```

### 2. 의존성 패키지 설치

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

### 3. 데이터베이스 초기화 및 관리자 계정 생성

로컬 개발 환경에서는 기본 환경 변수 값이 활성화되어 `SQLite3` 데이터베이스가 자동으로 구동됩니다.

```bash
python manage.py migrate
python manage.py createsuperuser

```

### 4. 로컬 서버 실행

```bash
python manage.py runserver

```

브라우저를 열고 `http://127.0.0.1:8000/` 경로에서 서비스를 확인할 수 있습니다.

---

## 🚀 운영 서버 배포 환경 설정 (Production Deployment)

본 프로젝트는 운영 배포 단계에서 인프라의 안정성, 보안 및 데이터 격리를 위하여 **AWS Lightsail 가상 서버** 내에 **Docker 컨테이너 기반 인프라**를 통합 운용합니다.

### 1. 환경 변수 기반 데이터베이스 분리 (`settings.py`)

배포 환경에서는 주입되는 환경 변수(`SQL_ENGINE` 등)에 맞춰 대용량 데이터 적재에 유리한 `PostgreSQL` 데이터베이스 엔진으로 자동 연결되도록 인프라 파이프라인이 안전하게 구성되어 있습니다.

### 2. 멀티 컨테이너 구조

Docker Compose 아케스트레이션에 의해 총 3개의 격리된 컨테이너가 가상 네트워크로 통신합니다.

* **Web 컨테이너:** Django (Gunicorn WSGI 서버 탑재)
* **DB 컨테이너:** PostgreSQL (데이터 볼륨 영속성 적용)
* **Nginx 컨테이너:** Reverse Proxy 서버 (HTTPS 보안 프록시 제어, 외부 정적/미디어 루트 라우팅 및 Certbot SSL 인증서 발급 연동)

### 3. 운영 환경 배포 구동 명령어

AWS Lightsail 방화벽 인바운드 규칙에서 **80(HTTP)** 및 **443(HTTPS)** 포트가 개방되어 있는지 확인한 뒤 서버 인스턴스 터미널에서 다음 명령을 실행합니다.

```bash
# 1. 원격 저장소로부터 배포 빌드 소스 pull
git pull origin main

# 2. Nginx 컨테이너 이미지 독립 빌드
sudo docker compose build nginx

# 3. 자동화 SSL 인증서 발급 및 갱신 스크립트 실행
sudo ./init-letsencrypt.sh

# 4. 프로덕션 멀티 컨테이너 서비스 백그라운드 빌드 및 전체 실행
sudo docker compose up -d --build

```