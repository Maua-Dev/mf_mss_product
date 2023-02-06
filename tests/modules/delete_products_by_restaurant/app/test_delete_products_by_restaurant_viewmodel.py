from src.modules.delete_products_by_restaurant.app.delete_products_by_restaurant_viewmodel import DeleteProductsByRestaurantViewmodel
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_DeleteProductsByRestaurantViewmodel:
    def test_delete_products_by_restaurant_viewmodel(self):
        repo = ProductRepositoryMock()
        viewmodel = DeleteProductsByRestaurantViewmodel(repo.products[0])

        expected = {
            'product': {
                "available": True,
                "price": 14.0,
                "name": "Lanche Mortadela",
                "description": "Mortadela",
                "prepareTime": 20,
                "meal_type": "SANDWICHES",
                "photo": 'https://avatars.githubusercontent.com/u/30812461?v=4',
                "product_id": 0,
                "last_update": 1674835337393,
                "restaurant": "SOUZA_DE_ABREU"
            },
            'message': "the product was deleted" 
        }

        assert viewmodel.to_dict() == expected

