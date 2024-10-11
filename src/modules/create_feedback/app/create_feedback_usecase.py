import uuid
from src.shared.domain.entities.feedback import Feedback
from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed, OrderAlreadyHaveFeedback, FeedbackNotAllowed

class CreateFeedbackUsecase:
    def __init__(self, repo_feedback: IOrderRepository, repo_user: IUserRepository):
        self.repo_feedback = repo_feedback
        self.repo_user = repo_user

    def __call__(self, order_id: str, user_id: str, restaurant: RESTAURANT, value: int) -> Feedback:

        user = self.repo_user.get_user_by_id(user_id)

        order = self.repo_feedback.get_order_by_id(order_id)

        if user is None:
            raise UnregisteredUser()

        feedback = self.repo_feedback.get_feedback_by_order_id(order_id)

        if feedback is not None:
            raise OrderAlreadyHaveFeedback()
        
        if order.restaurant != restaurant:
            raise FeedbackNotAllowed()

        feedback = Feedback(order_id=order_id, user_id=user_id, restaurant=restaurant, value=value)

        return self.repo_feedback.create_feedback(feedback=feedback)
