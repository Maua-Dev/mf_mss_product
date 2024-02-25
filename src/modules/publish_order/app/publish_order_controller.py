from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.action_enum import ACTION
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.external_interfaces.dynamo_event_parser import DynamoEventParser
from src.shared.helpers.external_interfaces.external_interface import IResponse
from .publish_order_usecase import PublishOrderUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import BadRequest, InternalServerError, OK

class PublishOrderController:

    def __init__(self, usecase: PublishOrderUsecase):
        self.PublishOrderUsecase = usecase

    def __call__(self, request: DynamoEventParser) -> IResponse:
        try:
            
            if request.data.get('all_records') is None:
                raise MissingParameters('all_records')
                
            if len(request.data.get('all_records')) <= 0:
                return BadRequest(body="There is no record")
            
            first_record = request.data.get('all_records')[0]

            order_dict = first_record["new_image"]
            products_dict_list = first_record["new_image"]["products"] 
            
            products = [OrderProduct(product_id=product["product_id"], product_name=product["product_name"], quantity = int(product["quantity"]), observation=product.get("observation")) for product in products_dict_list]

            order = Order(order_id=order_dict["order_id"],
                          user_name=order_dict["user_name"],
                          user_id=order_dict["user_id"],
                          products=products,
                          creation_time_milliseconds=int(order_dict["creation_time_milliseconds"]),
                          restaurant=RESTAURANT(order_dict["restaurant"]),
                          status=STATUS(order_dict["status"]),
                          action=ACTION(order_dict["action"]),
                          total_price=float(order_dict["total_price"]),
                          last_status_update_milliseconds=int(order_dict.get("last_status_update_milliseconds")) if order_dict.get("last_status_update_milliseconds") is not None else None,
                          aborted_reason=order_dict.get("aborted_reason"))

            publish_order = self.PublishOrderUsecase(order=order)
            response = {"message":f"The order {order.order_id} was published"}

            return OK(response)

        except MissingParameters as err:   
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])