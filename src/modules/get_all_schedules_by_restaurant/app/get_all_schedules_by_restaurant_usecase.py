from typing import Any, List
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.order_repository_interface import IOrderRepository


class GetAllSchedulesByRestaurantUsecase:

    def __init__(self, repo_order: IOrderRepository):
        self.repo_order = repo_order

    def __call__(self, restaurant: RESTAURANT) -> List[Order]:
        return self.repo_order.get_all_schedules_by_restaurant(restaurant=restaurant)