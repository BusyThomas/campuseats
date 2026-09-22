from app import app
from store import clear_store


def test_unknown_order_returns_404():
    app.config["TESTING"] = True
    clear_store()

    with app.test_client() as client:
        response = client.get("/orders/ORD-9999")

        assert response.status_code == 404
        assert response.get_json()["status"] == 404
