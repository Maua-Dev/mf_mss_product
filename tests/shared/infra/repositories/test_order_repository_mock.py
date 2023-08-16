from src.shared.domain.entities.order import Order
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_OrderRepositoryMock:
    def test_create_order(self):
        repo = OrderRepositoryMock()
        len_before = len(repo.orders)
        order = Order(
            order_id="1efc0e1a-24ed-4041-a4a0-fe5633711a3f", user_name="Lucas Milas", user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", products=[{"product_name": "Copo da Felicidade","product_id": "4d1716c4-5e51-4d72-ba93-349e31201a22","quantity": 1}], creation_time_milliseconds=1692159350, restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.PENDING, total_price=22.00, observation=None, aborted_reason=None
        )

        repo.create_order(order=order)

        assert len(repo.orders) == len_before + 1
        assert repo.orders[-1] == order
