from app import app
from store import clear_store


def test_malformed_body_returns_400():
    app.config["TESTING"] = True
    clear_store()

    with app.test_client() as client:
        response = client.post(
            "/orders",
            json={"userId": "user-1"},
            headers={"Idempotency-Key": "bad-body"},
        )

        assert response.status_code == 400
        body = response.get_json()
        assert {"type", "title", "status", "detail"} <= body.keys()
