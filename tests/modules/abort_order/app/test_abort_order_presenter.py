import json

from src.modules.abort_order.app.abort_order_presenter import lambda_handler
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_presenter_sockets_tests


repo_order = OrderRepositoryMock()


class Test_AbortOrderPresenter:
    def test_abort_order(self):
        order = repo_order.orders[0]
        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": order.order_id,
                "aborted_reason": "Desisti da compra!"
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 200
        assert json.loads(response["body"])["message"] == "the order was aborted"
        assert json.loads(response["body"])["order"]["aborted_reason"] == "Desisti da compra!"

    def test_presenter_order_id_none(self):
        order = repo_order.orders[0]
        event = get_event_for_presenter_sockets_tests(
            body={
                "aborted_reason": "Não tinha o produto"
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 400

    def test_presenter_order_id_inexistent(self):
        order = repo_order.orders[0]
        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": "135ef881-1b1f-4f38-a662-8ff7156e6xxx",  # id que não existe
                "aborted_reason": "Desisti da compra!"
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 404

    def test_new_aborted_reason_is_none(self):
        order = repo_order.orders[0]
        event = get_event_for_presenter_sockets_tests(
            body={
                "order_id": order.order_id
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 400



