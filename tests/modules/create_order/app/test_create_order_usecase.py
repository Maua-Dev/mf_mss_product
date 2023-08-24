import pytest
from src.modules.create_order.app.create_order_usecase import CreateOrderUsecase
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateOrderUsecase:
    def test_create_order_usecase_with_all_include(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order=repo_order, repo_user=repo_user, repo_product=repo_product)

        order = usecase(user_name="Lucas Milas", user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", products=[OrderProduct(product_name='Hot Dog', product_id="c4bb21ac-d9f6-4d4b-b56c-215fb0f7aa09", quantity=2)], restaurant=RESTAURANT.SOUZA_DE_ABREU, total_price=10.0, obervation="Com ketchup")

        assert repo_order.orders[-1].order_id == order.order_id
        assert repo_order.orders[-1].user_name == order.user_name
        assert repo_order.orders[-1].user_id == order.user_id
        assert repo_order.orders[-1].products == order.products
        assert repo_order.orders[-1].creation_time_milliseconds == order.creation_time_milliseconds
        assert repo_order.orders[-1].restaurant == order.restaurant
        assert repo_order.orders[-1].status == order.status
        assert repo_order.orders[-1].total_price == order.total_price
        assert repo_order.orders[-1].observation == order.observation
        assert repo_order.orders[-1].aborted_reason == order.aborted_reason

    def test_create_order_usecase_ungeristered_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order=repo_order, repo_user=repo_user, repo_product=repo_product)

        with pytest.raises(UnregisteredUser):
            order = usecase(user_name="Lucas Milas", user_id="outro", products=[OrderProduct(product_name='Hot Dog', product_id="c4bb21ac-d9f6-4d4b-b56c-215fb0f7aa09", quantity=2)], restaurant=RESTAURANT.SOUZA_DE_ABREU, total_price=10.0, obervation="Com ketchup")

    def test_create_order_usecase_no_items_found_product_id(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order=repo_order, repo_user=repo_user, repo_product=repo_product)

        with pytest.raises(NoItemsFound):
            order = usecase(user_name="Lucas Milas", user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", products=[OrderProduct(product_name='Hot Dog', product_id="c4bb21ac-d9f6-4d4b-b56c-215fb0f7aa12", quantity=2)], restaurant=RESTAURANT.SOUZA_DE_ABREU, total_price=10.0, obervation="Com ketchup")

    def test_create_order_usecase_no_items_found_restaurant(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_product = ProductRepositoryMock()
        usecase = CreateOrderUsecase(repo_order=repo_order, repo_user=repo_user, repo_product=repo_product)

        with pytest.raises(NoItemsFound):
            order = usecase(user_name="Lucas Milas", user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", products=[OrderProduct(product_name='Hot Dog', product_id="c4bb21ac-d9f6-4d4b-b56c-215fb0f7aa09", quantity=2)], restaurant=STATUS.CANCELLED, total_price=10.0, obervation="Com ketchup")