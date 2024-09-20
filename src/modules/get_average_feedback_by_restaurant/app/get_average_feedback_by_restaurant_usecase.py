from typing import Dict

from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from src.shared.domain.repositories.order_repository_interface import IOrderRepository


class GetAverageFeedbackByRestaurantUsecase:
    def __init__(self, user_repo: IUserRepository, order_repo: IOrderRepository):
        self.user_repo = user_repo
        self.order_repo = order_repo

    def __call__(self, user_id: str) -> Dict[str, float]:
        user = self.user_repo.get_user_by_id(user_id=user_id)
        if user is None:
            raise UnregisteredUser()
        if user.role not in [ROLE.ADMIN, ROLE.OWNER, ROLE.SELLER]:
            raise UserNotAllowed()
        if not user.restaurant:
            raise UserNotAllowed()

        average_feedback = self.order_repo.get_average_feedback_by_restaurant(restaurant=user.restaurant)

        return {
            "average_feedback": average_feedback,
            "message": "the average feedback was retrieved"
        }
