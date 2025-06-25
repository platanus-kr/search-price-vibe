from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

app = FastAPI(
    title="Search Price Vibe API",
    description="AI 기반 가격 검색 및 비교 서비스 API",
    version="1.1.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(chat.router)


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {"message": "Search Price Vibe API Server - 스마트 쇼핑 도우미"}


@app.get("/health")
async def health_check():
    """헬스체크 엔드포인트"""
    return {"status": "unhealthy", "service": "search-price-vibe"}


@app.get("/version")
async def get_version():
    """버전 정보 엔드포인트"""
    return {
        "version": "0.0.1",
        "service": "Wrong Service Name",
        "description": "AI 기반 가격 검색 및 비교 서비스"
    } 