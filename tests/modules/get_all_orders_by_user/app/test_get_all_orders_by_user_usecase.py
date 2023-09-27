import pytest
from src.modules.get_all_orders_by_user.app.get_all_orders_by_user_usecase import GetAllOrdersByUserUsecase
from src.shared.helpers.errors.usecase_errors import UserNotOrderOwner, NoItemsFound, UnregisteredUser
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllOrdersByUserUsecase:
    def test_get_all_orders_by_user_usecase(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[4]
        order = repo_order.orders[0]

        get_all_orders = usecase(user_id=user.user_id, exclusive_start_key=order.order_id)

        assert len(get_all_orders) == 2

    def test_get_all_orders_by_user_diff_amount(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[4]
        order = repo_order.orders[0]

        get_all_orders = usecase(user_id=user.user_id, exclusive_start_key=order.order_id, amount=1)

        assert len(get_all_orders) == 1

    def test_get_all_orders_by_user_usecase_without_exclusive_start_key(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[4]
        order = repo_order.orders[0]

        get_all_orders = usecase(user_id=user.user_id)

        assert len(get_all_orders) == 2

    def test_get_all_orders_by_user_user_id_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        order = repo_order.orders[0]

        with pytest.raises(UnregisteredUser):
            get_all_orders = usecase(user_id="Não tem", exclusive_start_key=order.order_id)

    def test_get_all_orders_by_user_order_not_found(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[4]

        with pytest.raises(NoItemsFound):
            get_all_orders = usecase(user_id=user.user_id, exclusive_start_key="não achou")

    def test_get_all_orders_by_user_user_not_order_owner(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[4]
        order = repo_order.orders[3]

        with pytest.raises(UserNotOrderOwner):
            get_all_orders = usecase(user_id=user.user_id, exclusive_start_key=order.order_id)

