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
        
    def test_get_all_products_group_by_restaurant(self):
        repo = ProductRepositoryMock()
        products = repo.get_all_products_group_by_restaurant()
        
        assert list(products.keys()) == [restaurant for restaurant in RESTAURANT]
        
        lenght_products = 0
        for list_of_products in products.values():
            for product in list_of_products:
                lenght_products += 1      
        assert lenght_products == len(repo.products)