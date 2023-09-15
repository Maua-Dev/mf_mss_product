from typing import List
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import MismatchID, NoItemsFound, UnregisteredUser, UserNotAllowed


class GetAllOrdersByUserUsecase:

    def __init__(self, repo_order: IOrderRepository, repo_user: IUserRepository):
        self.repo_order = repo_order
        self.repo_user = repo_user

    def __call__(self, user_id: str, order_id: str) -> List[Order]:
        
        user = self.repo_user.get_user_by_id(user_id)

        if user is None:
            raise UnregisteredUser()

        if user.role in [ROLE.OWNER, ROLE.ADMIN, ROLE.SELLER]:
            raise UserNotAllowed()
        
        order = self.repo_order.get_order_by_id(order_id)

        if order is None:
            raise NoItemsFound("order_id")
        
        if order.user_id != user_id:
            raise MismatchID()

        return self.repo_order.get_all_orders_by_user(user_id=user_id, order_id=order_id)