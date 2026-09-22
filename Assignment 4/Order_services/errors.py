from flask import jsonify


def problem(status: int, title: str, detail: str, problem_type: str | None = None):
    body = {
        "type": problem_type or f"https://campuseats.example/problems/{status}",
        "title": title,
        "status": status,
        "detail": detail,
    }
    return jsonify(body), status


def validate(data):
    """
    Validate a create-order request before app.py touches request fields.
    """
    if not isinstance(data, dict):
        return False, "Request body must be a JSON object."

    required = [
        "userId",
        "cartId",
        "deliveryAddressId",
        "paymentMethod",
    ]

    for field in required:
        if field not in data:
            return False, f"Missing required field: {field}"

        if not isinstance(data[field], str) or not data[field].strip():
            return False, f"{field} must be a non-empty string."

    if data["paymentMethod"] not in {"UPI", "CARD", "WALLET"}:
        return False, "paymentMethod must be UPI, CARD, or WALLET."

    if "couponCode" in data and data["couponCode"] is not None:
        if not isinstance(data["couponCode"], str):
            return False, "couponCode must be a string or null."

    return True, None


def validate_cancellation(data):
    if not isinstance(data, dict):
        return False, "Request body must be a JSON object."

    if "reason" not in data:
        return False, "Missing required field: reason."

    if not isinstance(data["reason"], str) or not data["reason"].strip():
        return False, "reason must be a non-empty string."

    return True, None
