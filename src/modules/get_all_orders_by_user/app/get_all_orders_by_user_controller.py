from .get_all_orders_by_user_usecase import GetAllOrdersByUserUsecase
from .get_all_orders_by_user_viewmodel import GetAllOrdersByUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UserNotOrderOwner, NoItemsFound, UnregisteredUser
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class GetAllOrdersByUserController:
    def __init__(self, usecase: GetAllOrdersByUserUsecase):
        self.GetAllOrdersByUserUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            all_orders = self.GetAllOrdersByUserUsecase(user_id=requester_user.user_id, exclusive_start_key=request.data.get('exclusive_start_key'), amount=request.data.get('amount', 20))

            viewmodel = GetAllOrdersByUserViewmodel(all_orders)

            return OK(viewmodel.to_dict())
        
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except UnregisteredUser as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except UserNotOrderOwner as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])