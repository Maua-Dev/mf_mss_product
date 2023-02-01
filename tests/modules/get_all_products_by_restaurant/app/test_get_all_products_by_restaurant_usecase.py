from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.modules.get_all_products_by_restaurant.app.get_all_product_by_restaurant_usecase import GetAllProductsByRestaurantUsecase
from src.shared.domain.entities.product import Product
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock



class Test_GetAllProductByRestaurantUsecase:
    def test_get_all_product_by_restaurant_usecase_souza_de_abreu(self):
        repo = ProductRepositoryMock()
        usecase = GetAllProductsByRestaurantUsecase(repo=repo)

        product_souza_de_abreu = usecase(restaurant=RESTAURANT.SOUZA_DE_ABREU)

        assert all([product.restaurant == RESTAURANT.SOUZA_DE_ABREU for product in product_souza_de_abreu])

    def test_get_all_product_by_restaurant_usecase_restaurante_do_h(self):
        repo = ProductRepositoryMock()
        usecase = GetAllProductsByRestaurantUsecase(repo=repo)

        product_restaurante_do_h = usecase(restaurant=RESTAURANT.RESTAURANTE_DO_H)

        assert all([product.restaurant == RESTAURANT.RESTAURANTE_DO_H for product in product_restaurante_do_h])