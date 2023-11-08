from typing import List
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import UserNotOrderOwner, NoItemsFound, UnregisteredUser


class GetAllOrdersByUserUsecase:

    def __init__(self, repo_order: IOrderRepository, repo_user: IUserRepository):
        self.repo_order = repo_order
        self.repo_user = repo_user

    def __call__(self, user_id: str, exclusive_start_key: str = None, amount: int = None) -> List[Order]:
        
        user = self.repo_user.get_user_by_id(user_id)

        if user is None:
            raise UnregisteredUser()
        
        if exclusive_start_key:
            order = self.repo_order.get_order_by_id(exclusive_start_key)

            if order is None:
                raise NoItemsFound("exclusive_start_key")
        
            if user.role != ROLE.ADMIN:
                if order.user_id != user_id:
                    raise UserNotOrderOwner()

        return self.repo_order.get_all_orders_by_user(user_id=user_id, exclusive_start_key=exclusive_start_key, amount=amount)