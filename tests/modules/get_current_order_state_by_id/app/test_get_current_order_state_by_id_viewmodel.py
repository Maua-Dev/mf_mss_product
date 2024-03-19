from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_viewmodel import \
    GetCurrentOrderStateViewmodel
from src.shared.domain.enums.status_enum import STATUS
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_GetCurrentOrderStateViewmodel:
    def test_viewmodel(self):
        order_repo = OrderRepositoryMock()
        order = order_repo.orders[-1]

        viewmodel = GetCurrentOrderStateViewmodel(order).to_dict()
        expected = {
            "order": {
                "order_id": order.order_id,
                "order_status": order.status.value,
                "aborted_reason": None,
                "action": order.action.value
            },
            "message": "the order status object was retrieved"
        }

        assert viewmodel == expected

    def test_order_refused(self):
        order_repo = OrderRepositoryMock()
        order = order_repo.orders[-1]
        order.status = STATUS.REFUSED
        order.aborted_reason = "Certamente tivemos um bom motivo pra cancelar esse pedido :/"

        viewmodel = GetCurrentOrderStateViewmodel(order).to_dict()
        expected = {
            "order": {
                "order_id": order.order_id,
                "order_status": STATUS.REFUSED.value,
                "aborted_reason": order.aborted_reason,
                "action": order.action.value
            },
            "message": "the order status object was retrieved"
        }

        assert viewmodel == expected

