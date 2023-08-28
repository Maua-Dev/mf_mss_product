from abc import ABC, abstractmethod
from typing import Dict, List

from src.shared.domain.entities.order import Order
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class IOrderRepository(ABC):

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_all_active_orders_by_restaurant(self, restaurant: RESTAURANT) -> List[Order]:
        """This method return all orders which status are PENDING or PREPARING of a single restaurant  that the user wishes."""
        pass

    