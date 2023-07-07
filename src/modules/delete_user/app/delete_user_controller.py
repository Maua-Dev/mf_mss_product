from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.modules.delete_user.app.delete_user_viewmodel import DeleteUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class DeleteUserController:
    def __init__(self, usecase: DeleteUserUsecase):
        self.DeleteUserUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            user = self.DeleteUserUsecase(user_id=requester_user.user_id)

            viewmodel = DeleteUserViewmodel(user=user)

            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:   
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])
        