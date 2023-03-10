from src.shared.domain.entities.product import Product
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class Test_ProductRepositoryMock():
        
    def test_get_all_products_group_by_restaurant(self):
        repo = ProductRepositoryMock()
        products = repo.get_all_products_group_by_restaurant()
        
        assert list(products.keys()) == [restaurant for restaurant in RESTAURANT]
        
        length_products = 0
        for list_of_products in products.values():
            for product in list_of_products:
                length_products += 1      
        assert length_products == len(repo.products)


    def test_delete_product(self):
        repo = ProductRepositoryMock()
        lenBefore = len(repo.products)
        product = repo.delete_product(product_id="6d6b38c0-927d-4c43-93b7-b33ea9278cba", restaurant=RESTAURANT.SOUZA_DE_ABREU)

        assert product.product_id == "6d6b38c0-927d-4c43-93b7-b33ea9278cba"
        assert product.restaurant.value == "SOUZA_DE_ABREU"
        assert len(repo.products) == lenBefore - 1

    def test_create_product(self):
        repo = ProductRepositoryMock()
        len_before = len(repo.products)
        product = repo.create_product(Product(
            available=True, 
            price=14.0, 
            name='Lanche Mortadela', 
            description='Mortadela', 
            prepare_time=20, 
            meal_type=MEAL_TYPE.SANDWICHES, 
            photo='https://avatars.githubusercontent.com/u/30812461?v=4', 
            product_id="1825f29d-78fe-4f0d-aa88-b8d44a9a0e1f", 
            last_update=1674835337393, 
            restaurant=RESTAURANT.SOUZA_DE_ABREU
        ))

        assert product.available == True
        assert product.price == 14.0
        assert product.name == 'Lanche Mortadela'
        assert product.description == 'Mortadela'
        assert product.prepare_time == 20
        assert product.meal_type == MEAL_TYPE.SANDWICHES
        assert product.photo == 'https://avatars.githubusercontent.com/u/30812461?v=4'
        assert product.product_id == "1825f29d-78fe-4f0d-aa88-b8d44a9a0e1f"
        assert product.last_update == 1674835337393
        assert product.restaurant == RESTAURANT.SOUZA_DE_ABREU

        assert type(product) == Product
        assert len(repo.products) == len_before + 1
        
