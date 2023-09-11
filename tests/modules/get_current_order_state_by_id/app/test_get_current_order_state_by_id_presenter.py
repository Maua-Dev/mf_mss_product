import json

from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_presenter import lambda_handler
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_presenter_sockets_tests


class Test_GetCurrentOrderStateByIdPresenter:
    def test_get_order_state(self):
        repo = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        order = repo.orders[0]
        user = repo_user.get_user_by_id(order.user_id)

        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": order.order_id
            },
            claims={
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            }
        )

        response = lambda_handler(event, None)

        expected_body = {
            "order": {
                "order_id": order.order_id,
                "order_status": order.status.value
            },
            "message": "the order status object was retrieved"
        }

        assert response["statusCode"] == 200
        assert json.loads(response["body"]) == expected_body

    def test_user_not_order_owner(self):
        repo = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        order = repo.orders[0]
        user = repo_user.users_list[-4]

        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": order.order_id
            },
            claims={
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 403

    def test_user_not_registered(self):
        repo = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        order = repo.orders[0]
        user = repo_user.users_list[0]

        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": order.order_id
            },
            claims={
                "sub": "um id que não existe",
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
