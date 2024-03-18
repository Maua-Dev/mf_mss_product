from src.modules.change_order_by_id.app.change_order_by_id_controller import ChangeOrderByIdController
from src.modules.change_order_by_id.app.change_order_by_id_usecase import ChangeOrderByIdUsecase
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ChangeOrderByIdController:
    def test_update_products_list(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(order_repo, user_repo)
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": user_repo.users_list[2].user_id,
                "name": user_repo.users_list[2].name,
                "email": user_repo.users_list[2].email,
                "custom:isMaua": True
            },
            "order_id": "8309d903-55ce-4299-9c70-13fa2e03bcdc",
            "new_products": [
                {
                    "product_name": "Cimento (400mL)",
                    "product_id": "4081a83a-516f-442c-85e2-b54bfb192e55",
                    "quantity": 5}
            ]
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "the order was updated"

    def test_request_user_is_missing(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(order_repo, user_repo)
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "order_id": "8309d903-55ce-4299-9c70-13fa2e03bcdc",
            "new_products": [
                {
                    "product_name": "Cimento (400mL)",
                    "product_id": "4081a83a-516f-442c-85e2-b54bfb192e55",
                    "quantity": 5}
            ]
        })

        response = controller(request)

        assert response.status_code == 400

    def test_non_owner_user_cant_change_order(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(order_repo, user_repo)
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": user_repo.users_list[4].user_id,
                "name": user_repo.users_list[4].name,
                "email": user_repo.users_list[4].email,
                "custom:isMaua": True
            },
            "order_id": "8309d903-55ce-4299-9c70-13fa2e03bcdc",
            "new_products": [
                {
                    "product_name": "Cimento (400mL)",
                    "product_id": "4081a83a-516f-442c-85e2-b54bfb192e55",
                    "quantity": 5}
            ]
        })

        response = controller(request)

        assert response.status_code == 403

    def test_order_does_not_exist(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(order_repo, user_repo)
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": user_repo.users_list[4].user_id,
                "name": user_repo.users_list[4].name,
                "email": user_repo.users_list[4].email,
                "custom:isMaua": True
            },
            "order_id": "um id que não existe",
            "new_products": [
                {
                    "product_name": "Cimento (400mL)",
                    "product_id": "4081a83a-516f-442c-85e2-b54bfb192e55",
                    "quantity": 5}
            ]
        })

        response = controller(request)

        assert response.status_code == 404

    def test_products_list_cant_be_empty(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(order_repo, user_repo)
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": user_repo.users_list[2].user_id,
                "name": user_repo.users_list[2].name,
                "email": user_repo.users_list[2].email,
                "custom:isMaua": True
            },
            "order_id": "8309d903-55ce-4299-9c70-13fa2e03bcdc",
            "new_products": []
        })

        response = controller(request)

        assert response.status_code == 403