from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.helpers.errors.controller_errors import MissingParameters
from .get_all_orders_by_restaurant_usecase import GetAllOrdersByRestaurantUsecase
from .get_all_orders_by_restaurant_viewmodel import GetAllOrdersByRestaurantViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.errors.usecase_errors import UnregisteredEmployee, UnregisteredUser, UserNotAllowed
from src.shared.helpers.external_interfaces.http_codes import Forbidden, InternalServerError, OK, BadRequest


class GetAllOrdersByRestaurantController:
    def __init__(self, usecase: GetAllOrdersByRestaurantUsecase):
        self.GetAllOrdersByRestaurantUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            all_orders = self.GetAllOrdersByRestaurantUsecase(user_id=requester_user.user_id,
                                                              order_id=request.data.get('order_id'))

            viewmodel = GetAllOrdersByRestaurantViewmodel(all_orders=all_orders)

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
