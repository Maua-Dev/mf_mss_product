import pytest

from src.modules.create_feedback.create_feedback_controller import CreateFeedbackController
from src.modules.create_feedback.create_feedback_usecase import CreateFeedbackUsecase
from src.shared.domain.entities.feedback import Feedback
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class Test_CreteFeedbackController:
    def test_create_feedback_controller(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback, repo_user)
        controller = CreateFeedbackController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "order_id": "d78a47cb-80db-4661-b810-8e7c9419d61b",
            "restaurant": "SOUZA_DE_ABREU",
            "value": 3}
        )

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body["message"] == "the feedback was created"
        assert response.body["feedback"]["order_id"] == "d78a47cb-80db-4661-b810-8e7c9419d61b"
        assert response.body["feedback"]["restaurant"] == "SOUZA_DE_ABREU"
        assert response.body["feedback"]["value"] == 3

    def test_create_feedback_controller_order_id_is_missing(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback, repo_user)
        controller = CreateFeedbackController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "restaurant": "SOUZA_DE_ABREU",
            "value": 3}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field order_id is missing"
      
    def test_create_feedback_controller_restaurant_is_missing(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback, repo_user)
        controller = CreateFeedbackController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "order_id": "d78a47cb-80db-4661-b810-8e7c9419d61b",
            "value": 3}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_create_feedback_controller_value_is_missing(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback, repo_user)
        controller = CreateFeedbackController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "order_id": "d78a47cb-80db-4661-b810-8e7c9419d61b",
            "restaurant": "SOUZA_DE_ABREU"
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field value is missing"

    def test_create_feedback_controller_unregistered_user(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback, repo_user)
        controller = CreateFeedbackController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": "um id",
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "order_id": "d78a47cb-80db-4661-b810-8e7c9419d61b",
            "restaurant": "SOUZA_DE_ABREU",
            "value": 3}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "That user is not registered"

    def test_create_feedback_controller_value_less_than_minumum(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback, repo_user)
        controller = CreateFeedbackController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "order_id": "d78a47cb-80db-4661-b810-8e7c9419d61b",
            "restaurant": "SOUZA_DE_ABREU",
            "value": 0}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "value can't be less than one"

    def test_create_feedback_controller_value_more_than_maximum(self):
        repo_feedback = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateFeedbackUsecase(repo_feedback, repo_user)
        controller = CreateFeedbackController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "order_id": "d78a47cb-80db-4661-b810-8e7c9419d61b",
            "restaurant": "SOUZA_DE_ABREU",
            "value": 6}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "value can't be more than five"