import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """헬스체크 엔드포인트 테스트"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "search-price-vibe"}


def test_read_root():
    """루트 엔드포인트 테스트"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_version_endpoint():
    """버전 엔드포인트 테스트"""
    response = client.get("/version")
    assert response.status_code == 200
    json_response = response.json()
    assert "version" in json_response
    assert "service" in json_response
    assert "description" in json_response
    assert json_response["version"] == "1.1.0"
    assert json_response["service"] == "Search Price Vibe API" 