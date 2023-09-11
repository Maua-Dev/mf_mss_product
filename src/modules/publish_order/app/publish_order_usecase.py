from typing import List
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.order_repository_interface import IOrderRepository

class PublishOrderUsecase:

    def __init__(self, repo: IOrderRepository):
        self.repo = repo

    def __call__(self, order: Order) -> List[Connection]:
        
        connections_list = self.repo.get_all_connections_by_restaurant(order.restaurant)

        if len(connections_list) == 0:
            return True
            
        return self.repo.publish_order(connections_list=connections_list, order=order)
        