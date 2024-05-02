from datetime import time

from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.entities.connection import Connection
from src.shared.domain.entities.feedback import Feedback
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.action_enum import ACTION
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_OrderRepositoryMock:
    def test_create_order(self):
        repo = OrderRepositoryMock()
        len_before = len(repo.orders)
        order = Order(
            order_id="1efc0e1a-24ed-4041-a4a0-fe5633711a3f", user_name="Lucas Milas",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", products=[
                OrderProduct(product_name="Copo da Felicidade", product_id="4d1716c4-5e51-4d72-ba93-349e31201a22",
                             quantity=1)], creation_time_milliseconds=1692159350000, restaurant=RESTAURANT.SOUZA_DE_ABREU,
            status=STATUS.PENDING, total_price=22.00, aborted_reason=None,
            last_status_update_milliseconds=1992159359900, action=ACTION.NEW
        )

        repo.create_order(order=order)

        assert len(repo.orders) == len_before + 1
        assert repo.orders[-1] == order

    def test_get_order_by_id(self):
        repo = OrderRepositoryMock()
        order_id = repo.orders[1].order_id

        response = repo.get_order_by_id(order_id=order_id)

        assert response.order_id == order_id
        assert response is repo.orders[1]

    def test_update_all_orders_attributes(self):
        repo = OrderRepositoryMock()
        order = repo.orders[1]
        order_id = order.order_id

        response = repo.update_order(
            order_id=order_id,
            new_products=[],
            new_status=STATUS.REFUSED,
            new_total_price=42.20,
            new_aborted_reason="Abortar missão, soldado"
        )

        assert order.products == []
        assert order.status == STATUS.REFUSED
        assert order.total_price == 42.20
        assert order.aborted_reason == "Abortar missão, soldado"

    def test_update_only_total_price(self):
        repo = OrderRepositoryMock()
        order = repo.orders[1]
        order_id = order.order_id

        response = repo.update_order(
            order_id=order_id,
            new_total_price=42.20,
        )
        assert order.total_price == 42.20

    def test_update_abortation_to_none(self):
        repo = OrderRepositoryMock()
        order = repo.orders[1]
        order_id = order.order_id

        response = repo.update_order(
            order_id=order_id,
            new_aborted_reason=None
        )
        assert order.aborted_reason is None

    def test_get_all_active_orders_by_restaurant(self):
        repo = OrderRepositoryMock()
        orders_list = repo.get_all_active_orders_by_restaurant(restaurant=RESTAURANT.SOUZA_DE_ABREU)

        assert len(orders_list) == 2

    def test_get_all_orders_by_restaurant_without_order_id(self):
        repo = OrderRepositoryMock()
        orders_list = repo.get_all_orders_by_restaurant(restaurant=RESTAURANT.SOUZA_DE_ABREU, exclusive_start_key=None,
                                                        amount=20)

        assert len(orders_list) == 7

    def test_get_all_orders_by_restaurant_with_order_id(self):
        repo = OrderRepositoryMock()
        order_id = repo.orders[2].order_id
        orders_list = repo.get_all_orders_by_restaurant(restaurant=RESTAURANT.SOUZA_DE_ABREU,
                                                        exclusive_start_key=order_id,
                                                        amount=20)

        assert len(orders_list) == 6

    def test_get_order_by_id(self):
        repo = OrderRepositoryMock()
        order_id = repo.orders[1].order_id

        response = repo.get_order_by_id(order_id=order_id)

        assert response.order_id == order_id
        assert response is repo.orders[1]

    def test_update_all_orders_attributes(self):
        repo = OrderRepositoryMock()
        order = repo.orders[1]
        order_id = order.order_id

        response = repo.update_order(
            order_id=order_id,
            new_products=[],
            new_status=STATUS.REFUSED,
            new_total_price=42.20,
            new_aborted_reason="Abortar missão, soldado"
        )

        assert order.products == []
        assert order.status == STATUS.REFUSED
        assert order.total_price == 42.20
        assert order.aborted_reason == "Abortar missão, soldado"

    def test_update_only_total_price(self):
        repo = OrderRepositoryMock()
        order = repo.orders[1]
        order_id = order.order_id

        response = repo.update_order(
            order_id=order_id,
            new_total_price=42.20,
        )
        assert order.total_price == 42.20


    def test_update_abortation_to_none(self):
        repo = OrderRepositoryMock()
        order = repo.orders[1]
        order_id = order.order_id

        response = repo.update_order(
            order_id=order_id,
            new_aborted_reason=None
        )
        assert order.aborted_reason is None

    def test_get_all_connections_by_restaurant(self):
        repo = OrderRepositoryMock()
        connections_list = repo.get_all_connections_by_restaurant(restaurant=RESTAURANT.SOUZA_DE_ABREU)

        assert len(connections_list) == 2
    
    def test_create_connection(self):
        repo = OrderRepositoryMock()
        len_before = len(repo.connections)

        connection = Connection(connection_id="4b133f88-2c34-3t", api_id="63c02df8-5", expire_date_seconds=1693418600, creation_time_seconds=1693414200, user_id="93bc6ada-c0d1-7054-42je-e17414c48af1", restaurant=RESTAURANT.CANTINA_DO_MOLEZA)

        repo.create_connection(connection=connection)

        assert len(repo.connections) == len_before + 1
        assert repo.connections[-1] == connection

    def test_abort_connection(self):
        repo = OrderRepositoryMock()
        len_before = len(repo.connections)

        connection_id = repo.connections[0].connection_id

        repo.abort_connection(connection_id)

        assert len(repo.connections) == len_before - 1

    def test_get_all_orders_by_user(self):
        repo = OrderRepositoryMock()
        order = repo.orders[0]

        order_list = repo.get_all_orders_by_user(user_id=order.user_id, exclusive_start_key=order.order_id, amount=2)

        assert len(order_list) == 2

    def test_create_feedback(self):
        repo = OrderRepositoryMock()
        len_before = len(repo.feedbacks)
        feedback = Feedback(
            order_id="1efc0e1a-24ed-4041-a4a0-fe5633711a3f",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            value=4
        )

        repo.create_feedback(feedback=feedback)

        assert len(repo.feedbacks) == len_before + 1
        assert repo.feedbacks[-1] == feedback
        
    def test_create_schedule(self):
        repo = OrderRepositoryMock()
        len_before = len(repo.schedules)
        schedule = Schedule(
            schedule_id="1efc0e1a-24ed-4041-a4a0-fe5633711a3f",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            hour_initial_time=7,
            minute_initial_time=0,
            hour_end_time=20,
            minute_end_time=0,
            accepted_reservation=True
        )

        repo.create_schedule(schedule=schedule)

        assert len(repo.schedules) == len_before + 1
        assert repo.schedules[-1] == schedule 
        
    def test_get_schedule_by_restaurant(self):
        repo = OrderRepositoryMock()
        schedule = repo.get_schedule_by_restaurant(restaurant=RESTAURANT.SOUZA_DE_ABREU)

        assert schedule is repo.schedules[1]
        
    def test_get_schedule_by_id(self):
        repo = OrderRepositoryMock()
        schedule_id = repo.schedules[1].schedule_id

        response = repo.get_schedule_by_id(schedule_id=schedule_id)

        assert response.schedule_id == schedule_id
        assert response is repo.schedules[1]
    
    def test_update_schedule(self):
        repo = OrderRepositoryMock()
        schedule = repo.schedules[1]
        schedule_id = schedule.schedule_id

        response = repo.update_schedule(
            schedule_id=schedule_id,
            new_initial_time=time(hour=7, minute=0),
            new_end_time=time(hour=20, minute=0),
            new_accepted_reservation=True
        )

        assert schedule.initial_time == time(7, 0)
        assert schedule.end_time == time(20, 0)
        
    
    
