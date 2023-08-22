from typing import List

from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class OrderRepositoryMock(IOrderRepository):
    orders: List[Order]

    def __init__(self):
        users_repo = UserRepositoryMock().users_list
        products_repo = ProductRepositoryMock().products

        self.orders = [
            Order(order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53", user_name=users_repo[4].name, user_id=users_repo[4].user_id, products=[OrderProduct(product_name=products_repo[167].name, product_id=products_repo[167].product_id, quantity=2)], creation_time_milliseconds=1692061296, restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.READY, total_price=30.00, observation="Capricha no morango", aborted_reason=None),

            Order(order_id="d2b29a41-69a6-4ad8-87b9-2444119fbf66", user_name=users_repo[0].name, user_id=users_repo[0].user_id, products=[OrderProduct(product_name=products_repo[17].name, product_id=products_repo[17].product_id, quantity=1)], creation_time_milliseconds=1692154782, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.READY, total_price=28.00, observation="Sem Frango", aborted_reason=None),

            Order(order_id="2f8a8827-e8e6-4273-8587-e4a93da66bef", user_name=users_repo[1].name, user_id=users_repo[1].user_id, products=[OrderProduct(product_name=products_repo[59].name, product_id=products_repo[59].product_id, quantity=1), OrderProduct(product_name=products_repo[42].name, product_id=products_repo[167].product_id, quantity=2)], creation_time_milliseconds=1692155608, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.REFUSED, total_price=33.00, observation=None, aborted_reason="Estamos sem Toddynho"),

            Order(order_id="d4c63753-5119-4990-b427-926798499924", user_name=users_repo[5].name, user_id=users_repo[5].user_id, products=[OrderProduct(product_name=products_repo[121].name, product_id=products_repo[121].product_id, quantity=3)], creation_time_milliseconds=1692156322, restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.PREPARING, total_price=25.5, observation=None, aborted_reason=None),

            Order(order_id="ceffe392-931c-4f8e-becb-44dfbe39a35f", user_name=users_repo[3].name, user_id=users_repo[3].user_id, products=[OrderProduct(product_name=products_repo[102].name, product_id=products_repo[102].product_id, quantity=1)], creation_time_milliseconds=1692156623, restaurant=RESTAURANT.HORA_H, status=STATUS.PREPARING, total_price=38.00, observation="Meus acompanhamentos serão Salada de Tomate e Queijo Branco Temperado com Beringela Caponata", aborted_reason=None),

            Order(order_id="8f90159a-5b53-4b7d-84d5-e0b0e9e16c28", user_name=users_repo[6].name, user_id=users_repo[6].user_id, products=[OrderProduct(product_name=products_repo[99].name, product_id=products_repo[99].product_id, quantity=1)], creation_time_milliseconds=1692156833, restaurant=RESTAURANT.HORA_H, status=STATUS.REFUSED, total_price=39.00, observation="Vou querer com Arroz Integral, Creme de Milho e Mix Legumes", aborted_reason="São apenas 2 acompanhamentos"),

            Order(order_id="f60615cc-d1cd-41d5-8ff2-7406ee5fd214", user_name="Fernandão", user_id="d05bbfae-c06b-4d99-ac03-28945e6c30f3", products=[OrderProduct(product_name=products_repo[115].name, product_id=products_repo[115].product_id, quantity=2)], creation_time_milliseconds=1692157097, restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.CANCELLED, total_price=17.00, observation=None, aborted_reason="Minha aula já está prestes a começar! :( "),

            Order(order_id="9e0cdcc8-a27b-470a-975e-7f173d9390d0", user_name="Lukita", user_id="551a2637-3aae-42ef-a7e3-c8d6e3353e1c", products=[[OrderProduct(product_name=products_repo[10].name, product_id=products_repo[10].product_id, quantity=1)], OrderProduct(product_name=products_repo[48].name, product_id=products_repo[48].product_id, quantity=1)], creation_time_milliseconds=1692157371, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.REFUSED, total_price=30.00, observation=None, aborted_reason="Estamos fechando!"),

            Order(order_id="8309d903-55ce-4299-9c70-13fa2e03bcdc", user_name=users_repo[2].name, user_id=users_repo[2].user_id, products=[OrderProduct(product_name=products_repo[91].name, product_id=products_repo[91].product_id, quantity=1)], creation_time_milliseconds=1692157436, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.PENDING, total_price=24.00, observation=None, aborted_reason=None),

            Order(order_id="135ef881-1b1f-4f38-a662-8ff7156e6c27", user_name="Julião", user_id="34c82913-2942-4d55-9e64-489e79574948", products=[[OrderProduct(product_name=products_repo[71].name, product_id=products_repo[71].product_id, quantity=2)], OrderProduct(product_name=products_repo[67].name, product_id=products_repo[67].product_id, quantity=1), OrderProduct(product_name=products_repo[33].name, product_id=products_repo[33].product_id, quantity=3)], creation_time_milliseconds=1692157822, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.PENDING, total_price=35.5, observation=None, aborted_reason=None)
        ]

    def create_order(self, order: Order) -> Order:
        self.orders.append(order)
        return order