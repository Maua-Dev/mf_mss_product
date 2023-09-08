import pytest
from src.modules.create_connection.app.manage_connection_usecase import ManageConnectionUsecase
from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ManageConnectionUsecase:
    def test_create_connection_usecase(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        len_before = len(repo_order.connections)

        connection = usecase(connection_id="8abqw064-r9lq-ul2", api_id="av2c2df8-6c", user_id=repo_user.users_list[0].user_id, restaurant=RESTAURANT.CANTINA_DO_MOLEZA)

        assert connection == "the connection was created"
        assert repo_order.connections[-1].connection_id == "8abqw064-r9lq-ul2"
        assert repo_order.connections[-1].api_id == "av2c2df8-6c"
        assert repo_order.connections[-1].user_id == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert repo_order.connections[-1].restaurant == RESTAURANT.CANTINA_DO_MOLEZA
        assert len(repo_order.connections) == len_before + 1

    def test_abort_connection_usecase(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        len_before = len(repo_order.connections)

        connection = usecase(connection_id="4b1e0f88-2c34-3t2", restaurant=RESTAURANT.CANTINA_DO_MOLEZA)

        assert connection == "the connection was aborted"
        assert len(repo_order.connections) == len_before - 1

    def test_abort_connection_usecase_no_connections_found(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)

        with pytest.raises(NoItemsFound):
            connection = usecase(connection_id="4b1e0f6h-2c34-3t2", restaurant=RESTAURANT.CANTINA_DO_MOLEZA)

    def test_manage_connection_usecase_ungeristered_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)

        with pytest.raises(UnregisteredUser):
            connection = usecase(connection_id="8abqw064-r9lq-ul2", api_id="av2c2df8-6c", user_id="id não encontrado :(", restaurant=RESTAURANT.CANTINA_DO_MOLEZA)