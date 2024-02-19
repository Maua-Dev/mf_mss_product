import pytest

from src.modules.create_feedback.create_feedback_usecase import CreateFeedbackUsecase
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, UnregisteredUser
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class Test_CreateFeedbackUsecase:

    def test_create_feedback(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback=repo_feedback,repo_user=repo_user)

        feedback = usecase(order_id="d78a47cb-80db-4661-b810-8e7c9419d61b", user_id="93bc6ada-c0d1-7054-66ab-e17414c48af9", restaurant=RESTAURANT.CANTINA_DO_MOLEZA, value=3)

        assert repo_feedback.feedbacks[-1].order_id == feedback.order_id
        assert repo_feedback.feedbacks[-1].user_id == feedback.user_id
        assert repo_feedback.feedbacks[-1].restaurant == feedback.restaurant
        assert repo_feedback.feedbacks[-1].value == feedback.value

    def test_create_feedback_unregistered_user(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback=repo_feedback,repo_user=repo_user)

        with pytest.raises(UnregisteredUser):
            feedback = usecase(order_id="d78a47cb-80db-4661-b810-8e7c9419d61b", user_id="93bc6ada-c0d1-7054-667b-e17414c48af9", restaurant=RESTAURANT.CANTINA_DO_MOLEZA, value=3)
