from src.modules.get_user.app.get_user_usecase import GetUserUseCase
from src.modules.get_user.app.get_user_viewmodel import GetUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import BadRequest, NotFound, InternalServerError, OK
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class GetUserController:
    def __init__(self, usecase: GetUserUseCase):
        self.usecase = usecase

    def __call__(self, request: IRequest):
        try:
            requester_user: UserApiGatewayDTO = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if requester_user.user_id is None:
                raise MissingParameters("user_id")
            
            user = self.usecase(user_id=requester_user.user_id)

            user_viewmodel = GetUserViewmodel(user).to_dict()

            return OK(user_viewmodel)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
