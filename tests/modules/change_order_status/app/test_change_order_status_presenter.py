import json

from src.modules.change_order_status.app.change_order_status_presenter import lambda_handler
from src.shared.domain.enums.status_enum import STATUS
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_presenter_sockets_tests

repo_order = OrderRepositoryMock()


class Test_ChangeOrderStatusPresenter:
    def test_change_order_status(self):
        order = repo_order.orders[0]
        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": order.order_id,
                "new_status": STATUS.REFUSED.value
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 200
        assert json.loads(response["body"])["message"] == "the order status was updated"
        assert json.loads(response["body"])["order"]["status"] == "REFUSED"

    def test_presenter_order_id_none(self):
        order = repo_order.orders[0]
        event = get_event_for_presenter_sockets_tests(
            body={
                "new_status": STATUS.REFUSED.value
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 400

    def test_presenter_order_id_inexistent(self):
        order = repo_order.orders[0]
        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": "135ef881-1b1f-4f38-a662-8ff7156e6xxx",  # id que não existe
                "new_status": STATUS.REFUSED.value
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 404

    def test_new_status_is_none(self):
        order = repo_order.orders[0]
        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": order.order_id
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 400
