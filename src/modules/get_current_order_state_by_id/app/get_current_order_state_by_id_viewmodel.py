from src.shared.domain.entities.order import Order
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.action_enum import ACTION


class OrderStatusViewmodel:
    current_status: STATUS
    action: ACTION

    def __init__(self, order: Order):
        self.order_id = order.order_id
        self.current_status = order.status
        self.aborted_reason = order.aborted_reason
        self.action = order.action

    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "status": self.current_status.value,
            "aborted_reason": self.aborted_reason,
            "action": self.action.value
        }


class GetCurrentOrderStateViewmodel:
    def __init__(self, order: Order):
        self.order_status_viewmodel = OrderStatusViewmodel(order)

    def to_dict(self):
        return {
            "order": self.order_status_viewmodel.to_dict(),
            "message": "the order status object was retrieved"
        }
