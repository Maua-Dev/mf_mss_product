import pytest

from src.modules.get_product.app.get_product_usecase import GetProductUsecase
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock

class Test_GetProductUsecase:

    def test_get_product_usecase(self):
        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)

        product = usecase(product_id=repo.products[0].product_id, restaurant=repo.products[0].restaurant)

        assert product.product_id == repo.products[0].product_id
        assert product.restaurant == repo.products[0].restaurant

    def test_get_product_usecase_with_invalid_product_id(self):
        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)

        with pytest.raises(EntityError):
            product = usecase(product_id= "1234", restaurant=RESTAURANT.HORA_H)
       
    def test_get_product_usecase_with_invalid_type_product_id(self):
        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)

        with pytest.raises(EntityError):
            product = usecase(product_id= 2, restaurant=RESTAURANT.HORA_H)

    def test_get_product_usecase_with_invalid_restaurant(self):
        repo = ProductRepositoryMock()
        usecase = GetProductUsecase(repo)

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant="Souzinha")

