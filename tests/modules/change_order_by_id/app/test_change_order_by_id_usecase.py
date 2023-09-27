import pytest

from src.modules.change_order_by_id.app.change_order_by_id_usecase import ChangeOrderByIdUsecase
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotOrderOwner, \
    OrderCantBeUpdated, ProducutsListCantBeEmpty
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


def get_usecase_order_repo_and_user_repo(order_belongs_to_user: bool = True, is_user_admin: bool = False):
    order_repo = OrderRepositoryMock()
    user_repo = UserRepositoryMock()
    usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

    user = user_repo.users_list[-1]
    order = order_repo.orders[-1]
    order.status = STATUS.PENDING
    order.products = [OrderProduct("Pamonha", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 12)]


    if is_user_admin:
        user.role = ROLE.ADMIN
    else:
        user.role = ROLE.USER

    if order_belongs_to_user:
        order.user_id = user.user_id
    else:
        order.user_id = user_repo.users_list[-2]

    return usecase, order, user


class Test_ChangeOrderByIdUsecase:
    def test_change_order_products(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        order.observation = "Uma bela de uma observação, ein"

        response: Order = usecase(
            order_id=order.order_id,
            user_id=user.user_id,
            new_prods_list=[OrderProduct("Pamonha", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 12)]
        )

        assert len(response.products) == 1
        assert response.observation == "Uma bela de uma observação, ein"

    def test_change_order_obeservation(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        order.observation = "Uma bela de uma observação, ein"

        response: Order = usecase(
            order_id=order.order_id,
            user_id=user.user_id,
            new_observation="Uma nova observação"
        )

        assert len(response.products) != 0
        assert response.observation == "Uma nova observação"

    def test_order_doesnt_exist(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        with pytest.raises(NoItemsFound):
            response: Order = usecase(
                order_id="Um id que não existe",
                user_id=user.user_id,
                new_observation="Uma nova observação"
            )

    def test_user_doesnt_exist(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        with pytest.raises(UnregisteredUser):
            response: Order = usecase(
                order_id=order.order_id,
                user_id="Um id que não existe",
                new_observation="Uma nova observação"
            )

    def test_admin_change_order_whether_is_owner_or_not(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo(order_belongs_to_user=False, is_user_admin=True)

        response: Order = usecase(
            order_id=order.order_id,
            user_id=user.user_id,
            new_observation="Uma nova observação"
        )

        assert response.observation == "Uma nova observação"
        assert response.user_id != user.user_id
        assert user.role == ROLE.ADMIN

    def test_common_user_cant_change_order_if_its_not_the_owner(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo(order_belongs_to_user=False, is_user_admin=False)

        with pytest.raises(UserNotOrderOwner):
            response: Order = usecase(
                order_id=order.order_id,
                user_id=user.user_id,
                new_observation="Uma nova observação"
            )

    def test_order_cant_be_updated_if_is_not_pending(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        order.status = STATUS.PREPARING

        with pytest.raises(OrderCantBeUpdated):
            response: Order = usecase(
                order_id=order.order_id,
                user_id=user.user_id,
                new_observation="Uma nova observação"
            )

    def test_when_updating_list_it_cant_be_empty(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        with pytest.raises(ProducutsListCantBeEmpty):
            response: Order = usecase(
                order_id=order.order_id,
                user_id=user.user_id,
                new_observation="Uma nova observação",
                new_prods_list=[]
            )

    def test_order_can_be_updated_if_user_is_admin(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo(is_user_admin=True)

        order.status = STATUS.PREPARING

        response: Order = usecase(
                order_id=order.order_id,
                user_id=user.user_id,
                new_observation="Uma nova observação"
            )

        assert order.status == STATUS.PREPARING
        assert order.observation == "Uma nova observação"
