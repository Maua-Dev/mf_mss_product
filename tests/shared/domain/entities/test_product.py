import pytest

from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Product:
    def test_product(self):
        product = Product(
            available=True,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=7
        )
        
        assert type(product) == Product
        assert product.available == True
        assert product.price == 20.00
        assert product.name == "Carne"
        assert product.description == "Um lanche de Carne"
        assert product.meal_type == MEAL_TYPE.PORTIONS
        assert product.photo == "https://avatars.githubusercontent.com/u/30812461?v=4"
        assert product.product_id == 5
        assert product.last_update == 1639323013000
        assert product.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert product.prepareTime == 7
    
    def test_product_prepareTime_None(self): 
        product = Product(
            available=True,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        )
        
        assert type(product) == Product
        assert product.available == True
        assert product.price == 20.00
        assert product.name == "Carne"
        assert product.description == "Um lanche de Carne"
        assert product.meal_type == MEAL_TYPE.PORTIONS
        assert product.photo == "https://avatars.githubusercontent.com/u/30812461?v=4"
        assert product.product_id == 5
        assert product.last_update == 1639323013000
        assert product.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert product.prepareTime == None
    
    def test_product_available_invalid(self): 
        with pytest.raises(EntityError):
            Product(
            available=10,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        )
    
    def test_product_price_invalid(self): 
        with pytest.raises(EntityError):
            Product(
            available=True,
            price="Lanche",
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        )
    
    def test_product_name_invalid(self):
        with pytest.raises(EntityError):
            Product(
            available=True,
            price=20.00,
            name=5,
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        )
    
    def test_product_description_invalid(self):
        with pytest.raises(EntityError):
            Product(
            available=True,
            price=20.00,
            name="Carne",
            description=8,
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        )
    
    def test_product_meal_type_invalid(self): 
        with pytest.raises(EntityError):
            Product(
            available=True,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=True,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        )
    
    def test_product_photo_invalid(self): 
        with pytest.raises(EntityError):
            Product(
            available=True,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo=None,
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        )
    
    def test_product_product_id_invalid(self): 
        with pytest.raises(EntityError):
            Product(
            available=True,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=[],
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        ) 
    
    def test_product_last_update_invalid(self): 
        with pytest.raises(EntityError):
            Product(
            available=True,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update={},
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=None
        )
    
    def test_product_restaurant_invalid(self): 
        with pytest.raises(EntityError):
            Product(
            available=True,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=MEAL_TYPE.SNACKS,
            prepareTime=None
        )
    
    def test_product_prepareTime_invalid(self): 
        with pytest.raises(EntityError):
            Product(
            available=True,
            price=20.00,
            name="Carne",
            description="Um lanche de Carne",
            meal_type=MEAL_TYPE.PORTIONS,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id=5,
            last_update=1639323013000,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepareTime=()
        )
        
    

    