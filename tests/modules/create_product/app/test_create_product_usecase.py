from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.modules.create_product.app.create_product_usecase import CreateProductUsecase

class Test_CreateProductUsecase:
    def test_create_product_usecase(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        productLenBefore = len(repo.products)

        product = usecase(available=True, price=14.0, name="Lanche de Mortadela", description="Mortadela", meal_type=MEAL_TYPE.SANDWICHES, photo="https://avatars.githubusercontent.com/u/30812461?v=4", product_id=0, last_update=1674835337393, restaurant=RESTAURANT.SOUZA_DE_ABREU, prepareTime=20)
        
        productLenAfter = productLenBefore + 1

        assert len(repo.products) == productLenAfter
        assert product.available == True
        assert product.price == 14.0
        assert product.name == "Lanche de Mortadela"
        assert product.description == "Mortadela"
        assert product.meal_type == MEAL_TYPE.SANDWICHES
        assert product.photo == "https://avatars.githubusercontent.com/u/30812461?v=4"
        assert product.product_id == 93
        assert type(product.last_update) == int
        assert product.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert product.prepareTime == 20