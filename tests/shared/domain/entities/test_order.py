import pytest

from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.action_enum import ACTION
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Order:
    def test_order(self):
        order = Order(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Lucas Milas",
            user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
            products=[
                OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da', quantity=2, observation="2 saladinhas fresca")],
            creation_time_milliseconds=1692061296,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            status=STATUS.PENDING,
            total_price=35.00,
            aborted_reason=None,
            last_status_update_milliseconds=1692061296,
            action=ACTION.NEW
        )

        assert type(order) == Order
        assert order.order_id == "b3f6c5aa-80ad-4f95-ae16-455b4f87fb53"
        assert order.user_name == "Lucas Milas"
        assert order.user_id == "f15d32eb-403f-46a4-8efc-804d9f8bed0f"
        assert order.products[0].product_name == "Saladinha"
        assert order.products[0].product_id == "305c486c-ce77-423d-97c1-1710a4c302da"
        assert order.products[0].quantity == 2
        assert order.products[0].observation == "2 saladinhas fresca"
        assert order.creation_time_milliseconds == 1692061296
        assert order.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert order.status == STATUS.PENDING
        assert order.total_price == 35
        assert order.last_status_update_milliseconds == 1692061296
        assert order.action == ACTION.NEW

    def test_several_orders(self):
        order = Order(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Lucas Milas",
            user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
            products=[
                OrderProduct(product_name="Saladinha", product_id="305c486c-ce77-423d-97c1-1710a4c302da", quantity=2),

                OrderProduct(product_name="Coquinha Gelada", product_id="deab0b72-c97f-4626-9f60-1111a1436d73",
                             quantity=1, observation="Coquinha bem gelada!"),

                OrderProduct(product_name="Vasco Delicia", product_id="bbab90c4-769c-4a31-885d-f5ac374b59fe",
                             quantity=3)
            ],
            creation_time_milliseconds=1692061296,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            status=STATUS.PENDING,
            total_price=35.00,
            aborted_reason=None,
            last_status_update_milliseconds=1692061296,
            action=ACTION.NEW
        )

        assert type(order) == Order
        assert order.order_id == "b3f6c5aa-80ad-4f95-ae16-455b4f87fb53"
        assert order.user_name == "Lucas Milas"
        assert order.user_id == "f15d32eb-403f-46a4-8efc-804d9f8bed0f"
        assert order.products[0].product_name == "Saladinha"
        assert order.products[1].product_id == "deab0b72-c97f-4626-9f60-1111a1436d73"
        assert order.products[2].quantity == 3
        assert order.creation_time_milliseconds == 1692061296
        assert order.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert order.status == STATUS.PENDING
        assert order.total_price == 35
        assert order.action == ACTION.NEW

    def test_invalid_id(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id=666,
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da', 
                                       quantity=2, observation="2 saladinhas fresca")],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_wrong_length_id(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2, observation="2 saladinhas fresca")],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_invalid_name(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name=True,
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2, observation="2 saladinhas fresca")],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_invalid_name_lenght(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lu",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2, observation="2 saladinhas fresca")],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_invalid_name_characters(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="L#c@s M!l*$",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2, observation="2 saladinhas fresca")],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_products_is_not_in_a_list(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                      quantity=2, observation="2 saladinhas fresca"),
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_invalid_creation_time_milliseconds(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2, observation="2 saladinhas fresca")],
                creation_time_milliseconds="1692061296",
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_invalid_restaurant(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2, observation="2 saladinhas fresca")],
                creation_time_milliseconds=1692061296,
                restaurant=STATUS.PREPARING,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_aborted_reason_not_none(self):
        order = Order(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Lucas Milas",
            user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
            products=[
                OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da', quantity=2, observation="2 saladinhas fresca")],
            creation_time_milliseconds=1692061296,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            status=STATUS.PENDING,
            total_price=35.00,
            aborted_reason="Vai rolar não",
            last_status_update_milliseconds=1692061296,
            action=ACTION.NEW
        )

        assert order.aborted_reason == "Vai rolar não"

    def test_invalid_status(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2)],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=RESTAURANT.CANTINA_DO_MOLEZA,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_invalid_price(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2)],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price="35",
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )

    def test_invalid_products(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[
                    {"product_name": "Saladinha", "product_id": "305c486c-ce77-423d-97c1-1710a4c302da", "quantity": 2}],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=ACTION.NEW
            )
        
    def test_invalid_action(self):
        with pytest.raises(EntityError):
            order = Order(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_name="Lucas Milas",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                products=[OrderProduct(product_name='Saladinha', product_id='305c486c-ce77-423d-97c1-1710a4c302da',
                                       quantity=2)],
                creation_time_milliseconds=1692061296,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                status=STATUS.PENDING,
                total_price=35.00,
                aborted_reason=None,
                last_status_update_milliseconds=1692061296,
                action=2
            )
