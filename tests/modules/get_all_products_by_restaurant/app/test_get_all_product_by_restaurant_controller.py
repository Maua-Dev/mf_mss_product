from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.modules.get_all_products_by_restaurant.app.get_all_product_by_restaurant_controller import GetAllProductByRestaurantController
from src.modules.get_all_products_by_restaurant.app.get_all_product_by_restaurant_usecase import GetAllProductsByRestaurantUsecase
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock

class Test_GetAllProductsByRestaurantController:
    def test_get_all_product_by_restaurant_controller(self):
        repo = ProductRepositoryMock()
        usecase = GetAllProductsByRestaurantUsecase(repo=repo)
        controller = GetAllProductByRestaurantController(usecase=usecase)

        request = HttpRequest(
            query_params={
                'restaurant': repo.products[0].restaurant.value
                }
            )
        
        response = controller(request=request)

        assert response.status_code == 200
        assert len(response.body['all_products']) == 93
        assert all([product['restaurant'] == repo.products[0].restaurant.value for product in response.body['all_products']])
        assert response.body['message'] == "the products were retrieved"

    def test_get_all_product_by_restaurant_controller_restaurant_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = GetAllProductsByRestaurantUsecase(repo=repo)
        controller = GetAllProductByRestaurantController(usecase=usecase)

        request = HttpRequest()

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_get_all_product_by_restaurant_controller_invalid_restaurant(self):
        repo = ProductRepositoryMock()
        usecase = GetAllProductsByRestaurantUsecase(repo=repo)
        controller = GetAllProductByRestaurantController(usecase=usecase)

        request = HttpRequest(
            query_params={
                'restaurant': 5
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is not valid"