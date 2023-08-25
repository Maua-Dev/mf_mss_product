from typing import List
from src.modules.create_order.app.create_order_usecase import CreateOrderUsecase
from src.modules.create_order.app.create_order_viewmodel import CreateOrderViewmodel
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class CreateOrderController:

    def __init__(self, usecase: CreateOrderUsecase):
        self.CreateOrderUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            products = request.data.get("products")
            if products is None:
                raise MissingParameters("products")
            
            products_list = list()
            for product in products:
                
                product_name = product["product_name"]
                product_id = product["product_id"]
                quantity = product["quantity"]

                products_list.append(OrderProduct(product_name, product_id, quantity))

            if request.data.get('restaurant') is None:
                raise MissingParameters("restaurant")

            restaurant = request.data.get('restaurant')
            if restaurant not in [restaurant_value.value for restaurant_value in RESTAURANT]:
                raise NoItemsFound('restaurant')
            
            order = self.CreateOrderUsecase(user_name=str(requester_user.name),
                                            user_id=str(requester_user.user_id),
                                            products=list(products_list),
                                            restaurant=RESTAURANT[restaurant],
                                            obervation=str(request.data.get('observation'))
                                            )
            
            viewmodel = CreateOrderViewmodel(order)

            return Created(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
