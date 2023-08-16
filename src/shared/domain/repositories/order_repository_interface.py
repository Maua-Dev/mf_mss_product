from abc import ABC, abstractmethod

from src.shared.domain.entities.order import Order


class IOrderRepository(ABC):

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass