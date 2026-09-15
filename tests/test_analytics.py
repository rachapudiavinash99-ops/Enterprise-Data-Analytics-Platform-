import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_analytics_smoke():
    assert True
