from src.modules.delete_product.app.delete_product_controller import DeleteProductsByRestaurantController
from src.modules.delete_product.app.delete_product_usecase import DeleteProductsByRestaurantUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_DeleteProductsByRestaurantController:
    def test_delete_products_by_restaurant_controller(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductsByRestaurantUsecase(repo=repo)
        controller = DeleteProductsByRestaurantController(usecase=usecase)

        request = HttpRequest(
            body={
                "product_id": repo.products[0].product_id,
                "restaurant": repo.products[0].restaurant.value
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['product']['product_id'] == 0
        assert response.body['product']['restaurant'] == "SOUZA_DE_ABREU"
        assert response.body['message'] == "the product was deleted"
        
    def test_delete_products_by_restaurant_product_id_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductsByRestaurantUsecase(repo=repo)
        controller = DeleteProductsByRestaurantController(usecase=usecase)
        
        request = HttpRequest(
            body={
                "restaurant": repo.products[0].restaurant.value
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field product_id is missing"

    def test_delete_products_by_restaurant_restaurant_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductsByRestaurantUsecase(repo=repo)
        controller = DeleteProductsByRestaurantController(usecase=usecase)
        
        request = HttpRequest(
            body={
                "product_id": repo.products[0].product_id
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_delete_products_by_restaurant_not_found(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductsByRestaurantUsecase(repo=repo)
        controller = DeleteProductsByRestaurantController(usecase=usecase)
        
        request = HttpRequest(
            body={
                "product_id": repo.products[0].product_id,
                "restaurant": "Molas"
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is not valid"