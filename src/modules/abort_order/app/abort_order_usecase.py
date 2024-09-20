import datetime
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.action_enum import ACTION
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotOrderOwner, \
    OrderAlreadyPreparing, UserNotAllowed


class AbortOrderUsecase:

    def __init__(self, repo_order: IOrderRepository, repo_user: IUserRepository):
        self.repo_order = repo_order
        self.repo_user = repo_user

    def __call__(self, order_id: str, user_id: str, new_aborted_reason: str):
        user = self.repo_user.get_user_by_id(user_id=user_id)

        if user is None:
            raise UnregisteredUser()

        order_to_update: Order = self.repo_order.get_order_by_id(order_id=order_id)

        if order_to_update is None:
            raise NoItemsFound("order")

        allowed_roles = [ROLE.ADMIN, ROLE.OWNER]

        if order_to_update.status != STATUS.PENDING and user.role not in allowed_roles:
            raise OrderAlreadyPreparing()

        if user.role in [ROLE.OWNER, ROLE.SELLER] and order_to_update.restaurant != user.restaurant:
            raise UserNotAllowed()

        if user.role in [ROLE.ADMIN, ROLE.OWNER, ROLE.SELLER]:
            updated_order = self.repo_order.update_order(order_id=order_id, new_aborted_reason=new_aborted_reason,
                                                         new_status=STATUS.CANCELLED, new_action=ACTION.DELETED)
            return updated_order

        if order_to_update.user_id != user_id:
            raise UserNotOrderOwner()


        updated_order = self.repo_order.update_order(order_id=order_id, new_aborted_reason=new_aborted_reason,
                                                     new_status=STATUS.CANCELLED, new_action=ACTION.DELETED)

        return updated_order
