from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import UnregisteredEmployee, UnregisteredUser, UserNotAllowed
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_all_active_orders_by_restaurant_usecase import GetAllActiveOrdersByRestaurantUsecase 

from .get_all_active_orders_by_restaurant_viewmodel import GetAllActiveOrdersByRestaurantViewmodel

from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import Forbidden, InternalServerError, OK, BadRequest
from src.shared.helpers.errors.domain_errors import EntityError


class GetAllActiveOrdersByRestaurantController:
    def __init__(self, usecase: GetAllActiveOrdersByRestaurantUsecase):
        self.GetAllActiveOrdersByRestaurantUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            all_active_orders = self.GetAllActiveOrdersByRestaurantUsecase(user_id=requester_user.user_id)
            
            viewmodel = GetAllActiveOrdersByRestaurantViewmodel(all_active_orders=all_active_orders)

            return OK(viewmodel.to_dict())

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)
        
        except UnregisteredUser as err:
            return BadRequest(body=err.message)
        
        except UnregisteredEmployee as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])