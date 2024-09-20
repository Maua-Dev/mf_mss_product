import json
from src.modules.delete_product.app.delete_product_presenter import lambda_handler
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_test_presenter_no_socket


class Test_DeleteProductPresenter:
    def test_delete_product_presenter(self):
        event = get_event_for_test_presenter_no_socket(
            body={
                "product_id": "2f9ad2af-a751-4adf-81c4-50e6a9b06c8b",
                "restaurant": "SOUZA_DE_ABREU",
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 200
        assert json.loads(response["body"])['message'] == "the product was deleted"

    def test_delete_product_presenter_product_id_is_missing(self):
        event = get_event_for_test_presenter_no_socket(
            body={
                "restaurant": "HORA_H",
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field product_id is missing"

    def test_delete_product_presenter_restaurant_is_missing(self):
        event = get_event_for_test_presenter_no_socket(
            body={
                "product_id": "71ede2ce-31c6-4b22-bab5-da2175654308",
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field restaurant is missing"

    def test_delete_product_presenter_restaurant_not_valid(self):
        event = get_event_for_test_presenter_no_socket(
            body={
                "product_id": "71ede2ce-31c6-4b22-bab5-da2175654308",
                "restaurant": "DAHORA_H",
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field restaurant is not valid"
