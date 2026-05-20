import os
from dotenv import load_dotenv

# 환경 변수를 모든 임포트보다 먼저 로드합니다.
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.routers import convert

app = FastAPI(title="업무 말투 변환기 API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 포함
app.include_router(convert.router, prefix="/api")

# 헬스 체크
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# 정적 파일 서빙 (프론트엔드)
static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

    @app.get("/")
    async def read_index():
        return FileResponse(os.path.join(static_path, "index.html"))
else:
    @app.get("/")
    async def read_root():
        return {"message": "Frontend directory not found. Please check your structure."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
