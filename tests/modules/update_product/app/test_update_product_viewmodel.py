from src.modules.update_product.app.update_product_viewmodel import UpdateProductViewmodel
from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_UpdateProductViewmodel:
    def test_update_product_viewmodel(self):
        
        product = Product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, available=True, price=15.0, name='Nome Atualizado', description='Descrição Atualizada', prepare_time=20, meal_type=MEAL_TYPE.DRINKS, photo='new_photo', last_update=1678744638)

        viewmodel = UpdateProductViewmodel(product=product)

        expected ={
        'product':{
            'product_id':'8a705b91-c9e9-4353-a755-07f13afafed3',
            'restaurant':'SOUZA_DE_ABREU',
            'available':True,
            'price':15.0,
            'name':'Nome Atualizado',
            'description':'Descrição Atualizada',
            'prepare_time':20,
            'meal_type':'DRINKS',
            'photo':'new_photo',
            'last_update':1678744638,
        },
        'message':'the product was updated'
        }

        assert viewmodel.to_dict() == expected