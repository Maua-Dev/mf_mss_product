from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_controller import \
    GetCurrentOrderStateByIdController
from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_usecase import \
    GetCurrentOrderStateByIdUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetCurrentOrderStateByIdController:
    def test_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetCurrentOrderStateByIdUsecase(user_repo=repo_user, order_repo=repo_order)
        controller = GetCurrentOrderStateByIdController(usecase)

        order = repo_order.orders[-1]
        user = repo_user.users_list[-1]
        order.user_id = user.user_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "order_id": order.order_id
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "the order status object was retrieved"

    def test_user_not_order_owner(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetCurrentOrderStateByIdUsecase(user_repo=repo_user, order_repo=repo_order)
        controller = GetCurrentOrderStateByIdController(usecase)

        order = repo_order.orders[-1]
        user = repo_user.users_list[-1]
        order.user_id = user.user_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "order_id": order.order_id
        })

        response = controller(request)

        assert response.status_code == 403

    def test_user_not_registered(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetCurrentOrderStateByIdUsecase(user_repo=repo_user, order_repo=repo_order)
        controller = GetCurrentOrderStateByIdController(usecase)

        order = repo_order.orders[-1]
        user = repo_user.users_list[-1]

        request = HttpRequest(body={
            "requester_user": {
                "sub": "um id que não existe",
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "order_id": order.order_id
        })

        response = controller(request)

        assert response.status_code == 400
