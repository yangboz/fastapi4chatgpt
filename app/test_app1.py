from app1 import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI #1"}
