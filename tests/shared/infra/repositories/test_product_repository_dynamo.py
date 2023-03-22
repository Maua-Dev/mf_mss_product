import pytest
from src.shared.infra.repositories.product_repository_dynamo import ProductRepositoryDynamo
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_ProductRepositoryDynamo:
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_product(self):
        repo_dynamo = ProductRepositoryDynamo()
        repo_mock = ProductRepositoryMock()

        new_product = repo_dynamo.create_product(new_product=repo_mock.products[2])

        assert new_product == repo_mock.products[2]