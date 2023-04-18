import datetime
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
        product = repo.delete_product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU)

        assert product.product_id == "8a705b91-c9e9-4353-a755-07f13afafed3"
        assert product.restaurant.value == "SOUZA_DE_ABREU"
        assert len(repo.products) == lenBefore - 1

    def test_create_product(self):
        repo = ProductRepositoryMock()
        len_before = len(repo.products)
        product = repo.create_product(Product(
            available=True, 
            price=17.0, 
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
        assert product.price == 17.0
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

    def test_get_product(self):
        repo = ProductRepositoryMock()
        product = repo.get_product(repo.products[0].product_id, repo.products[0].restaurant)

        assert type(product) == Product
        assert product.product_id == repo.products[0].product_id
        assert product.restaurant == repo.products[0].restaurant
    
    def test_get_product_product_not_found(self):
        repo = ProductRepositoryMock()
        product = repo.get_product("00000000-0000-0000-0000-000000000000")

        assert product == None

    def test_update_product(self):
        repo = ProductRepositoryMock()
        product = repo.update_product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', new_last_update=int(datetime.datetime.now().timestamp()*1000))

        assert repo.products[0].available == product.available
        assert repo.products[0].price == product.price
        assert repo.products[0].name == product.name
        assert repo.products[0].description == product.description
        assert repo.products[0].prepare_time == product.prepare_time
        assert repo.products[0].meal_type == product.meal_type
        assert repo.products[0].photo == product.photo
        assert repo.products[0].last_update == product.last_update