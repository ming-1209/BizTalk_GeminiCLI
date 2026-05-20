# Project: 업무 말투 변환기 (Biztone Converter)

이 프로젝트는 사용자가 입력한 평상시 말투를 선택한 대상(상사, 동료, 고객 등)에 적합한 비즈니스 말투로 변환해주는 웹 서비스입니다. 바이브 코딩(Vibe Coding) 실습을 위한 One Day 프로젝트로 설계되었습니다.

## 🚀 프로젝트 개요
- **목적**: 비즈니스 커뮤니케이션의 어려움을 AI(Upstage Solar-Pro2)를 통해 해결
- **핵심 기술**:
    - **Backend**: Python 3.11+, FastAPI, LangChain
    - **Frontend**: HTML5, CSS3, JavaScript (Vanilla JS)
    - **AI Model**: Upstage Solar-Pro2 (`langchain-upstage` 활용)
    - **Deployment**: Vercel

## 🛠 빌드 및 실행 가이드

### 1. 환경 준비
- Python 3.11 이상 설치 필요
- Upstage API Key 발급 필요

### 2. 백엔드 실행 (Local)
```bash
# 가상환경 생성 및 활성화 (권장)
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 패키지 설치
pip install -r requirements.txt

# 환경 변수 설정 (.env 파일 생성)
echo "UPSTAGE_API_KEY=your_api_key_here" > .env

# 서버 실행
uvicorn main:app --reload --port 8000
```

### 3. 프론트엔드 실행
- `frontend/index.html` 파일을 브라우저로 직접 열거나, Live Server 등을 활용하여 실행합니다.
- 백엔드 API 주소(`API_BASE`)가 로컬 환경(`http://localhost:8000`)으로 설정되어 있는지 확인하십시오.

## 📏 개발 규칙 및 컨벤션

### 1. 바이브 코딩 3원칙 (PRD 명시)
- **원칙 1. 완료 기준 선정의**: 작업 시작 전 체크리스트를 통해 목표 기능을 명확히 합니다.
- **원칙 2. 조사 먼저, 구현 나중**: 외부 API 연동이나 새로운 기술 도입 시 방법을 먼저 파악한 후 코드를 작성합니다.
- **원칙 3. 버그 분석 먼저, 수정 나중**: 에러 발생 시 원인 분석을 선행하고 근본적인 해결책을 적용합니다.

### 2. 보안 지침 (my-rules.md 준수)
- **민감 정보 보호**: `.env` 파일은 절대 Git에 커밋하지 않습니다. (이미 `.gitignore`에 등록됨)
- **위험 작업 금지**: `git push --force`, `git reset --hard` 등 히스토리를 파괴하는 작업은 엄격히 금지합니다.
- **한국어 응답**: 모든 대화와 문서 작성은 한국어를 기본으로 합니다.

### 3. 디렉토리 구조
- `backend/`: FastAPI 기반 서버 로직 (routers, services, prompts, models)
- `frontend/`: 웹 UI (HTML, CSS, JS)

## 📌 주요 파일 설명
- `PRD_업무말투변환기.md`: 제품 요구사항 및 기술 명세서
- `개요서_업무말투변환기.md`: 프로젝트 목적 및 기능 요약
- `my-rules.md`: AI 어시스턴트의 행동 강령 및 작업 제한 사항

## 🔜 구현 체크리스트 (TODO)
- [ ] FastAPI 서버 및 Health Check 구현
- [ ] LangChain을 이용한 Solar-Pro2 연동 (대상별 프롬프트 적용)
- [ ] 정적 파일 라우팅 설정
- [ ] 프론트엔드 UI 및 API 연동 (Fetch API)
- [ ] Vercel 통합 배포 설정

### Source Code가 변경되거나 라이브러리 버전이 변경되면 반드시 @PRD_업무말투변환기.md 문서도 반드시 같이 업데이트 합니다. 
* 구현이 완료된 사항들은 `2. 완료 체크리스트`에 모두 체크표시를 해서 완료되었음을 표시하세요.
* `8. 단계별 구현 순서` 의 STEP1 ~ STRP4 에 완료가 되면 체크표시를 해서 완료되었음을 표시하세요.
* 라이브러리 버전이 변경되면 `@PRD_업무말투변환기.md` 문서, `GEMINI.md` 문서도 업데이트 하세요.
  