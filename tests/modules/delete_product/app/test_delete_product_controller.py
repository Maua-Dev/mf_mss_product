from src.modules.delete_product.app.delete_product_controller import DeleteProductController
from src.modules.delete_product.app.delete_product_usecase import DeleteProductUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_DeleteProductController:
    def test_delete_product_controller(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductUsecase(repo=repo)
        controller = DeleteProductController(usecase=usecase)

        request = HttpRequest(
            body={
                "product_id": repo.products[0].product_id,
                "restaurant": repo.products[0].restaurant.value
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['product']['product_id'] == "8a705b91-c9e9-4353-a755-07f13afafed3"
        assert response.body['product']['restaurant'] == "SOUZA_DE_ABREU"
        assert response.body['message'] == "the product was deleted"
        
    def test_delete_product_product_id_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductUsecase(repo=repo)
        controller = DeleteProductController(usecase=usecase)
        
        request = HttpRequest(
            body={
                "restaurant": repo.products[0].restaurant.value
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field product_id is missing"

    def test_delete_product_restaurant_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductUsecase(repo=repo)
        controller = DeleteProductController(usecase=usecase)
        
        request = HttpRequest(
            body={
                "product_id": repo.products[0].product_id
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_delete_product_restaurant_not_valid(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductUsecase(repo=repo)
        controller = DeleteProductController(usecase=usecase)
        
        request = HttpRequest(
            body={
                "product_id": repo.products[0].product_id,
                "restaurant": "Molas"
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is not valid"