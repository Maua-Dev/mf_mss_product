from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.modules.get_product.app.get_product_viewmodel import GetProductViewmodel

class Test_GetProductViewmodel:

    def test_get_product_viewmodel(self):
        repo = ProductRepositoryMock()

        product = repo.products[0]

        get_product_viewmodel = GetProductViewmodel(product).to_dict()

        excepted = {
            "product":{
                    "available":True, 
                    "price":19.0, 
                    "name":'X-Salada', 
                    "description":'Hamburguer/Mussarela/Maionese/Alface/Tomate', 
                    "prepare_time":20, 
                    "meal_type":"SANDWICHES", 
                    "photo":'https://avatars.githubusercontent.com/u/30812461?v=4', 
                    "product_id":"8a705b91-c9e9-4353-a755-07f13afafed3", 
                    "last_update":1678228149, 
                    "restaurant":"SOUZA_DE_ABREU" },
            'message': 'the product was retrieved'}

        assert get_product_viewmodel == excepted