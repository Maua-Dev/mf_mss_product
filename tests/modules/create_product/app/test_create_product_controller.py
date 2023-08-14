import pytest

from src.modules.create_product.app.create_product_controller import CreateProductController
from src.modules.create_product.app.create_product_usecase import CreateProductUsecase
from src.shared.domain.entities.product import Product
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class Test_CreteProductController:
    def test_create_product_controller(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20}
        )

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body["message"] == "the product was created"
        assert response.body["product"]["available"] == True
        assert response.body["product"]["price"] == 14.0
        assert response.body["product"]["name"] == "Lanche de Mortadela"
        assert response.body["product"]["description"] == "Mortadela"
        assert response.body["product"]["meal_type"] == "SANDWICHES"
        assert response.body["product"]["photo"] == "https://avatars.githubusercontent.com/u/30812461?v=4"
        assert type(response.body["product"]["product_id"]) == str
        assert type(response.body["product"]["last_update"]) == int
        assert response.body["product"]["restaurant"] == "SOUZA_DE_ABREU"
        assert response.body["product"]["prepare_time"] == 20

    def test_create_product_controller_available_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20,
            "user_id": repo_user.users_list[0].user_id,

        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field available is missing"

    def test_create_product_controller_price_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field price is missing"

    def test_create_product_controller_name_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field name is missing"

    def test_create_product_controller_description_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field description is missing"

    def test_create_product_controller_meal_type_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field meal_type is missing"

    def test_create_product_controller_restaurant_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_create_product_controller_prepare_time_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field prepare_time is missing"

    def test_create_product_controller_invalid_meal_type(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": "INVALID_TYPE",
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

    def test_create_product_controller_meal_type_is_not_str(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": {},
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field meal_type is not valid"

    def test_create_product_controller_invalid_restaurant(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": "RESTAURANT[BANANA]",
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is not valid"

    def test_create_product_controller_restaurant_is_not_str(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": 1,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is not valid"

    def test_create_product_controller_invalid_available(self):
        repo_product = ProductRepositoryMock()

        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": 2,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field available is not valid"

    def test_create_product_controller_invalid_price(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": "EH O RODAS",
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field price is not valid"

    def test_create_product_controller_invalid_name(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": [],
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field name is not valid"

    def test_create_product_controller_invalid_description(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": 696969,
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field description is not valid"

    def test_create_product_controller_invalid_photo(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": False,
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": repo_user.users_list[0].user_id,
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field photo is not valid"

    def test_create_product_controller_invalid_prepare_time(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": "EH O CRUDAS"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field prepare_time is not valid"

    def test_create_product_controller_unregistered_user(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": "id",
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 17.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20, "user_id": "id",
            "product_id": "22781c75-1a8a-42d5-be88-046ca81f7254"}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "That user is not registered"

    def test_create_product_with_negative_prepare_time(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": 14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": -20}
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_with_negative_price(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": -14.0,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20}
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_with_none_price(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": None,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20}
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_create_a_product_with_a_high_price(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_product, repo_user)
        controller = CreateProductController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "available": True,
            "price": Product.MAXIMUM_PRICE+1,
            "name": "Lanche de Mortadela",
            "description": "Mortadela",
            "meal_type": repo_product.products[0].meal_type.value,
            "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
            "restaurant": repo_product.products[0].restaurant.value,
            "prepare_time": 20}
        )

        response = controller(request=request)

        assert response.status_code == 400
