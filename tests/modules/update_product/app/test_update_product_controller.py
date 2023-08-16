import datetime

import pytest

from src.modules.update_product.app.update_product_controller import UpdateProductController
from src.modules.update_product.app.update_product_usecase import UpdateProductUsecase
from src.shared.domain.entities.product import Product
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.external_interfaces.http_codes import Forbidden
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

repo_user = UserRepositoryMock()
user_id_with_permission = repo_user.users_list[0].user_id


class Test_UpdateProductController:
    def test_update_product_controller(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={"requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_available': True,
                'new_price': 15.0,
                'new_name': 'Nome Atualizado',
                'new_description': 'Descrição Atualizada',
                'new_prepare_time': 20,
                'new_meal_type': 'DRINKS',
                'new_photo': 'new_photo',

            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["available"] == True
        assert response.body["product"]["price"] == 15.0
        assert response.body["product"]["name"] == "Nome Atualizado"
        assert response.body["product"]["description"] == "Descrição Atualizada"
        assert response.body["product"]["prepare_time"] == 20
        assert response.body["product"]["meal_type"] == "DRINKS"
        assert response.body["product"]["photo"] == "new_photo"
        assert response.body["product"]["last_update"] == int(datetime.datetime.now().timestamp())
        assert response.body["message"] == "the product was updated"

    def test_update_only_product_name(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={"requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_name': 'Novo nome do produto',
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["name"] == "Novo nome do produto"
        assert response.body["message"] == "the product was updated"

    def test_update_product_with_nonexistent_user(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        user_withouth_permission = repo_user.users_list[-1]
        user_withouth_permission.role = ROLE.USER

        request = HttpRequest(
            body={"requester_user": {
                "sub": "um id que não existe",
                "name": user_withouth_permission.name,
                "email": user_withouth_permission.email,
                "custom:isMaua": True
            },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_available': True,
                'new_price': 15.0,
                'new_name': 'Nome Atualizado',
                'new_description': 'Descrição Atualizada',
                'new_prepare_time': 20,
                'new_meal_type': 'DRINKS',
                'new_photo': 'new_photo',

            }
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_update_product_without_permission(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        user_withouth_permission = repo_user.users_list[-1]
        user_withouth_permission.role = ROLE.USER

        request = HttpRequest(
            body={"requester_user": {
                "sub": user_withouth_permission.user_id,
                "name": user_withouth_permission.name,
                "email": user_withouth_permission.email,
                "custom:isMaua": True
            },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_available': True,
                'new_price': 15.0,
                'new_name': 'Nome Atualizado',
                'new_description': 'Descrição Atualizada',
                'new_prepare_time': 20,
                'new_meal_type': 'DRINKS',
                'new_photo': 'new_photo',

            }
        )

        response = controller(request=request)

        assert response.status_code == 403

    def test_update_product_controller_product_id_is_missing(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'restaurant': 'SOUZA_DE_ABREU',
                'new_available': True,
                'new_price': 15.0,
                'new_name': 'Nome Atualizado',
                'new_description': 'Descrição Atualizada',
                'new_prepare_time': 20,
                'new_meal_type': 'DRINKS',
                'new_photo': 'new_photo'
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field product_id is missing"

    def test_update_product_controller_restaurant_is_missing(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email, 'custom:isMaua': True},
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'new_available': True,
                'new_price': 15.0,
                'new_name': 'Nome Atualizado',
                'new_description': 'Descrição Atualizada',
                'new_prepare_time': 20,
                'new_meal_type': 'DRINKS',
                'new_photo': 'new_photo'
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_update_product_controller_restaurant_not_valid(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={'requester_user': {'sub': repo_user.users_list[0].user_id, 'name': repo_user.users_list[0].name,
                                     'email': repo_user.users_list[0].email, 'custom:isMaua': True},
                  'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                  'restaurant': 'Souzinha',
                  'new_available': True,
                  'new_price': 15.0,
                  'new_name': 'Nome Atualizado',
                  'new_description': 'Descrição Atualizada',
                  'new_prepare_time': 20,
                  'new_meal_type': 'DRINKS',
                  'new_photo': 'new_photo'
                  }
        )

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for restaurant"

    def test_update_only_product_description(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={"requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_description': 'minha nova descrição!!'
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["description"] == "minha nova descrição!!"
        assert response.body["message"] == "the product was updated"

    def test_update_product_controller_meal_type_not_valid(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_available': True,
                'new_price': 15.0,
                'new_name': 'Nome Atualizado',
                'new_description': 'Descrição Atualizada',
                'new_prepare_time': 20,
                'new_meal_type': 'SARGADIN',
                'new_photo': 'new_photo'
            }
        )

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for new_meal_type"

    def test_update_price_with_integer_value(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_price': 15,
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["price"] == 15
        assert response.body["message"] == "the product was updated"

    def test_update_prepare_time_with_none_value(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_prepare_time': None
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["prepare_time"] == None
        assert response.body["message"] == "the product was updated"

    def test_update_prepare_time_with_integer_value(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_prepare_time': 42
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["prepare_time"] == 42
        assert response.body["message"] == "the product was updated"

    def test_update_prepare_time_with_float_value(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_prepare_time': 42.00
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["prepare_time"] == 42
        assert response.body["message"] == "the product was updated"

    def test_update_prepare_time_with_negative_value(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_prepare_time': -42.00
            }
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_update_with_negative_price(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_price': -42
            }
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_update_product_with_too_high_price(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_price': Product.MAXIMUM_PRICE+1
            }
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_update_with_none_price(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        product_updated = repo_prod.products[0]

        price_before = product_updated.price

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': repo_prod.products[0].product_id,
                'restaurant': repo_prod.products[0].restaurant.value,
                'new_price': None
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert product_updated.price is not None
        assert product_updated.price == price_before

    def test_update_description_with_none_value(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_description': None
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["description"] == None
        assert response.body["message"] == "the product was updated"


    def test_update_description_with_void_string(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_description': ''
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["description"] == ''
        assert response.body["message"] == "the product was updated"

    def test_update_description_with_a_value(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': repo_user.users_list[0].user_id,
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_description': 'Minha nova descricao'
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["description"] == 'Minha nova descricao'
        assert response.body["message"] == "the product was updated"

    def test_update_product_unregistered_user(self):
        repo_prod = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo_prod, repo_user=repo_user)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    'sub': "id",
                    'name': repo_user.users_list[0].name,
                    'email': repo_user.users_list[0].email,
                    'custom:isMaua': True
                },
                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                'restaurant': 'SOUZA_DE_ABREU',
                'new_available': True,
                'new_price': 15.0,
                'new_name': 'Nome Atualizado',
                'new_description': 'Descrição Atualizada',
                'new_prepare_time': 20,
                'new_meal_type': 'DRINKS',
                'new_photo': 'new_photo'
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "That user is not registered"
