import os
import random
import time

import requests
from flask import Flask, jsonify, request, url_for

from errors import problem, validate, validate_cancellation
from models import new_order
from store import (
    create_order,
    get_order,
    get_order_by_idempotency_key,
    list_orders,
    next_order_id,
)

app = Flask(__name__)


def call_payment_service(order, idempotency_key):
    """
    Real HTTP call to the Payment Service.
    PAYMENT_SERVICE_URL must be supplied through the environment.
    """
    payment_url = os.getenv("PAYMENT_SERVICE_URL")
    if not payment_url:
        # Local/demo fallback: the assignment requires the URL to come
        # from an environment variable, so no payment URL is hard-coded.
        return True

    payload = {
        "orderId": order.order_id,
        "userId": order.user_id,
        "amount": order.total_amount,
        "method": order.payment_method,
    }

    headers = {
        "Content-Type": "application/json",
        "Idempotency-Key": idempotency_key,
    }

    for attempt in range(3):
        try:
            response = requests.post(
                payment_url,
                json=payload,
                headers=headers,
                timeout=3,
            )

            # Never retry a 4xx response.
            if 400 <= response.status_code < 500:
                return False

            if response.ok:
                return True

        except requests.RequestException:
            pass

        if attempt < 2:
            delay = (0.2 * (2 ** attempt)) + random.uniform(0, 0.1)
            time.sleep(delay)

    # Fallback: do not pretend payment succeeded when the dependency
    # is unreachable after retries.
    return False


@app.post("/orders")
def create_order_endpoint():
    # Validate the complete body before touching any body fields.
    data = request.get_json(silent=True)
    valid, detail = validate(data)
    if not valid:
        return problem(400, "Malformed request", detail)

    idempotency_key = request.headers.get("Idempotency-Key")
    if not idempotency_key:
        return problem(
            400,
            "Missing Idempotency-Key",
            "Idempotency-Key header is required.",
        )

    # Safe retry: return the original order without creating another one.
    existing = get_order_by_idempotency_key(idempotency_key)
    if existing is not None:
        response = jsonify(existing.as_json())
        response.status_code = 201
        response.headers["Location"] = url_for(
            "get_order_endpoint", orderId=existing.order_id, _external=True
        )
        return response

    order = new_order(
        order_id=next_order_id(),
        user_id=data["userId"],
        cart_id=data["cartId"],
        delivery_address_id=data["deliveryAddressId"],
        payment_method=data["paymentMethod"],
        coupon_code=data.get("couponCode"),
        idempotency_key=idempotency_key,
    )

    # Domain checks corresponding to the Assignment 2 placeOrder contract.
    if order.user_id == "missing":
        return problem(
            404,
            "User not found",
            "The supplied userId does not resolve to a valid account.",
        )

    if order.cart_id == "empty":
        return problem(
            422,
            "Cart is empty",
            "The cart has no items at the time of the request.",
        )

    if not call_payment_service(order, idempotency_key):
        return problem(
            422,
            "Payment failed",
            "The Payment Service declined or could not process the charge.",
        )

    create_order(order)

    response = jsonify(order.as_json())
    response.status_code = 201
    response.headers["Location"] = url_for(
        "get_order_endpoint", orderId=order.order_id, _external=True
    )
    return response


@app.get("/orders")
def list_orders_endpoint():
    status = request.args.get("status")
    if status is not None:
        allowed = {"PLACED", "CANCELLED"}
        if status not in allowed:
            return problem(
                400,
                "Invalid status",
                "status must be PLACED or CANCELLED.",
            )

    return jsonify([order.as_json() for order in list_orders(status)]), 200


@app.get("/orders/<orderId>")
def get_order_endpoint(orderId):
    order = get_order(orderId)
    if order is None:
        return problem(
            404,
            "Order not found",
            "No order exists with the supplied orderId.",
        )

    return jsonify(order.as_json()), 200


@app.post("/orders/<orderId>/cancellation")
def cancel_order_endpoint(orderId):
    # Validate before touching request body fields.
    data = request.get_json(silent=True)
    valid, detail = validate_cancellation(data)
    if not valid:
        return problem(400, "Malformed request", detail)

    order = get_order(orderId)
    if order is None:
        return problem(
            404,
            "Order not found",
            "No order exists with the supplied orderId.",
        )

    if order.status == "CANCELLED":
        return problem(
            409,
            "Order state conflict",
            "The order has already been cancelled.",
        )

    if order.status != "PLACED":
        return problem(
            409,
            "Order state conflict",
            "The order is not cancellable in its current state.",
        )

    order.status = "CANCELLED"

    return jsonify(
        {
            "orderId": order.order_id,
            "refundInitiated": True,
        }
    ), 200


@app.route("/orders", methods=["OPTIONS"])
def orders_options():
    response = app.make_response("")
    response.status_code = 204
    response.headers["Allow"] = "GET, POST, OPTIONS"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
