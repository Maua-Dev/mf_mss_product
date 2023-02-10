from src.modules.delete_product.app.delete_product_viewmodel import DeleteProductViewmodel
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_DeleteProductViewmodel:
    def test_delete_product_viewmodel(self):
        repo = ProductRepositoryMock()
        viewmodel = DeleteProductViewmodel(repo.products[0])

        expected ={
        'product':{
            'available':True,
            'price':16.0,
            'name':'X-Salada',
            'description':'Hamburguer/Mussarela/Maionese/Alface/Tomate',
            'prepareTime':20,
            'meal_type':'SANDWICHES',
            'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
            'product_id':'8a705b91-c9e9-4353-a755-07f13afafed3',
            'last_update':1674835337393,
            'restaurant':'SOUZA_DE_ABREU'
        },
        'message':'the product was deleted'
        }

        assert viewmodel.to_dict() == expected

