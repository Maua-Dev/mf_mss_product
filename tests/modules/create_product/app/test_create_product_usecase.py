from src.shared.domain.entities.product import Product
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.modules.create_product.app.create_product_usecase import CreateProductUsecase
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class Test_CreateProductUsecase:
    def test_create_product_usecase(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)

        product = usecase(available=True, price=14.0, name='Lanche Mortadela', description='Mortadela', prepareTime=20, meal_type=MEAL_TYPE.SANDWICHES, photo='https://avatars.githubusercontent.com/u/30812461?v=4', restaurant=RESTAURANT.SOUZA_DE_ABREU)
        
        assert type(product) == Product
        assert type(product.product_id) == str
        assert len(product.product_id) == 36
        assert type(product.last_update) == int
        
        
