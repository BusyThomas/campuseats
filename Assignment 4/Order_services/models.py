from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class Order:
    order_id: str
    user_id: str
    cart_id: str
    delivery_address_id: str
    payment_method: str
    coupon_code: str | None
    status: str
    total_amount: float
    estimated_delivery_minutes: int
    idempotency_key: str
    created_at: str

    def as_json(self) -> dict[str, Any]:
        # Public representation intentionally differs from the stored record:
        # internal fields such as cart_id and idempotency_key are not exposed.
        return {
            "orderId": self.order_id,
            "status": self.status,
            "totalAmount": self.total_amount,
            "estimatedDeliveryMinutes": self.estimated_delivery_minutes,
        }


def new_order(
    order_id: str,
    user_id: str,
    cart_id: str,
    delivery_address_id: str,
    payment_method: str,
    coupon_code: str | None,
    idempotency_key: str,
) -> Order:
    return Order(
        order_id=order_id,
        user_id=user_id,
        cart_id=cart_id,
        delivery_address_id=delivery_address_id,
        payment_method=payment_method,
        coupon_code=coupon_code,
        status="PLACED",
        total_amount=349.00,
        estimated_delivery_minutes=25,
        idempotency_key=idempotency_key,
        created_at=datetime.now(timezone.utc).isoformat(),
    )
