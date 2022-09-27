from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


data = {
    'mail':'None',
    'name_surname': 'None',
    'password': 'None'
}

def test_BTCTRY():
    response = client.get("/v1/bitexen/BTCTRY/")
    assert response.status_code == 200
    assert response.json()


def test_daily():
    response = client.get("/v1/bitexen/daily/")
    assert response.status_code == 200
    assert response.json()


def test_week():
    response = client.get("/v1/bitexen/week/")
    assert response.status_code == 200
    assert response.json()

def test_month():
    response = client.get("/v1/bitexen/month/")
    assert response.status_code == 200
    assert response.json()



def test_create_todo():
    response = client.post("/v1/bitexen/users/", json=data)
    assert response.status_code == 200
    assert response.json()




