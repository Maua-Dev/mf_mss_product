from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_usecase import \
    GetCurrentOrderStateByIdUsecase
from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_viewmodel import \
    GetCurrentOrderStateViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotOrderOwner
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import BadRequest, InternalServerError, OK, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class GetCurrentOrderStateByIdController:
    def __init__(self, usecase: GetCurrentOrderStateByIdUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest):
        try:
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            order_id = request.data.get('order_id')

            order = self.usecase(order_id=order_id, user_id=requester_user.user_id)

            order_status_viewmodel = GetCurrentOrderStateViewmodel(order).to_dict()

            return OK(order_status_viewmodel)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except UnregisteredUser as err:
            return BadRequest(body=err.message)

        except UserNotOrderOwner as err:
            return Forbidden(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
