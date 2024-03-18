import pytest

from src.modules.change_order_by_id.app.change_order_by_id_usecase import ChangeOrderByIdUsecase
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.action_enum import ACTION
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotOrderOwner, \
    OrderCantBeUpdated, ProducutsListCantBeEmpty
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ChangeOrderByIdUsecase:
    def test_change_order_products(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

        products_repo = ProductRepositoryMock().products

        order = usecase(order_id="8309d903-55ce-4299-9c70-13fa2e03bcdc", user_id=user_repo.users_list[2].user_id, new_prods_list=[OrderProduct(product_name=products_repo[167].name, product_id=products_repo[167].product_id, quantity=3, observation="Uma bela de uma observação, ein")])

        assert order_repo.orders[9].products == order.products
        assert order.action == ACTION.EDITED

    def test_order_doesnt_exist(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

        with pytest.raises(NoItemsFound):
            response: Order = usecase(
                order_id="Um id que não existe",
                user_id=user_repo.users_list[2].user_id,
            )

    def test_user_doesnt_exist(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

        with pytest.raises(UnregisteredUser):
            response: Order = usecase(
                order_id="8309d903-55ce-4299-9c70-13fa2e03bcdc",
                user_id="Um id que não existe",
            )

    def test_admin_change_order_whether_is_owner_or_not(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

        response: Order = usecase(
            order_id="8309d903-55ce-4299-9c70-13fa2e03bcdc",
            user_id=user_repo.users_list[0].user_id,
        )

        assert response.user_id != user_repo.users_list[0].user_id
        assert user_repo.users_list[0].role == ROLE.ADMIN

    def test_common_user_cant_change_order_if_its_not_the_owner(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

        with pytest.raises(UserNotOrderOwner):
            response: Order = usecase(
                order_id="8309d903-55ce-4299-9c70-13fa2e03bcdc",
                user_id=user_repo.users_list[4].user_id,
            )

    def test_order_cant_be_updated_if_is_not_pending(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

        with pytest.raises(OrderCantBeUpdated):
            response: Order = usecase(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_id=user_repo.users_list[4].user_id,
            )

    def test_when_updating_list_it_cant_be_empty(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

        with pytest.raises(ProducutsListCantBeEmpty):
            response: Order = usecase(
                order_id="8309d903-55ce-4299-9c70-13fa2e03bcdc",
                user_id=user_repo.users_list[2].user_id,
                new_prods_list=[]
            )

    def test_order_can_be_updated_if_user_is_admin(self):
        order_repo = OrderRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

        response: Order = usecase(
                order_id="d4c63753-5119-4990-b427-926798499924",
                user_id=user_repo.users_list[0].user_id,
            )

        assert response.status == STATUS.PREPARING
