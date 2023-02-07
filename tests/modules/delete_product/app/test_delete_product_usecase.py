import pytest
from src.modules.delete_product.app.delete_product_usecase import DeleteProductsByRestaurantUsecase
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.domain_errors import EntityError


class Test_DeleteProductsByRestaurantUsecase:
    def test_delete_products_by_restaurant_usecase(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductsByRestaurantUsecase(repo=repo)
        lenBefore = len(repo.products)

        product_id = 0

        product = usecase(product_id=product_id, restaurant=RESTAURANT.SOUZA_DE_ABREU)

        assert len(repo.products) == lenBefore - 1
        assert [product.product_id, product.restaurant] == [product_id, repo.products[0].restaurant]

    def test_delete_products_by_restaurant_diff_type_product_id(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductsByRestaurantUsecase(repo=repo)

        with pytest.raises(EntityError):
            product = usecase(product_id="0", restaurant=RESTAURANT.SOUZA_DE_ABREU)

    def test_delete_products_by_restaurant_diff_type_restaurant(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductsByRestaurantUsecase(repo=repo)

        with pytest.raises(EntityError):
            product = usecase(product_id=0, restaurant="SOUZA_DE_ABREU")

    def test_delete_products_by_restaurant_not_found_product_id(self):
        repo = ProductRepositoryMock()
        usecase = DeleteProductsByRestaurantUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            product = usecase(product_id=1000, restaurant=RESTAURANT.SOUZA_DE_ABREU)

