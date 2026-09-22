import pytest

from app import app
from store import clear_store


@pytest.fixture
def client():
    app.config["TESTING"] = True
    clear_store()

    with app.test_client() as client:
        yield client

    clear_store()


def order_payload():
    return {
        "userId": "USER-1001",
        "cartId": "CART-1001",
        "deliveryAddressId": "ADDR-1001",
        "paymentMethod": "UPI",
    }


def test_create_order_success(client):
    response = client.post(
        "/orders",
        json=order_payload(),
        headers={"Idempotency-Key": "test-key-1"},
    )

    assert response.status_code == 201
    assert response.headers["Location"].endswith("/orders/ORD-1001")
    assert response.json["orderId"] == "ORD-1001"


def test_idempotent_repeat_returns_original_order(client):
    headers = {"Idempotency-Key": "same-key"}

    first = client.post(
        "/orders",
        json=order_payload(),
        headers=headers,
    )

    second = client.post(
        "/orders",
        json=order_payload(),
        headers=headers,
    )

    assert first.status_code == 201
    assert second.status_code == 201
    assert second.json["orderId"] == first.json["orderId"]
    assert second.headers["Location"] == first.headers["Location"]


def test_malformed_request_returns_400(client):
    response = client.post(
        "/orders",
        json={"userId": "USER-1001"},
        headers={"Idempotency-Key": "bad-request-key"},
    )

    assert response.status_code == 400


def test_unknown_order_returns_404(client):
    response = client.get("/orders/ORD-9999")

    assert response.status_code == 404


def test_options_returns_allow_header(client):
    response = client.options("/orders")

    assert response.status_code == 204
    assert response.headers["Allow"] == "GET, POST, OPTIONS"
    assert response.data == b""
