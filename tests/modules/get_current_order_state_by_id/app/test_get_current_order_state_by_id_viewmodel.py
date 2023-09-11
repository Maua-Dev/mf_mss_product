from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_viewmodel import \
    GetCurrentOrderStateViewmodel
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_GetCurrentOrderStateViewmodel:
    def test_viewmodel(self):
        order_repo = OrderRepositoryMock()
        order = order_repo.orders[-1]

        viewmodel = GetCurrentOrderStateViewmodel(order).to_dict()
        expected = {
            "order": {
                "order_id": order.order_id,
                "order_status": order.status
            },
            "message": "the order status object was retrieved"
        }

        assert viewmodel == expected

