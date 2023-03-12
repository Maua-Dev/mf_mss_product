from src.modules.get_product.app.get_product_controller import GetProductController
from src.modules.get_product.app.get_product_usecase import GetProductUsecase
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_GetProductController:
    def test_get_product_controller(self):

        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)
        controller = GetProductController(usecase)
        request = HttpRequest(query_params={'available': repo.products[0].available, 'price': repo.products[0].price, 'name': repo.products[0].name, 'description': repo.products[0].description, 'prepare_time': repo.products[0].prepare_time, 'meal_type': repo.products[0].meal_type.value, 'photo': repo.products[0].photo, 'product_id': repo.products[0].product_id, 'last_update': repo.products[0].last_update, 'restaurant': repo.products[0].restaurant.value  })

        response = controller(request)

        assert response.status_code == 200
        assert response.body['available'] == repo.products[0].available
        assert response.body['price'] == repo.products[0].price
        assert response.body['name'] == repo.products[0].name
        assert response.body['description'] == repo.products[0].description
        assert response.body['prepare_time'] == repo.products[0].prepare_time
        assert response.body['meal_type'] == repo.products[0].meal_type.value
        assert response.body['photo'] == repo.products[0].photo
        assert response.body['product_id'] == repo.products[0].product_id
        assert response.body['last_update'] == repo.products[0].last_update
        assert response.body['restaurant'] == repo.products[0].restaurant.value
        assert response.body['message'] == "the product was retrieved"

    def test_get_product_controller_missing_product_id(self):

        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)
        controller = GetProductController(usecase)
        request = HttpRequest(query_params={'available': repo.products[0].available, 'price': repo.products[0].price, 'name': repo.products[0].name, 'description': repo.products[0].description, 'prepare_time': repo.products[0].prepare_time, 'meal_type': repo.products[0].meal_type.value, 'photo': repo.products[0].photo, 'last_update': repo.products[0].last_update, 'restaurant': repo.products[0].restaurant.value  })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: Field product_id is missing'


    