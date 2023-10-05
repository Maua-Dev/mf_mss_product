from src.modules.abort_order.app.abort_order_viewmodel import AbortOrderViewmodel
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS


class Test_AbortOrderViewmodel:
    def test_abort_order_viewmodel(self):
        order = Order(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Felipe Carillo",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf",
            products=[
                OrderProduct(product_name='Hot Dog', product_id="c4bb21ac-d9f6-4d4b-b56c-215fb0f7aa09", quantity=2)],
            creation_time_milliseconds=2799764896,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            status=STATUS.PENDING,
            total_price=30.00,
            aborted_reason="Desisti da compra!",
            last_status_update_milliseconds=2799764896
        )

        order_viewmodel = AbortOrderViewmodel(order=order).to_dict()

        expected = {
            "order": {
                "order_id": "b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                "user_name": "Felipe Carillo",
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                "products": [{
                    "product_name": "Hot Dog",
                    "product_id": "c4bb21ac-d9f6-4d4b-b56c-215fb0f7aa09",
                    "quantity": 2,
                    "observation": None
                }],
                "creation_time_milliseconds": 2799764896,
                "restaurant": "SOUZA_DE_ABREU",
                "status": "PENDING",
                "aborted_reason": "Desisti da compra!",
                "total_price": 30.00,
                "last_status_update": 2799764896
            },
            "message": "the order was aborted"
        }

        assert expected == order_viewmodel

