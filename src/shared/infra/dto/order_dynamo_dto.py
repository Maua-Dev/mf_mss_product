from decimal import Decimal
from typing import List, Optional
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS

class OrderDynamoDTO:
    order_id: str
    user_name: str
    user_id: str
    products: List[OrderProduct]
    creation_time_milliseconds: int
    restaurant: RESTAURANT
    status: STATUS
    aborted_reason: Optional[str] = None
    total_price: float
    last_status_update_milliseconds: int = None

    def __init__(self, order_id: str, user_name: str, user_id: str, products: List[OrderProduct], creation_time_milliseconds: int, restaurant: RESTAURANT, status: STATUS, total_price: float, last_status_update_milliseconds: int = None, aborted_reason: Optional[str] = None):
        self.order_id = order_id
        self.user_name = user_name
        self.user_id = user_id
        self.products = products
        self.creation_time_milliseconds = creation_time_milliseconds
        self.restaurant = restaurant
        self.status = status
        self.total_price = total_price
        self.last_status_update_milliseconds = last_status_update_milliseconds
        self.aborted_reason = aborted_reason
        
    @staticmethod
    def from_entity(order:Order) -> "OrderDynamoDTO":
        """
        Parse data from Order to OrderDynamoDTO
        """
        return OrderDynamoDTO(
            order_id = order.order_id,
            user_name = order.user_name,    
            user_id = order.user_id,
            products = order.products,
            creation_time_milliseconds = order.creation_time_milliseconds,
            restaurant = order.restaurant,
            status = order.status, 
            total_price = order.total_price,
            last_status_update_milliseconds = order.last_status_update_milliseconds,
            aborted_reason = order.aborted_reason
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from OrderDynamoDTO to dict
        """
        data = {
            "entity": "order",
            "order_id": self.order_id,
            "user_name": self.user_name,
            "user_id": self.user_id,
            "products":  [{
                "product_name": product.product_name,
                "product_id": product.product_id,
                "quantity": Decimal(str(product.quantity)),
                "observation": product.observation
            } for product in self.products],
            "creation_time_milliseconds": Decimal(str(self.creation_time_milliseconds)),
            "restaurant": self.restaurant.value,
            "status": self.status.value,
            "total_price": Decimal(str(self.total_price)),
            "last_status_update_milliseconds": Decimal(str(self.last_status_update_milliseconds)) if self.last_status_update_milliseconds is not None else None,
            "aborted_reason": self.aborted_reason if self.aborted_reason is not None else None
        }

        data_without_none_values = {k: v for k, v in data.items() if v is not None}

        return data_without_none_values
    
    @staticmethod
    def from_dynamo(order_data: dict) -> "OrderDynamoDTO":
        """
        Parse data from DynamoDB to OrderDynamoDTO
        @param order_data: dict from DynamoDB
        """
        return OrderDynamoDTO(
            order_id=str(order_data["order_id"]),
            user_name=str(order_data["user_name"]),
            user_id=str(order_data["user_id"]),
            products=[OrderProduct(
                product_name=product["product_name"],
                product_id=product["product_id"],
                quantity=int(product["quantity"]),
                observation=product.get("observation")
            ) for product in order_data["products"]],
            creation_time_milliseconds=int(order_data["creation_time_milliseconds"]),
            restaurant=RESTAURANT(order_data.get("restaurant")),
            status=STATUS(order_data.get("status")),
            total_price=float(order_data["total_price"]),
            last_status_update_milliseconds=int(order_data.get("last_status_update_milliseconds")),
            aborted_reason=order_data.get("aborted_reason") if order_data.get("aborted_reason") is not None else None
        )

    def to_entity(self) -> Order:
        """
        Parse data from OrderDynamoDTO to Order
        """
        return Order(
            order_id=self.order_id,
            user_name=self.user_name,
            user_id=self.user_id,
            products=self.products,
            creation_time_milliseconds=self.creation_time_milliseconds,
            restaurant=self.restaurant,
            status=self.status,
            total_price=self.total_price,
            last_status_update_milliseconds=self.last_status_update_milliseconds,
            aborted_reason=self.aborted_reason
        )

    def __eq__(self, other):
        return self.order_id == other.order_id and self.user_name == other.user_name and self.user_id == other.user_id and self.products == other.products and self.creation_time_milliseconds == other.creation_time_milliseconds and self.restaurant == other.restaurant and self.status == other.status and self.total_price == other.total_price and self.last_status_update_milliseconds == other.last_status_update_milliseconds and self.aborted_reason == other.aborted_reason