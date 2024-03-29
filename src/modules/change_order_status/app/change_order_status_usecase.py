from datetime import datetime

from src.shared.domain.entities.order import Order
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.action_enum import ACTION
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import UserNotAllowed, ForbiddenAction, NoItemsFound, \
    UserNotRelatedToRestaurant


class ChangeOrderStatusUsecase:
    def __init__(self, repo_order: IOrderRepository, repo_user: IUserRepository):
        self.repo_order = repo_order
        self.repo_user = repo_user

    def __call__(self, order_id: str, user_id: str, new_status: STATUS):
        user = self.repo_user.get_user_by_id(user_id)

        if user.role == ROLE.USER:
            raise UserNotAllowed()

        order_to_update: Order = self.repo_order.get_order_by_id(order_id)
        if order_to_update is None:
            raise NoItemsFound("order")

        if user.role == ROLE.ADMIN:
            updated_order = self.repo_order.update_order(
                order_id=order_id,
                new_status=new_status,
                new_action=ACTION.EDITED
            )
            updated_order.last_status_update_milliseconds = int(datetime.now().timestamp() * 1000)
            return updated_order

        if user.restaurant != order_to_update.restaurant:
            raise UserNotRelatedToRestaurant(order_to_update.restaurant)

        updated_order = self.repo_order.update_order(
            order_id=order_id,
            new_status=new_status,
            new_action=ACTION.EDITED
        )
        updated_order.last_status_update_milliseconds = int(datetime.now().timestamp() * 1000)

        return updated_order
