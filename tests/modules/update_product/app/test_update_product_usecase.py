from src.modules.update_product.app.update_product_usecase import UpdateProductUsecase
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_UpdateProductUsecase:
    def test_update_product_usecase(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo=repo)

        product = usecase(new_available=True, new_price=20.0, new_name='Novo Produto', new_description='Nova Descrição', new_prepare_time=20, new_meal_type=MEAL_TYPE.CANDIES, new_photo='new_photo', new_last_update=1678742373, new_restaurant=RESTAURANT.HORA_H)

        