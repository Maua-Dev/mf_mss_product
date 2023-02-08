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
        
        lenght_products = 0
        for list_of_products in products.values():
            for product in list_of_products:
                lenght_products += 1      
        assert lenght_products == len(repo.products)

    def test_create_product(self):
        repo = ProductRepositoryMock()
        len_before = len(repo.products)
        product = repo.create_product(Product(
            available=True, 
            price=14.0, 
            name='Lanche Mortadela', 
            description='Mortadela', 
            prepareTime=20, 
            meal_type=MEAL_TYPE.SANDWICHES, 
            photo='https://avatars.githubusercontent.com/u/30812461?v=4', 
            product_id=0, 
            last_update=1674835337393, 
            restaurant=RESTAURANT.SOUZA_DE_ABREU
        ))

        assert type(product) == Product
        assert len(repo.products) == len_before + 1
        