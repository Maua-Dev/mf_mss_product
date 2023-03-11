import pytest

from src.modules.get_product.app.get_product_usecase import GetProductUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock

class Test_GetProductUsecase:

    def test_get_product_usecase(self):
        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)

        product = usecase(product_id=repo.products[0].product_id)

        assert product == repo.products[0]

    def test_get_product_usecase_with_invalid_product_id(self):
        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)

        with pytest.raises(EntityError):
            product = usecase(product_id= 2)

