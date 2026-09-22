from typing import Optional

from models import Order


_orders: dict[str, Order] = {}
_idempotency_index: dict[str, str] = {}
_next_order_number = 1001


def create_order(order: Order) -> Order:
    _orders[order.order_id] = order
    _idempotency_index[order.idempotency_key] = order.order_id
    return order


def get_order(order_id: str) -> Optional[Order]:
    return _orders.get(order_id)


def get_order_by_idempotency_key(key: str) -> Optional[Order]:
    order_id = _idempotency_index.get(key)

    if order_id is None:
        return None

    return _orders.get(order_id)


def next_order_id() -> str:
    global _next_order_number

    order_id = f"ORD-{_next_order_number}"
    _next_order_number += 1

    return order_id


def list_orders(status: str | None = None) -> list[Order]:
    orders = list(_orders.values())

    if status is not None:
        orders = [order for order in orders if order.status == status]

    return orders


def clear_store() -> None:
    global _next_order_number

    _orders.clear()
    _idempotency_index.clear()
    _next_order_number = 1001
