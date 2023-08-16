from typing import List

from src.shared.domain.entities.order import Order
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.repositories.order_repository_interface import IOrderRepository


class OrderRepositoryMock(IOrderRepository):
    orders: List[Order]

    def __init__(self):
        self.orders = [
            Order(order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53", user_name="Lucas Milas", user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", products=[{"product_name": "Cimento (400mL)","product_id": "4081a83a-516f-442c-85e2-b54bfb192e55","quantity": 2}], creation_time_milliseconds=1692061296, restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.READY, total_price=30.00, observation="Capricha no morango", aborted_reason=None),
            Order(order_id="d2b29a41-69a6-4ad8-87b9-2444119fbf66", user_name="Lucas Duez", user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", products=[{"product_name": "Vasco de Frango","product_id": "39c6556c-680a-4c48-a80a-0e4bb53d965e","quantity": 1}], creation_time_milliseconds=1692154782, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.READY, total_price=28.00, observation="Sem Frango", aborted_reason=None),
            Order(order_id="2f8a8827-e8e6-4273-8587-e4a93da66bef", user_name="Vitor Sollas", user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae5",products=[{"product_name": "Toddynho","product_id": "3a707065-a73b-4d24-848b-4dbca8cd4b39","quantity": 1}, {"product_name": "Queijo Quente 02","product_id": "20602c5e-adb3-426a-8176-59fabca63aaf","quantity": 1}], creation_time_milliseconds=1692155608, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.REFUSED, total_price=33.00, observation=None, aborted_reason="Estamos sem Toddynho"),
            Order(order_id="d4c63753-5119-4990-b427-926798499924", user_name="Rodrigo Morales", user_id="93bc6ada-c0d1-7054-66ab-e17414c48af9",products=[{"product_name": "Carteira","product_id": "9589b258-ed44-4c24-b7d6-e96ae221baae","quantity": 3}], creation_time_milliseconds=1692156322, restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.PREPARING, total_price=25.5, observation=None, aborted_reason=None),
            Order(order_id="ceffe392-931c-4f8e-becb-44dfbe39a35f", user_name="João Brancas", user_id="93bc6ada-c0d1-7054-66ab-e17414c48af4",products=[{"product_name": "Peixe a Dore (Pescada Branca)","product_id": "04a65d3f-a7f7-4161-ac7b-50d139946d2e","quantity": 1}], creation_time_milliseconds=1692156623, restaurant=RESTAURANT.HORA_H, status=STATUS.PREPARING, total_price=38.00, observation="Meus acompanhamentos serão Salada de Tomate e Queijo Branco Temperado com Beringela Caponata", aborted_reason=None),
            Order(order_id="8f90159a-5b53-4b7d-84d5-e0b0e9e16c28", user_name="José", user_id="93bc6ada-c0d1-7054-66ab-e17414c48af1",products=[{"product_name": "Parmegiana de Carne (Molho de tomate caseiro)","product_id": "7a425df8-6d4d-4f3a-b69b-3ae9b7c6ab96","quantity": 1}], creation_time_milliseconds=1692156833, restaurant=RESTAURANT.HORA_H, status=STATUS.REFUSED, total_price=39.00, observation="Vou querer com Arroz Integral, Creme de Milho e Mix Legumes", aborted_reason="São apenas 2 acompanhamentos"),
            Order(order_id="f60615cc-d1cd-41d5-8ff2-7406ee5fd214", user_name="Fernandão", user_id="d05bbfae-c06b-4d99-ac03-28945e6c30f3",products=[{"product_name": "Croissant de Frango com Catupiry","product_id": "aaddfbd0-136c-4824-a12b-005ff6729a42","quantity": 2}], creation_time_milliseconds=1692157097, restaurant=RESTAURANT.CANTINA_DO_MOLEZA, status=STATUS.CANCELLED, total_price=17.00, observation=None, aborted_reason="Minha aula já está prestes a começar! :( "),
            Order(order_id="9e0cdcc8-a27b-470a-975e-7f173d9390d0", user_name="Lukita", user_id="551a2637-3aae-42ef-a7e3-c8d6e3353e1c",products=[{"product_name": "Churrasco","product_id": "e1027314-13aa-44a2-87be-e66eb9307765","quantity": 1}, {"product_name": "Refrigerante Lata","product_id": "29f360d0-fd00-4ae1-8b24-e00f37624b02","quantity": 1}], creation_time_milliseconds=1692157371, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.REFUSED, total_price=30.00, observation=None, aborted_reason="Estamos fechando!"),
            Order(order_id="8309d903-55ce-4299-9c70-13fa2e03bcdc", user_name="Laura Carolina", user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",products=[{"product_name": "Fritas Gde Simples","product_id": "82c875f0-378a-4996-89cd-231311c093fb","quantity": 1}], creation_time_milliseconds=1692157436, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.PENDING, total_price=24.00, observation=None, aborted_reason=None),
            Order(order_id="135ef881-1b1f-4f38-a662-8ff7156e6c27", user_name="Julião", user_id="34c82913-2942-4d55-9e64-489e79574948",products=[{"product_name": "Pão de Queijo","product_id": "0165b801-04c5-41b7-82bb-10f1501333ae","quantity": 2}, {"product_name": "Capuccino - gde.","product_id": "4e6979d6-c9c3-438e-9b8c-e4d799358720","quantity": 1}, {"product_name": "Paçoquita","product_id": "79e2706e-7621-43ab-b6d1-82aeb45fc57c","quantity": 3}], creation_time_milliseconds=1692157822, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.PENDING, total_price=35.5, observation=None, aborted_reason=None)
        ]

    def create_order(self, order: Order) -> Order:
        self.orders.append(order)
        return order