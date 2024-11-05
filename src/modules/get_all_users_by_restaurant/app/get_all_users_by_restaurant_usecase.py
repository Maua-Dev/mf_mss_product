from typing import List
from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNeedsRestaurant, UserNotAllowed


class GetAllUsersByRestaurantUseCase:
    def __init__(self, user_repo: IUserRepository, order_repo: IOrderRepository):
        self.user_repo = user_repo
        self.order_repo = order_repo

    def __call__(self, user_id: str, restaurant: RESTAURANT) -> List[User]:

        user = self.user_repo.get_user_by_id(user_id)

        if not user:
            raise UnregisteredUser()
        
        if user.role not in [ROLE.OWNER, ROLE.ADMIN]:
            raise UserNotAllowed()

        if user.restaurant is None:
            raise UserNeedsRestaurant()
        
        users = self.user_repo.get_all_users_by_restaurant(restaurant)

        return users
        
