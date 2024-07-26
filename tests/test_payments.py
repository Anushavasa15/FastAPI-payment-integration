import pytest
from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)


def test_create_payment_method():
    response = client.post("/payments/create", json={
        "number": "4242424242424242",
        "exp_month": 8,
        "exp_year": 2026,
        "cvc": "314"
    })
    assert response.status_code == 200
    data = response.json()
    import pdb;pdb.set_trace()
    assert "id" in data
    assert data["object"] == "payment_method"


def test_retrieve_payment_method():
   
    create_response = client.post("/payments/create", json={
        "number": "4242424242424242",
        "exp_month": 8,
        "exp_year": 2026,
        "cvc": "314"
    })
    payment_method_id = create_response.json()["id"]
    

    retrieve_response = client.get(f"/payments/{payment_method_id}")
    assert retrieve_response.status_code == 200
    data = retrieve_response.json()
    assert data["id"] == payment_method_id
    assert data["object"] == "payment_method"


def test_create_webhook_endpoint():
    response = client.post("/create-webhook-endpoint")
    assert response.status_code == 200
    data = response.json()["webhook_endpoint"]
    assert "id" in data
    assert data["object"] == "webhook_endpoint"
    assert data["url"] == "https://example.com/my/webhook/endpoint"
