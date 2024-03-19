import pytest
from src.modules.manage_connection.app.manage_connection_usecase import ManageConnectionUsecase
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotAllowed, WrongTypeRouteKey
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ManageConnectionUsecase:
    def test_create_connection_usecase(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        len_before = len(repo_order.connections)

        connection = usecase(connection_id="8abqw064-r9lq-ul", api_id="av2c2df8-6", user_id=repo_user.users_list[0].user_id, route_key="$connect")

        assert repo_order.connections[-1].connection_id == connection.connection_id
        assert repo_order.connections[-1].api_id == connection.api_id
        assert repo_order.connections[-1].user_id == connection.user_id
        assert repo_order.connections[-1].creation_time_seconds == connection.creation_time_seconds
        assert repo_order.connections[-1].expire_date_seconds == connection.expire_date_seconds
        assert len(repo_order.connections) == len_before + 1

    def test_abort_connection_usecase_disconnect(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        len_before = len(repo_order.connections)

        connection = usecase(connection_id="4b1e0f88-2c34-3t", api_id="63c02df8-d", user_id=repo_user.users_list[2].user_id)

        assert len(repo_order.connections) == len_before - 1

    def test_manage_connection_usecase_default_error(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)

        with pytest.raises(WrongTypeRouteKey):
            connection = usecase(connection_id="4b1e0f88-2c34-3t", api_id="63c02df8-d", user_id=repo_user.users_list[0].user_id, route_key="$default")

    def test_abort_connection_usecase_no_connections_found(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)

        with pytest.raises(NoItemsFound):
            connection = usecase(connection_id="4b1e0f88-2c34-66", api_id="63c02df8-d", user_id=repo_user.users_list[0].user_id)

    def test_manage_connection_usecase_user_not_allowed(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)

        with pytest.raises(UserNotAllowed):
            connection = usecase(connection_id="4b1e0f88-2c34-3t", api_id="63c02df8-d", user_id=repo_user.users_list[4].user_id, route_key="$connect")

    def test_manage_connection_usecase_ungeristered_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)

        with pytest.raises(UnregisteredUser):
            connection = usecase(connection_id="4b1e0f88-2c34-3t", api_id="63c02df8-d", user_id="id não encontrado :(", route_key="$connect")