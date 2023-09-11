from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import UserNotOrderOwner, UnregisteredUser


class GetCurrentOrderStateByIdUsecase:
    def __init__(self, user_repo: IUserRepository, order_repo: IOrderRepository):
        self.user_repo = user_repo
        self.order_repo = order_repo

    def __call__(self, order_id: str, user_id: str):
        order = self.order_repo.get_order_by_id(order_id=order_id)
        user = self.user_repo.get_user_by_id(user_id=user_id)

        if user is None:
            raise UnregisteredUser()

        if order.user_id != user_id:
            raise UserNotOrderOwner()

        return order
