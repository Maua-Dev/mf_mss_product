from src.modules.abort_order.app.abort_order_controller import AbortOrderController
from src.modules.abort_order.app.abort_order_usecase import AbortOrderUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_AbortOrderController:
    def test_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user,)
        controller = AbortOrderController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "order_id": repo_order.orders[0].order_id,
            "aborted_reason": "Desisti da compra!"
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "the order was aborted"
        assert repo_order.orders[0].aborted_reason == "Desisti da compra!"

    def test_requester_user_is_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)
        controller = AbortOrderController(usecase)

        request = HttpRequest(body={
            "order_id": repo_order.orders[0].order_id,
            "aborted_reason": "Desisti da compra!"
        })

        response = controller(request)

        assert response.status_code == 400

    def test_requester_order_id_is_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)
        controller = AbortOrderController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "aborted_reason": "Desisti da compra!"
        })

        response = controller(request)

        assert response.status_code == 400

    def test_new_aborted_reason_is_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)
        controller = AbortOrderController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "order_id": repo_order.orders[0].order_id
        })

        response = controller(request)

        assert response.status_code == 400