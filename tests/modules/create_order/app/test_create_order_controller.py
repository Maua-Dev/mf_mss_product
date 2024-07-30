import datetime
from src.modules.create_order.app.create_order_controller import CreateOrderController
from src.modules.create_order.app.create_order_usecase import CreateOrderUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from freezegun import freeze_time

class Test_CreateOrderController:
    def test_create_order_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order, repo_user, repo_product)
        controller = CreateOrderController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "products": [{
                "product_name": repo_product.products[0].name,
                "product_id": repo_product.products[0].product_id,
                "quantity": 1,
                "observation": "Sem tomate"
            }],
            "restaurant": repo_product.products[0].restaurant.value,
        })

        response = controller(request)

        assert response.status_code == 201
        assert response.body["message"] == "the order was created"
        assert response.body["order"]["user_name"] == "Lucas Duez"
        assert response.body["order"]["user_id"] == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert response.body["order"]["products"][0]["product_name"] == "X-Salada"
        assert response.body["order"]["products"][0]["product_id"] == "8a705b91-c9e9-4353-a755-07f13afafed3"
        assert response.body["order"]["products"][0]["quantity"] == 1
        assert response.body["order"]["restaurant"] == "SOUZA_DE_ABREU"
        assert response.body["order"]["order_status"] == "PENDING"
        assert response.body["order"]["total_price"] == 19.00
        assert response.body["order"]["action"] == "NEW"

    @freeze_time("2023-08-30")
    def test_create_order_controller_several_orders(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order, repo_user, repo_product)
        controller = CreateOrderController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "products": [{
                "product_name": repo_product.products[0].name,
                "product_id": repo_product.products[0].product_id,
                "quantity": 1,
                "observation": "Sem tomate no X-Salada"
            },
            {
                "product_name": repo_product.products[1].name,
                "product_id": repo_product.products[1].product_id,
                "quantity": 1,
                "observation": "Sem tomate no X-Salada"
            },
            {
                "product_name": repo_product.products[2].name,
                "product_id": repo_product.products[2].product_id,
                "quantity": 3,
                "observation": "Sem tomate no X-Salada"
            }],
            "restaurant": repo_product.products[0].restaurant.value,
        })

        response = controller(request)

        assert response.status_code == 201
        assert response.body["message"] == "the order was created"
        assert response.body["order"]["user_name"] == "Lucas Duez"
        assert response.body["order"]["user_id"] == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert response.body["order"]["products"][0]["product_name"] == "X-Salada"
        assert response.body["order"]["products"][1]["product_id"] == "cf8b01e6-ea9f-40fc-8344-d77d61761fbe"
        assert response.body["order"]["products"][2]["quantity"] == 3
        assert response.body["order"]["restaurant"] == "SOUZA_DE_ABREU"
        assert response.body["order"]["creation_time_milliseconds"] == int(datetime.datetime.now().timestamp() * 1000)
        assert response.body["order"]["order_status"] == "PENDING"
        assert response.body["order"]["total_price"] == 66.00
        assert response.body["order"]["action"] == "NEW"

    def test_create_order_controller_requester_user_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order, repo_user, repo_product)
        controller = CreateOrderController(usecase)

        request = HttpRequest(body={
            "products": [{
                "product_name": repo_product.products[0].name,
                "product_id": repo_product.products[0].product_id,
                "quantity": 1,
                "observation": "Sem tomate"
            }],
            "restaurant": repo_product.products[0].restaurant.value,
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_create_order_controller_products_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order, repo_user, repo_product)
        controller = CreateOrderController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "restaurant": repo_product.products[0].restaurant.value,
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field products is missing"

    def test_create_order_controller_restaurant_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order, repo_user, repo_product)
        controller = CreateOrderController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "products": [{
                "product_name": repo_product.products[0].name,
                "product_id": repo_product.products[0].product_id,
                "quantity": 1,
                "observation": "Sem tomate"
            }],
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_create_order_controller_restaurant_not_found(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order, repo_user, repo_product)
        controller = CreateOrderController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "products": [{
                "product_name": repo_product.products[0].name,
                "product_id": repo_product.products[0].product_id,
                "quantity": 1,
                "observation": "Sem tomate"
            }],
            "restaurant": "Tech Food?",
        })

        response = controller(request)

        assert response.status_code == 404
        assert response.body == "Field 'Tech Food?' is not a restaurant"

    