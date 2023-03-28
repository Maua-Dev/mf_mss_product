import pytest
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_dynamo import ProductRepositoryDynamo
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_ProductRepositoryDynamo:
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_product(self):
        repo_dynamo = ProductRepositoryDynamo()
        repo_mock = ProductRepositoryMock()

        new_product = repo_dynamo.create_product(new_product=repo_mock.products[2])

        assert new_product == repo_mock.products[2]

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_product(self):
        repo_dynamo = ProductRepositoryDynamo()
        repo_mock = ProductRepositoryMock()

        update_product = repo_dynamo.update_product(restaurant=RESTAURANT.SOUZA_DE_ABREU, product_id='00170e97-6a4a-49c7-8bb2-342071ad752e', new_available=True, new_price=20.0, new_name='Novo_produto', new_description='Nova_descrição', new_prepare_time=20, new_meal_type=MEAL_TYPE.PLATES, new_photo="https://avatars.githubusercontent.com/u/30812461?v=4", new_last_update=1678228149)

        assert update_product.available == True
        assert update_product.description == "Nova_descrição"
        assert update_product.name == "Novo_produto"