from src.modules.change_order_status.app.change_order_status_controller import ChangeOrderStatusController
from src.modules.change_order_status.app.change_order_status_usecase import ChangeOrderStatusUsecase
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ChangeOrderStatusController:
    def test_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ChangeOrderStatusUsecase(repo_order=repo_order, repo_user=repo_user)
        controller = ChangeOrderStatusController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "order_id": repo_order.orders[0].order_id,
            "new_status": STATUS.REFUSED.value
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "the order status was updated"
        assert repo_order.orders[0].status == STATUS.REFUSED

    def test_requester_user_is_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ChangeOrderStatusUsecase(repo_order=repo_order, repo_user=repo_user)
        controller = ChangeOrderStatusController(usecase)

        request = HttpRequest(body={
            "order_id": repo_order.orders[0].order_id,
            "new_status": STATUS.REFUSED.value
        })

        response = controller(request)

        assert response.status_code == 400

    def test_requester_order_id_is_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ChangeOrderStatusUsecase(repo_order=repo_order, repo_user=repo_user)
        controller = ChangeOrderStatusController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "new_status": STATUS.REFUSED.value
        })

        response = controller(request)

        assert response.status_code == 400

    def test_requester_new_status_is_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ChangeOrderStatusUsecase(repo_order=repo_order, repo_user=repo_user)
        controller = ChangeOrderStatusController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "new_status": STATUS.REFUSED.value
        })

        response = controller(request)

        assert response.status_code == 400
