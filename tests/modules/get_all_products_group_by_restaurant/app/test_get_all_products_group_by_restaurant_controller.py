from src.modules.get_all_products_group_by_restaurant.app.get_all_products_group_by_restaurant_controller import GetAllProductGroupByRestaurantController
from src.modules.get_all_products_group_by_restaurant.app.get_all_products_group_by_restaurant_usecase import GetAllProductsGroupByRestaurantUsecase
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_GetAllProductsGroupByRestaurantController:
    def test_get_all_products_group_by_restaurant_controller(self):
        repo = ProductRepositoryMock()
        usecase = GetAllProductsGroupByRestaurantUsecase(repo=repo)
        controller = GetAllProductGroupByRestaurantController(usecase=usecase)
        
        response = controller(request={})
        
        assert response.status_code == 200
        assert response.data["message"] == "the products were retrieved"