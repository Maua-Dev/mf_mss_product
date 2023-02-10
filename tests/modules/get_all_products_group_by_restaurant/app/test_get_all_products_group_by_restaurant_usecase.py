from src.modules.get_all_products_group_by_restaurant.app.get_all_products_group_by_restaurant_usecase import GetAllProductsGroupByRestaurantUsecase
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_GetAllProductsGroupByRestaurantUsecase:
    def test_get_all_products_group_by_restaurant_usecase(self):
        repo = ProductRepositoryMock()
        usecase = GetAllProductsGroupByRestaurantUsecase(repo=repo)
        products = usecase()
        
        assert list(products.keys()) == [restaurant for restaurant in RESTAURANT]
        
        length_products = 0
        for list_of_products in products.values():
            for product in list_of_products:
                length_products += 1      
        assert length_products == len(repo.products)