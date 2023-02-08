from src.shared.domain.entities.product import Product
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock

class Test_ProductRepositoryMock():
        
    def test_get_all_products_group_by_restaurant(self):
        repo = ProductRepositoryMock()
        products = repo.get_all_products_group_by_restaurant()
        
        assert list(products.keys()) == [restaurant for restaurant in RESTAURANT]
        
        lenght_products = 0
        for list_of_products in products.values():
            for product in list_of_products:
                lenght_products += 1      
        assert lenght_products == len(repo.products)

    def test_delete_product(self):
        repo = ProductRepositoryMock()
        lenBefore = len(repo.products)
        product = repo.delete_product(product_id=0, restaurant=RESTAURANT.SOUZA_DE_ABREU)

        assert product.product_id == 0
        assert product.restaurant.value == "SOUZA_DE_ABREU"
        assert len(repo.products) == lenBefore - 1