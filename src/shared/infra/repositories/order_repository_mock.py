from ast import Dict
from datetime import datetime
from typing import List, Optional

from src.shared.domain.entities.order import Order
from src.shared.domain.entities.connection import Connection
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class OrderRepositoryMock(IOrderRepository):
    orders: List[Order]
    connections: List[Connection]

    def __init__(self):
        users_repo = UserRepositoryMock().users_list
        products_repo = ProductRepositoryMock().products

        self.orders = [
            Order(order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53", user_name=users_repo[4].name,
                  user_id=users_repo[4].user_id, products=[
                    OrderProduct(product_name=products_repo[167].name, product_id=products_repo[167].product_id,
                                 quantity=2)], creation_time_milliseconds=1692061296000,
                  restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.READY, total_price=30.00,
                   aborted_reason=None,
                  last_status_update_milliseconds=1992061596999
                  ),

            Order(order_id="b3f6c5aa-80ad-4f95-ae16-455b4f874553", user_name=users_repo[4].name,
                  user_id=users_repo[4].user_id, products=[
                    OrderProduct(product_name=products_repo[168].name, product_id=products_repo[168].product_id,
                                 quantity=2)], creation_time_milliseconds=1692061297000,
                  restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.READY, total_price=14.00,
                    aborted_reason=None,
                  last_status_update_milliseconds=1992061596999
                  ),

            Order(order_id="d2b29a41-69a6-4ad8-87b9-2444119fbf66", user_name=users_repo[0].name,
                  user_id=users_repo[0].user_id, products=[
                    OrderProduct(product_name=products_repo[17].name, product_id=products_repo[17].product_id,
                                 quantity=1)], creation_time_milliseconds=1692154782000,
                  restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.READY, total_price=28.00,
                   aborted_reason=None,
                  last_status_update_milliseconds=1992061596999
                  ),

            Order(order_id="2f8a8827-e8e6-4273-8587-e4a93da66bef", user_name=users_repo[1].name,
                  user_id=users_repo[1].user_id, products=[
                    OrderProduct(product_name=products_repo[59].name, product_id=products_repo[59].product_id,
                                 quantity=1),
                    OrderProduct(product_name=products_repo[42].name, product_id=products_repo[167].product_id,
                                 quantity=2)], creation_time_milliseconds=1692155608000,
                  restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.REFUSED, total_price=33.00,
                  aborted_reason="Estamos sem Toddynho",
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="d4c63753-5119-4990-b427-926798499924", user_name=users_repo[5].name,
                  user_id=users_repo[5].user_id, products=[
                    OrderProduct(product_name=products_repo[121].name, product_id=products_repo[121].product_id,
                                 quantity=3)], creation_time_milliseconds=1692156322000,
                  restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.PREPARING, total_price=25.5,
                  aborted_reason=None,
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="ceffe392-931c-4f8e-becb-44dfbe39a35f", user_name=users_repo[3].name,
                  user_id=users_repo[3].user_id, products=[
                    OrderProduct(product_name=products_repo[102].name, product_id=products_repo[102].product_id,
                                 quantity=1)], creation_time_milliseconds=1692156623000, restaurant=RESTAURANT.HORA_H,
                  status=STATUS.PREPARING, total_price=38.00,
                  aborted_reason=None,
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="8f90159a-5b53-4b7d-84d5-e0b0e9e16c28", user_name=users_repo[6].name,
                  user_id=users_repo[6].user_id, products=[
                    OrderProduct(product_name=products_repo[99].name, product_id=products_repo[99].product_id,
                                 quantity=1)], creation_time_milliseconds=1692156833000, restaurant=RESTAURANT.HORA_H,
                  status=STATUS.REFUSED, total_price=39.00,
                  aborted_reason="São apenas 2 acompanhamentos",
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="f60615cc-d1cd-41d5-8ff2-7406ee5fd214", user_name="Fernandão",
                  user_id="d05bbfae-c06b-4d99-ac03-28945e6c30f3", products=[
                    OrderProduct(product_name=products_repo[115].name, product_id=products_repo[115].product_id,
                                 quantity=2)], creation_time_milliseconds=1692157097000,
                  restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.CANCELLED, total_price=17.00,
                  aborted_reason="Minha aula já está prestes a começar! :( ",
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="9e0cdcc8-a27b-470a-975e-7f173d9390d0", user_name="Lukita",
                  user_id="551a2637-3aae-42ef-a7e3-c8d6e3353e1c", products=[
                    OrderProduct(product_name=products_repo[10].name, product_id=products_repo[10].product_id,
                                 quantity=1),
                    OrderProduct(product_name=products_repo[48].name, product_id=products_repo[48].product_id,
                                 quantity=1)], creation_time_milliseconds=1692157371000,
                  restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.REFUSED, total_price=30.00,
                  aborted_reason="Estamos fechando!",
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="8309d903-55ce-4299-9c70-13fa2e03bcdc", user_name=users_repo[2].name,
                  user_id=users_repo[2].user_id, products=[
                    OrderProduct(product_name=products_repo[91].name, product_id=products_repo[91].product_id,
                                 quantity=1)], creation_time_milliseconds=1692157436000,
                  restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.PENDING, total_price=24.00,
                  aborted_reason=None,
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="135ef881-1b1f-4f38-a662-8ff7156e6c27", user_name=users_repo[9].name,
                  user_id=users_repo[9].user_id, products=[
                    OrderProduct(product_name=products_repo[71].name, product_id=products_repo[71].product_id,
                                 quantity=2),
                    OrderProduct(product_name=products_repo[67].name, product_id=products_repo[67].product_id,
                                 quantity=1),
                    OrderProduct(product_name=products_repo[33].name, product_id=products_repo[33].product_id,
                                 quantity=3)], creation_time_milliseconds=1692157822000,
                  restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.PENDING, total_price=35.5,
                  aborted_reason=None,
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="1eeef881-1b1f-4f38-a662-8ff7156e6c27", user_name=users_repo[9].name,
                  user_id=users_repo[9].user_id, products=[
                    OrderProduct(product_name=products_repo[71].name, product_id=products_repo[71].product_id,
                                 quantity=2),
                    OrderProduct(product_name=products_repo[67].name, product_id=products_repo[67].product_id,
                                 quantity=1),
                    OrderProduct(product_name=products_repo[33].name, product_id=products_repo[33].product_id,
                                 quantity=3)], creation_time_milliseconds=1692157822000,
                  restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.REFUSED, total_price=35.5,
                  aborted_reason=None,
                  last_status_update_milliseconds=1992061596999),

            Order(order_id="1feef881-1b1f-4f38-a662-8ff7156e6c27", user_name=users_repo[9].name,
                  user_id=users_repo[9].user_id, products=[
                    OrderProduct(product_name=products_repo[71].name, product_id=products_repo[71].product_id,
                                 quantity=2,
                                observation="Estou observando aqui"
                                 ),
                    OrderProduct(product_name=products_repo[67].name, product_id=products_repo[67].product_id,
                                 quantity=1,
                                 observation="Olha eu observando dnv"
                                 ),
                    OrderProduct(product_name=products_repo[33].name, product_id=products_repo[33].product_id,
                                 quantity=3,
                                 observation="sem comentarios"
                                 )], creation_time_milliseconds=1692157822,
                  restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.READY, total_price=35.5,
                  aborted_reason=None,
                  last_status_update_milliseconds=1992061596999)
        ]

        self.connections = [
            Connection(connection_id="4b1e0f88-2c34-3t", api_id="63c02df8-d", expire_date_seconds=1693418400,
                       creation_time_seconds=1693414800, user_id=users_repo[2].user_id,
                       restaurant=RESTAURANT.CANTINA_DO_MOLEZA),

            Connection(connection_id="d43e0f88-ab24-ec", api_id="b1f02df8-g", expire_date_seconds=1693328400,
                       creation_time_seconds=1693324800, user_id=users_repo[3].user_id,
                       restaurant=RESTAURANT.SOUZA_DE_ABREU),

            Connection(connection_id="ad2e0f88-2c34-bv", api_id="efc02df8-r", expire_date_seconds=1683291600,
                       creation_time_seconds=1683288000, user_id=users_repo[1].user_id, restaurant=RESTAURANT.HORA_H),

            Connection(connection_id="yu120f88-2c34-45", api_id="gdc02df8-j", expire_date_seconds=1682265600,
                       creation_time_seconds=1682262000, user_id=users_repo[0].user_id, restaurant=RESTAURANT.HORA_H),

            Connection(connection_id="9efe0f88-tu34-cd", api_id="a9kpodf8-a", expire_date_seconds=1686848400,
                       creation_time_seconds=1686844800, user_id=users_repo[4].user_id,
                       restaurant=RESTAURANT.CANTINA_DO_MOLEZA),

            Connection(connection_id="48kl9abc-kd20-af", api_id="52h4g57l-u", expire_date_seconds=1675087200,
                       creation_time_seconds=1675083600, user_id=users_repo[5].user_id, restaurant=RESTAURANT.HORA_H),

            Connection(connection_id="8abc9064-r9lq-ul", api_id="av2c2df8-d", expire_date_seconds=1677636000,
                       creation_time_seconds=1677632400, user_id=users_repo[6].user_id,
                       restaurant=RESTAURANT.SOUZA_DE_ABREU),
        ]

    def create_order(self, order: Order) -> Order:
        self.orders.append(order)
        return order

    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def get_all_active_orders_by_restaurant(self, restaurant: RESTAURANT) -> List[Order]:
        return [order for order in self.orders if
                order.status in [STATUS.PENDING, STATUS.PREPARING] and order.restaurant == restaurant]

    def update_order(self, order_id: str, new_products: Optional[List[OrderProduct]] = None,
                     new_status: Optional[STATUS] = None,
                     new_total_price: Optional[float] = None,
                     new_aborted_reason: Optional[str] = None):

        order_to_update = self.get_order_by_id(order_id)

        if order_to_update is None:
            return None

        if new_products is not None:
            order_to_update.products = new_products

        if new_status is not None:
            order_to_update.status = new_status
            order_to_update.last_status_update_milliseconds = int(datetime.now().timestamp() * 1000)

        if new_total_price is not None:
            order_to_update.total_price = new_total_price

        if new_aborted_reason is not None:  # Mesma coisa para o motivo de ter abortado o pedido
            if new_aborted_reason == "":
                order_to_update.aborted_reason = None
            else:
                order_to_update.aborted_reason = new_aborted_reason

        return order_to_update

    def get_all_connections_by_restaurant(self, restaurant: RESTAURANT) -> List[Connection]:
        return [connection for connection in self.connections if connection.restaurant == restaurant]

    def create_connection(self, connection: Connection) -> Connection:
        self.connections.append(connection)
        return connection

    def abort_connection(self, connection_id: str) -> Connection:
        connection = self.get_connection_by_connection_id(connection_id=connection_id)
        if connection is None:
            return None
        else:
            restaurant = connection.restaurant
        
        for connection in self.connections:
            if connection_id == connection.connection_id and restaurant == connection.restaurant:
                self.connections.remove(connection)
                return connection
        return None

    def publish_order(self, connections_list: List[Connection], order: Order) -> bool:
        return True
    
    def get_all_orders_by_user(self, user_id: str, exclusive_start_key: str or None, amount: int) -> List[Order]:

        # Getting all orders from the requested user_id sorted by creation_time_milliseconds
        user_orders = sorted([order for order in self.orders if order.user_id == user_id],
                             key=lambda order: order.creation_time_milliseconds, reverse=False)

        # Getting the order_id position in the list
        if exclusive_start_key:
            for index, order in enumerate(user_orders):
                if order.order_id == exclusive_start_key:
                    order_id_position = index
                    return user_orders[order_id_position:order_id_position + amount]

        else:
            return user_orders[:amount]

    def get_all_orders_by_restaurant(self, restaurant: RESTAURANT, exclusive_start_key: str or None, amount: int) -> \
    List[Order]:
        # Getting all orders from the requested restaurant sorted by creation_time_milliseconds
        restaurant_orders = sorted([order for order in self.orders if order.restaurant == restaurant],
                                   key=lambda order: order.creation_time_milliseconds, reverse=False)

        # Getting the order_id position in the list
        if exclusive_start_key:
            for index, order in enumerate(restaurant_orders):
                if order.order_id == exclusive_start_key:
                    order_id_position = index
                    return restaurant_orders[order_id_position:order_id_position + amount]

        else:
            return restaurant_orders[:amount]
        
    def get_connection_by_connection_id(self, connection_id: str) -> Optional[Connection]:
        for connection in self.connections:
            if connection.connection_id == connection_id:
                return connection
        return None
