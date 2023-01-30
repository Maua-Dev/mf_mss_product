from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.modules.get_all_products_by_restaurant.app.get_all_product_by_restaurant_usecase import GetAllProductsByRestaurantUsecase
from src.shared.domain.entities.product import Product
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock



class Test_GetAllProductByRestaurant:
    def test_get_all_product_by_restarant(self):
        repo = ProductRepositoryMock()
        usecase = GetAllProductsByRestaurantUsecase(repo=repo)

        product_rest1 = usecase(restaurant=RESTAURANT.SOUZA_DE_ABREU)
        product_rest2 = usecase(restaurant=RESTAURANT.RESTAURANTE_DO_H)

        assert all([product.restaurant == RESTAURANT.SOUZA_DE_ABREU for product in product_rest1])
        assert all([product.restaurant == RESTAURANT.RESTAURANTE_DO_H for product in product_rest2])
         