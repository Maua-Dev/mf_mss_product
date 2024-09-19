from typing import List, Optional
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser

class GetAllSchedulesByRestaurantUseCase:
    def __init__(self, userrepo: IUserRepository, orderrepo: IOrderRepository):
        self.userrepo = userrepo
        self.orderrepo = orderrepo
        
    def execute(self, user_id: str, restaurant: RESTAURANT) -> List[Schedule]:
        #verifica se o usuario existe no repo de usuarios
        user = self.userrepo.get_user_by_id(user_id)
        if not user:
            raise UnregisteredUser(f"User with id {user_id} not found")
        
        #busca todos os agendamentos do restaurante
        schedules = self.orderrepo.get_all_schedules_by_restaurant(restaurant)

        return schedules
