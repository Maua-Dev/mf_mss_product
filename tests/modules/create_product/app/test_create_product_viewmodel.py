from src.modules.create_product.app.create_product_viewmodel import CreateProductViewmodel
from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class Test_CreateProductViewmodel:

    def test_create_product_viewmodel(self):

        product = Product(
            available=True,
            input_price=16.0,
            name="X-Salada",
            description="Hamburguer/Mussarela/Maionese/Alface/Tomate",
            meal_type=MEAL_TYPE.SANDWICHES,
            photo="https://avatars.githubusercontent.com/u/30812461?v=4",
            product_id="926a6368-806c-4845-bc4b-61bad0978ddf",
            last_update=1674835337393,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepare_time=20
        )

        product_viewmodel = CreateProductViewmodel(product=product).to_dict()

        expected = {
            "product": {
            "available":True,
            "price": 16.0,
            "name":"X-Salada",
            "description":"Hamburguer/Mussarela/Maionese/Alface/Tomate",
            "meal_type":"SANDWICHES",
            "photo":"https://avatars.githubusercontent.com/u/30812461?v=4",
            "product_id":"926a6368-806c-4845-bc4b-61bad0978ddf",
            "last_update":product_viewmodel["product"]["last_update"],
            "restaurant":"SOUZA_DE_ABREU",
            "prepare_time":20,
            },
            "message":"the product was created"
            }
        
        
        assert expected == product_viewmodel
        assert type(product_viewmodel["product"]["last_update"]) == int