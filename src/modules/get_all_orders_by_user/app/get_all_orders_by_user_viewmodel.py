from typing import List, Optional
from src.shared.domain.entities.order import Order

from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.action_enum import ACTION


class OrderProductViewmodel:
    order_product: OrderProduct

    def __init__(self, order_product: OrderProduct):
        self.order_product = order_product

    def to_dict(self) -> dict:
        return {
            "product_name": self.order_product.product_name,
            "product_id": self.order_product.product_id,
            "quantity": self.order_product.quantity,
            "observation": self.order_product.observation
        }


class OrderViewmodel:
    order_id: str
    user_name: str
    user_id: str
    products: List[OrderProduct]
    creation_time_milliseconds: int
    restaurant: RESTAURANT
    status: STATUS
    action: ACTION
    aborted_reason: Optional[str] = None
    total_price: float
    time_reserved: Optional[int] = None

    def __init__(self, order: Order):
        self.order_id = order.order_id
        self.user_name = order.user_name
        self.user_id = order.user_id
        self.products = [OrderProductViewmodel(order_product) for order_product in order.products]
        self.creation_time_milliseconds = order.creation_time_milliseconds
        self.restaurant = order.restaurant
        self.status = order.status
        self.aborted_reason = order.aborted_reason
        self.total_price = order.total_price
        self.last_status_update_milliseconds = order.last_status_update_milliseconds
        self.action = order.action
        self.time_reserved = order.time_reserved

    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "user_name": self.user_name,
            "user_id": self.user_id,
            "products": [order_product.to_dict() for order_product in self.products],
            "creation_time_milliseconds": self.creation_time_milliseconds,
            "restaurant": self.restaurant.value,
            "status": self.status.value,
            "aborted_reason": self.aborted_reason,
            "total_price": self.total_price,
            "last_status_update": self.last_status_update_milliseconds,
            "action": self.action.value,
            "time_reserved": self.time_reserved
        }


class GetAllOrdersByUserViewmodel:
    all_orders: List[Order]

    def __init__(self, all_orders: List[Order]):
        self.all_orders = all_orders

    def to_dict(self):
        return {
            'all_orders_by_user': [OrderViewmodel(order).to_dict() for order in self.all_orders] if len(self.all_orders) > 0 else [],
            'last_order_id': self.all_orders[-1].order_id if len(self.all_orders) > 0 else None,
            'message': "the orders were retrieved"
        }
