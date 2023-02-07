import pytest
from src.modules.create_product.app.create_product_controller import CreateProductController
from src.modules.create_product.app.create_product_usecase import CreateProductUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class Test_CreteProductController:
    def test_create_product_controller(self):

        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })

        response = controller(request=request)
        assert response.status_code == 201
        assert response.body["message"] == "the product was created"
        assert response.body["product"]["available"] == True
        assert response.body["product"]["price"] == 14.0
        assert response.body["product"]["name"] == "Lanche de Mortadela"
        assert response.body["product"]["description"] == "Mortadela"
        assert response.body["product"]["meal_type"] == "SANDWICHES"
        assert response.body["product"]["photo"] == "https://avatars.githubusercontent.com/u/30812461?v=4"
        assert response.body["product"]["product_id"] == 0
        assert response.body["product"]["last_update"] == 1674835337393 
        assert response.body["product"]["restaurant"] == "SOUZA_DE_ABREU"
        assert response.body["product"]["prepareTime"] == 20

    def test_create_product_controller_available_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "price":14.0,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })
        
        
        response = controller(request=request)

        assert response.status_code == 400
    
    def test_create_product_controller_price_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })
        
        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_controller_name_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })
        
        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_controller_description_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "name":"Lanche de Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })
        
        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_controller_meal_type_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })
        
        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_controller_photo_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })
        
        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_controller_product_id_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })
        
        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_controller_last_update_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "restaurant":repo.products[0].restaurant.value,
            "prepareTime":20
        })
        
        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_controller_restaurant_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "prepareTime":20
        })
        
        response = controller(request=request)

        assert response.status_code == 400

    def test_create_product_controller_prepare_time_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        controller = CreateProductController(usecase=usecase)
        request = HttpRequest(body={
            "available":True,
            "price":14.0,
            "name":"Lanche de Mortadela",
            "description":"Mortadela",
            "meal_type":repo.products[0].meal_type.value,
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":repo.products[0].product_id,
            "last_update":1674835337393,
            "restaurant":repo.products[0].restaurant.value
        })
        
        response = controller(request=request)

        assert response.status_code == 400