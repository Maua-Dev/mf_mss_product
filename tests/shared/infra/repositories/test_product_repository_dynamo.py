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

        product = repo_mock.products[2]
        product.available = False
        product.name = 'Teste do False'

        new_product = repo_dynamo.create_product(new_product=product)

        assert new_product == repo_mock.products[2]

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_product(self):
        repo_dynamo = ProductRepositoryDynamo()
        repo_mock = ProductRepositoryMock()

        update_product = repo_dynamo.update_product(restaurant=RESTAURANT.SOUZA_DE_ABREU, product_id='00170e97-6a4a-49c7-8bb2-342071ad752e', new_available=True, new_price=20.0, new_name='Novo_produto', new_description='Nova_descrição', new_prepare_time=20, new_meal_type=MEAL_TYPE.PLATES, new_photo="https://avatars.githubusercontent.com/u/30812461?v=4", new_last_update=1678228149)

        assert update_product.available == True
        assert update_product.description == "Nova_descrição"
        assert update_product.name == "Novo_produto"

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_product(self):
        repo_dynamo = ProductRepositoryDynamo()
        repo_mock = ProductRepositoryMock()

        product = repo_mock.products[1]

        get_product = repo_dynamo.get_product(product_id=product.product_id, restaurant=product.restaurant)

        assert get_product.available == product.available
        assert get_product.name == product.name
        assert get_product.description == product.description
        assert get_product.price == product.price
        assert get_product.meal_type == product.meal_type
        assert get_product.prepare_time == product.prepare_time

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_delete_product(self):
        repo_dynamo = ProductRepositoryDynamo()
        repo_mock = ProductRepositoryMock()

        product = repo_mock.products[0]
        
        delete_product = repo_dynamo.delete_product(product_id=product.product_id, restaurant=product.restaurant)

        assert True

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_products_group_by_restaurant(self):
        repo_dynamo = ProductRepositoryDynamo()
        repo_mock = ProductRepositoryMock()

        products = repo_mock.products
        
        get_all_products = repo_dynamo.get_all_products_group_by_restaurant()

        assert len([restaurant_value.value for restaurant_value in RESTAURANT]) == len(get_all_products.keys())
