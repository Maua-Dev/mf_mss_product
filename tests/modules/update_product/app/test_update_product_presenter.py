import datetime
import json
from src.modules.update_product.app.update_product_presenter import lambda_handler
from src.shared.domain.entities.product import Product
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_test_presenter
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

user_repo = UserRepositoryMock()
user = user_repo.users_list[0]


class Test_UpdateProductPresenter:
    def test_update_product_presenter(self):
        event = get_event_for_test_presenter(
            body=
            {

                "product_id": "8a705b91-c9e9-4353-a755-07f13afafed3",
                "restaurant": "SOUZA_DE_ABREU",
                "new_available": "True",
                "new_price": 15.0,
                "new_name": "Nome Atualizado",
                "new_description": "Descrição Atualizada",
                "new_prepare_time": 20,
                "new_meal_type": "DRINKS",
                "new_photo": "new_photo"
            }
        )

        expected = {
            'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
            'restaurant': 'SOUZA_DE_ABREU',
            'available': True,
            'price': 15.0,
            'name': 'Nome Atualizado',
            'description': 'Descrição Atualizada',
            'prepare_time': 20,
            'meal_type': 'DRINKS',
            'photo': 'new_photo',
            'last_update': int(datetime.datetime.now().timestamp())
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 200
        assert json.loads(response["body"])['product'] == expected
        assert json.loads(response["body"])['message'] == "the product was updated"

    def test_update_product_presenter_product_id_is_missing(self):
        event = get_event_for_test_presenter(
            body=
            {
                "restaurant": "SOUZA_DE_ABREU",
                "new_available": "True",
                "new_price": 15.0,
                "new_name": "Nome Atualizado",
                "new_description": "Descrição Atualizada",
                "new_prepare_time": 20,
                "new_meal_type": "DRINKS",
                "new_photo": "new_photo"
            }
        )

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field product_id is missing"

    def test_update_product_presenter_restaurant_is_missing(self):
        event = get_event_for_test_presenter(
            body=
            {
                "product_id": "8a705b91-c9e9-4353-a755-07f13afafed3",
                "new_available": "True",
                "new_price": 15.0,
                "new_name": "Nome Atualizado",
                "new_description": "Descrição Atualizada",
                "new_prepare_time": 20,
                "new_meal_type": "DRINKS",
                "new_photo": "new_photo"
            }
        )

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field restaurant is missing"

    def test_update_product_presenter_restaurant_not_found(self):
        event = get_event_for_test_presenter(
            body=
            {
                "product_id": "8a705b91-c9e9-4353-a755-07f13afafed3",
                "restaurant": "SOUZINHA",
                "new_available": "True",
                "new_price": 15.0,
                "new_name": "Nome Atualizado",
                "new_description": "Descrição Atualizada",
                "new_prepare_time": 20,
                "new_meal_type": "DRINKS",
                "new_photo": "new_photo"}
        )
        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "No items found for restaurant"

    def test_update_product_presenter_meal_type_not_found(self):
        event = get_event_for_test_presenter(body=
        {
            "product_id": "8a705b91-c9e9-4353-a755-07f13afafed3",
            "restaurant": "SOUZA_DE_ABREU",
            "new_available": "True",
            "new_price": 15.0,
            "new_name": "Nome Atualizado",
            "new_description": "Descrição Atualizada",
            "new_prepare_time": 20,
            "new_meal_type": "BEBIDINHAS",
            "new_photo": "new_photo"
        }
        )

        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "No items found for new_meal_type"

    def test_update_only_name_and_photo(self):
        product_repo = ProductRepositoryMock()
        product_old_values = Product(
            available=product_repo.products[3].available,
            product_id=product_repo.products[3].product_id,
            restaurant=product_repo.products[3].restaurant,
            price=product_repo.products[3].price,
            name=product_repo.products[3].name,
            description=product_repo.products[3].description,
            meal_type=product_repo.products[3].meal_type,
            photo=product_repo.products[3].photo,
            prepare_time=product_repo.products[3].prepare_time,
            last_update=product_repo.products[3].last_update
        )

        event = get_event_for_test_presenter({
            "product_id": product_old_values.product_id,
            "restaurant": product_old_values.restaurant.value,
            "new_name": "Nome Atualizado",
            "new_photo": "olha que bela foto"})

        expected = {
            'product_id': product_old_values.product_id,
            'restaurant': product_old_values.restaurant.value,
            'available': product_old_values.available,
            'price': product_old_values.price,
            'name': 'Nome Atualizado',
            'description': product_old_values.description,
            'prepare_time': product_old_values.prepare_time,
            'meal_type': product_old_values.meal_type.value,
            'photo': 'olha que bela foto',
            'last_update': int(datetime.datetime.now().timestamp())
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 200
        assert json.loads(response["body"])['product'] == expected
        assert json.loads(response["body"])['message'] == "the product was updated"


    def test_update_product_with_negative_prepare_time(self):
        event = get_event_for_test_presenter(
            body={
                "product_id": "8a705b91-c9e9-4353-a755-07f13afafed3",
                "restaurant": "SOUZA_DE_ABREU",
                "new_prepare_time": -20,
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 400
