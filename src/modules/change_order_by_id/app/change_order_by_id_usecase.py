from typing import Optional, List

from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotOrderOwner, \
    OrderCantBeUpdated, ProducutsListCantBeEmpty


class ChangeOrderByIdUsecase:
    def __init__(self, repo_order: IOrderRepository, repo_user: IUserRepository):
        self.repo_order = repo_order
        self.repo_user = repo_user

    def __call__(self, order_id: str, user_id: str, new_observation: Optional[str] = None,
                 new_prods_list: Optional[List[OrderProduct]] = None):
        order = self.repo_order.get_order_by_id(order_id=order_id)
        user = self.repo_user.get_user_by_id(user_id=user_id)

        if order is None:
            raise NoItemsFound(f'order with id {order_id}')

        if user is None:
            raise UnregisteredUser()

        if user.role != ROLE.ADMIN:
            if order.user_id != user_id:
                raise UserNotOrderOwner()
            if order.status != STATUS.PENDING:
                raise OrderCantBeUpdated()

        if new_prods_list is not None:
            if len(new_prods_list) <= 0:
                raise ProducutsListCantBeEmpty()

        updated_order = self.repo_order.update_order(
            order_id=order_id,
            new_products=new_prods_list,
            new_status=None,
            new_total_price=None,
            new_observation=new_observation,
            new_aborted_reason=None
        )

        return updated_order
