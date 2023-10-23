import pytest
from src.shared.domain.enums.status_enum import STATUS
from src.shared.infra.repositories.order_repository_dynamo import OrderRepositoryDynamo
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_OrderRepositoryDynamo:

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_order(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        order = repo_mock.orders[0]
        order.order_id = "66666666-e8e6-4273-8587-e4a93da66bef"

        new_order = repo_dynamo.create_order(new_order=order)

        assert new_order == repo_mock.orders[0]

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_order_by_id(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        order = repo_mock.orders[0]

        get_order = repo_dynamo.get_order_by_id(order.order_id)

        assert get_order == order

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_active_orders_by_restaurant(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        order = repo_mock.orders[2]

        get_all = repo_dynamo.get_all_active_orders_by_restaurant(order.restaurant)

        assert len(get_all) == 2

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_order(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        order = repo_mock.orders[0]

        update = repo_dynamo.update_order(order.order_id, new_status=STATUS.CANCELLED, new_aborted_reason="Minha aula começou")

        assert update.status.value == "CANCELLED"
        assert update.aborted_reason == "Minha aula começou"

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_orders_by_user(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        order = repo_mock.orders[0]

        get_all = repo_dynamo.get_all_orders_by_user(user_id=order.user_id, exclusive_start_key=order.order_id, amount=2)

        assert len(get_all) == 2
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_orders_by_restaurant(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        order = repo_mock.orders[0]

        get_all = repo_dynamo.get_all_orders_by_restaurant(restaurant=order.restaurant, exclusive_start_key=order.order_id)

        assert len(get_all) == 5

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_connection(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        connection = repo_mock.connections[1]
        connection.connection_id = "4b1e0f88-LLLL-3t"

        new_connection = repo_dynamo.create_connection(connection)

        assert new_connection == connection

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_abort_connection(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        connection = repo_mock.connections[0]

        abort_connection = repo_dynamo.abort_connection(connection.connection_id)

        assert True

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_connections_by_restaurant(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        connection = repo_mock.connections[3]

        get_all = repo_dynamo.get_all_connections_by_restaurant(restaurant=connection.restaurant)

        assert len(get_all) == 6

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_connection_by_connection_id(self):
        repo_dynamo = OrderRepositoryDynamo()
        repo_mock = OrderRepositoryMock()

        connection = repo_mock.connections[3]

        get_connection = repo_dynamo.get_connection_by_connection_id(connection.connection_id)

        assert get_connection == connection