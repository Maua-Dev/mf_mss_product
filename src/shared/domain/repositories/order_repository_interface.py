from datetime import time
from typing import List, Optional
from abc import ABC, abstractmethod

from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.entities.schedule import Schedule
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
    def get_all_orders_by_restaurant(self, restaurant: RESTAURANT, amount: int = 20,
                                     exclusive_start_key: Optional[str] = None) -> List[Order]:
        """
        This method return the history of orders of the selected restaurant with pagination. The total of orders per
        page is defined by amount.
        """
        pass

    @abstractmethod
    def get_all_schedules_by_restaurant(self, restaurant: RESTAURANT) -> List[Order]:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        pass

    @abstractmethod
    def update_order(self, order_id: str, new_products: Optional[List[OrderProduct]] = None,
                     new_status: Optional[STATUS] = None,
                     new_total_price: Optional[float] = None,
                     new_aborted_reason: Optional[str] = None,
                     new_action: Optional[ACTION] = None,
                     new_schedule: Optional[Schedule] = None
                     ) -> Optional[Order]:
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
    def get_all_orders_by_user(self, user_id: str, amount: int = 20, exclusive_start_key: Optional[str] = None) -> List[
        Order]:
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

    @abstractmethod
    def get_feedback_by_order_id(self, order_id: str) -> Optional[Feedback]:
        pass

    @abstractmethod
    def create_schedule(self, schedule: Schedule) -> Schedule:
        pass

    @abstractmethod
    def get_schedules_by_restaurant(self, restaurant: RESTAURANT) -> Optional[List[Schedule]]:
        pass

    @abstractmethod
    def get_schedule_by_id(self, schedule_id: str) -> Optional[Schedule]:
        pass

    @abstractmethod
    def update_schedule(self, schedule_id: str, new_initial_time: Optional[time] = None,
                        new_end_time: Optional[time] = None,
                        new_accepted_reservation: Optional[bool] = None) -> Optional[Schedule]:
        pass

    @abstractmethod
    def check_schedule(self, schedule: Schedule) -> bool:
        """
        This method checks if the schedule is available for reservation.
        """
        pass

