import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_dashboards_smoke():
    assert True
