import pytest
from src.modules.get_all_orders_by_user.app.get_all_orders_by_user_usecase import GetAllOrdersByUserUsecase
from src.shared.helpers.errors.usecase_errors import MismatchID, NoItemsFound, UnregisteredUser, UserNotAllowed
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllOrdersByUserUsecase:
    def test_get_all_orders_by_user_usecase(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[4]
        order = repo_order.orders[0]

        get_all_orders = usecase(user_id=user.user_id, order_id=order.order_id)

        assert len(get_all_orders) == 2

    def test_get_all_orders_by_user_user_id_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        order = repo_order.orders[0]

        with pytest.raises(UnregisteredUser):
            get_all_orders = usecase(user_id="Não tem", order_id=order.order_id)

    def test_get_all_orders_by_user_user_not_allowed(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[0]
        order = repo_order.orders[0]

        with pytest.raises(UserNotAllowed):
            get_all_orders = usecase(user_id=user.user_id, order_id=order.order_id)

    def test_get_all_orders_by_user_order_not_found(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[4]

        with pytest.raises(NoItemsFound):
            get_all_orders = usecase(user_id=user.user_id, order_id="não achou")

    def test_get_all_orders_by_user_mismatch_id(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        user = repo_user.users_list[4]
        order = repo_order.orders[3]

        with pytest.raises(MismatchID):
            get_all_orders = usecase(user_id=user.user_id, order_id=order.order_id)

