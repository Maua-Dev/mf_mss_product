from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS

class IOrderRepository(ABC):

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_all_active_orders_by_restaurant(self, restaurant: RESTAURANT) -> List[Order]:
        """This method return all orders which status are PENDING or PREPARING of a single restaurant  that the user wishes."""
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        pass
    
    @abstractmethod
    def update_order(self, order_id: str, new_products: Optional[List[OrderProduct]] = None,
                     new_status: Optional[STATUS] = None,
                     new_total_price: Optional[float] = None, new_observation: Optional[str] = None,
                     new_aborted_reason: Optional[str] = None):
        pass

    @abstractmethod
    def get_all_connections_by_restaurant(self, restaurant: RESTAURANT) -> List[Connection]:
        pass