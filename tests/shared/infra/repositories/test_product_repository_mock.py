from src.shared.domain.entities.product import Product
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock

class Test_ProductRepositoryMock():
    def test_get_all_products_by_restaurant_biba(self):
        repo = ProductRepositoryMock()
        products = repo.get_all_products_by_restaurant(restaurant=RESTAURANT.SOUZA_DE_ABREU)
        
        assert len(products) > 0
        assert all([type(product) == Product for product in products])
        assert all([product.restaurant == RESTAURANT.SOUZA_DE_ABREU for product in products])
        
    def test_get_all_products_by_restaurant_h(self):
        repo = ProductRepositoryMock()
        products = repo.get_all_products_by_restaurant(restaurant=RESTAURANT.RESTAURANTE_DO_H)
        
        assert len(products) > 0
        assert all([type(product) == Product for product in products])
        assert all([product.restaurant == RESTAURANT.RESTAURANTE_DO_H for product in products])
        
    def test_get_all_products_by_restaurant_not_found(self):
        repo = ProductRepositoryMock()
        products = repo.get_all_products_by_restaurant(restaurant="Eh o Rodas")
        
        assert products == []
        