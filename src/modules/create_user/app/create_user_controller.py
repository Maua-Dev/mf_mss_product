from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .create_user_usecase import CreateUserUsecase
from .create_user_viewmodel import CreateUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import BadRequest, InternalServerError, Created

class CreateUserController:

    def __init__(self, usecase: CreateUserUsecase):
        self.CreateUserUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            
            user = self.CreateUserUsecase(
                name = requester_user.name,
                email= requester_user.email,
                user_id=requester_user.user_id
            )

            viewmodel = CreateUserViewmodel(user)
            
            return Created(viewmodel.to_dict())

        except MissingParameters as err:   
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])
