from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.action_enum import ACTION
from src.shared.domain.entities.connection import Connection
from src.shared.domain.entities.feedback import Feedback

class IOrderRepository(ABC):

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_all_active_orders_by_restaurant(self, restaurant: RESTAURANT) -> List[Order]:
        """
        This method return all orders which status are PENDING or PREPARING of a single restaurant  that the user
        wishes.
        """
        pass

    @abstractmethod
    def get_all_orders_by_restaurant(self, restaurant: RESTAURANT, amount: int = 20, exclusive_start_key: Optional[str] = None) -> List[Order]:
        """
        This method return the history of orders of the selected restaurant with pagination. The total of orders per
        page is defined by amount.
        """
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        pass
    
    @abstractmethod
    def update_order(self, order_id: str, new_products: Optional[List[OrderProduct]] = None,
                     new_status: Optional[STATUS] = None,
                     new_total_price: Optional[float] = None,
                     new_aborted_reason: Optional[str] = None,
                     new_action: Optional[ACTION] = None):
        pass

    @abstractmethod
    def get_all_connections_by_restaurant(self, restaurant: RESTAURANT) -> List[Connection]:
        pass

    @abstractmethod
    def create_connection(self, connection: Connection) -> Connection:
        pass

    @abstractmethod
    def abort_connection(self, connection_id: str) -> Connection:
        """
        This method gets the connection based on the connection_id and deletes it based on the connection's restaurant.
        """
        pass
    
    @abstractmethod
    def publish_order(self, connections_list: List[Connection], order: Order) -> bool:
        pass

    @abstractmethod
    def get_all_orders_by_user(self, user_id: str, amount: int = 20, exclusive_start_key: Optional[str] = None) -> List[Order]:
        """
        This method return the history of orders of the selected user with pagination. The total of orders per
        page is defined by amount.
        """
        pass

    @abstractmethod
    def get_connection_by_connection_id(self, connection_id: str) -> Optional[Connection]:
        pass

    @abstractmethod
    def create_feedback(self, feedback: Feedback) -> Feedback:
        pass

    @abstractmethod
    def get_average_feedback_by_restaurant(self, restaurant: RESTAURANT) -> float:
        pass
