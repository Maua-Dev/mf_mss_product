from src.modules.get_product.app.get_product_controller import GetProductController
from src.modules.get_product.app.get_product_usecase import GetProductUsecase
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_GetProductController:
    def test_get_product_controller(self):

        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)
        controller = GetProductController(usecase)
        request = HttpRequest(query_params={'product_id': repo.products[0].product_id,'restaurant': repo.products[0].restaurant.value})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['product']['available'] == repo.products[0].available
        assert response.body['product']['price'] == repo.products[0].price
        assert response.body['product']['name'] == repo.products[0].name
        assert response.body['product']['description'] == repo.products[0].description
        assert response.body['product']['prepare_time'] == repo.products[0].prepare_time
        assert response.body['product']['meal_type'] == repo.products[0].meal_type.value
        assert response.body['product']['photo'] == repo.products[0].photo
        assert response.body['product']['product_id'] == repo.products[0].product_id
        assert response.body['product']['last_update'] == repo.products[0].last_update
        assert response.body['product']['restaurant'] == repo.products[0].restaurant.value
        assert response.body['message'] == "the product was retrieved"

    def test_get_product_controller_missing_product_id(self):

        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)
        controller = GetProductController(usecase)
        request = HttpRequest(query_params={'restaurant': repo.products[0].restaurant})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field product_id is missing'

    def test_get_product_controller_missing_restaurant(self):

        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)
        controller = GetProductController(usecase)
        request = HttpRequest(query_params={'product_id': repo.products[0].product_id})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field restaurant is missing'

    def test_get_product_controller_invalid_restaurant(self):

        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)
        controller = GetProductController(usecase)
        request = HttpRequest(query_params={'product_id': repo.products[0].product_id, "restaurant": "CANTINA_DO_BRANCAS"})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is not valid"

    def test_get_product_controller_invalid_product_id(self):

        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)
        controller = GetProductController(usecase)
        request = HttpRequest(query_params={'product_id': "2", "restaurant": repo.products[0].restaurant.value})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field product_id is not valid"

    def test_get_product_controller_product_not_found(self):

        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)
        controller = GetProductController(usecase)
        request = HttpRequest(query_params={'product_id':"00000000-0000-0000-0000-000000000000", "restaurant": repo.products[0].restaurant.value})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == "No items found for product"
