import pytest
from src.modules.delete_product.app.delete_product_usecase import DeleteProductUsecase
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotAllowed
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteProductUsecase:
    def test_delete_product_usecase(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteProductUsecase(repo_prod,repo_user)
        lenBefore = len(repo_prod.products)

        product_id = "8a705b91-c9e9-4353-a755-07f13afafed3"
        user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae5"

        product = usecase(product_id=product_id, restaurant=RESTAURANT.SOUZA_DE_ABREU, user_id=user_id)

        assert len(repo_prod.products) == lenBefore - 1
        assert [product.product_id, product.restaurant] == [product_id, repo_prod.products[0].restaurant]

    def test_delete_product_usecase_role_invalid(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteProductUsecase(repo_prod,repo_user)

        product_id = "8a705b91-c9e9-4353-a755-07f13afafed3"
        user_id = "93bc6ada-c0d1-7054-66ab-e17414c48af1"

        with pytest.raises(UserNotAllowed):
            product = usecase(product_id=product_id, restaurant=RESTAURANT.SOUZA_DE_ABREU, user_id=user_id)

    def test_delete_product_product_id_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteProductUsecase(repo_prod,repo_user)

        user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae5"

        with pytest.raises(EntityError):
            product = usecase(product_id=123, restaurant=RESTAURANT.SOUZA_DE_ABREU, user_id=user_id)
            
    def test_delete_product_product_id_invalid_length(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteProductUsecase(repo_prod,repo_user)

        user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae5"

        with pytest.raises(EntityError):
            product = usecase(product_id="27cb49f5-4313-49a7-9f84", restaurant=RESTAURANT.SOUZA_DE_ABREU, user_id=user_id)

    def test_delete_product_diff_type_restaurant(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteProductUsecase(repo_prod,repo_user)

        user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae5"

        with pytest.raises(EntityError):
            product = usecase(product_id="6d6b38c0-927d-4c43-93b7-b33ea9278cba", restaurant="SOUZA_DE_ABREU", user_id=user_id)

    def test_delete_product_not_found_product_id(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteProductUsecase(repo_prod,repo_user)

        user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae5"

        with pytest.raises(NoItemsFound):
            product = usecase(product_id="6d6b38c0-927d-4c43-93b7-b33ea9278cma", restaurant=RESTAURANT.SOUZA_DE_ABREU, user_id=user_id)

    def test_delete_product_unregistered_user(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteProductUsecase(repo_prod,repo_user)

        user_id = "id"

        with pytest.raises(UnregisteredUser):
            product = usecase(product_id="6d6b38c0-927d-4c43-93b7-b33ea9278cma", restaurant=RESTAURANT.SOUZA_DE_ABREU, user_id=user_id)


