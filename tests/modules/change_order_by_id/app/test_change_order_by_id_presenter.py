import json

from src.modules.change_order_by_id.app.change_order_by_id_presenter import lambda_handler
from src.modules.change_order_by_id.app.change_order_by_id_usecase import ChangeOrderByIdUsecase
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_presenter_sockets_tests


class Test_ChangeOrderByIdPresenter:

    def test_change_order_products(self):
        user_repo = UserRepositoryMock().users_list

        event = get_event_for_presenter_sockets_tests(
            claims={
                "sub": user_repo[2].user_id,
                "name": user_repo[2].name,
                "email": user_repo[2].email,
                "custom:isMaua": True
            },
            body={
                "order_id": "8309d903-55ce-4299-9c70-13fa2e03bcdc",
                "new_products": [
                {
                    "product_name": "Cimento (400mL)",
                    "product_id": "4081a83a-516f-442c-85e2-b54bfb192e55",
                    "quantity": 5,
                    "observation": "Bem observado!"}
                ]
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 200
        assert json.loads(response["body"])["message"] == "the order was updated"
        assert json.loads(response["body"])["order"]["products"] == [
                {
                    "product_name": "Cimento (400mL)",
                    "product_id": "4081a83a-516f-442c-85e2-b54bfb192e55",
                    "quantity": 5,
                    "observation": "Bem observado!"}
                ]

    def test_order_does_not_exist(self):
        user_repo = UserRepositoryMock().users_list

        event = get_event_for_presenter_sockets_tests(
            claims={
                "sub": user_repo[2].user_id,
                "name": user_repo[2].name,
                "email": user_repo[2].email,
                "custom:isMaua": True
            },
            body={
                "order_id": "um id que não existe",
                "new_products": [
                {
                    "product_name": "Cimento (400mL)",
                    "product_id": "4081a83a-516f-442c-85e2-b54bfb192e55",
                    "quantity": 5,
                    "observation": "Bem observado!"}
                ]
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 404

    def test_user_does_not_exist(self):
        user_repo = UserRepositoryMock().users_list

        event = get_event_for_presenter_sockets_tests(
            claims={
                "sub": "um id inexistente",
                "name": user_repo[2].name,
                "email": user_repo[2].email,
                "custom:isMaua": True
            },
            body={
                "order_id": "8309d903-55ce-4299-9c70-13fa2e03bcdc",
                "new_products": [
                {
                    "product_name": "Cimento (400mL)",
                    "product_id": "4081a83a-516f-442c-85e2-b54bfb192e55",
                    "quantity": 5,
                    "observation": "Bem observado!"}
                ]
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 400

    def test_products_list_cant_be_empty(self):
        user_repo = UserRepositoryMock().users_list

        event = get_event_for_presenter_sockets_tests(
            claims={
                "sub": user_repo[2].user_id,
                "name": user_repo[2].name,
                "email": user_repo[2].email,
                "custom:isMaua": True
            },
            body={
                "order_id": "8309d903-55ce-4299-9c70-13fa2e03bcdc",
                "new_products": []
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 403
