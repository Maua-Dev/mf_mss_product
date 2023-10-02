from src.modules.change_order_by_id.app.change_order_by_id_viewmodel import ChangeOrderByIdViewmodel
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS


class Test_ChangeOrderViewmodel:
    def test_change_order_status_viewmodel(self):
        order = Order(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Lucas Milas",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf",
            products=[
                OrderProduct(product_name='Hot Dog', product_id="c4bb21ac-d9f6-4d4b-b56c-215fb0f7aa09", quantity=2)],
            creation_time_milliseconds=1692061296,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=30.00,
            observation="Capricha no morango",
            aborted_reason=None,
            last_status_update_milliseconds=1692061896
        )

        order_viewmodel = ChangeOrderByIdViewmodel(order=order).to_dict()

        expected = {
            "order": {
                "order_id": "b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                "user_name": "Lucas Milas",
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                "products": [{
                    "product_name": "Hot Dog",
                    "product_id": "c4bb21ac-d9f6-4d4b-b56c-215fb0f7aa09",
                    "quantity": 2
                }],
                "creation_time_milliseconds": 1692061296,
                "restaurant": "CANTINA_DO_MOLEZA",
                "observation": "Capricha no morango",
                "status": "READY",
                "aborted_reason": None,
                "total_price": 30.00,
                "last_status_update": 1692061896
            },
            "message": "the order was updated"
        }

        assert expected == order_viewmodel
