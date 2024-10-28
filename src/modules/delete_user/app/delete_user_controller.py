from .delete_user_usecase import DeleteUserUsecase
from .delete_user_viewmodel import DeleteUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class DeleteUserController:
    def __init__(self, usecase: DeleteUserUsecase):
        self.DeleteUserUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            if 'validate_user' not in request.data['requester_user']:
                raise MissingParameters('validate_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            validate_user = request.data.get('requester_user', {}).get('validate_user', False)
            restaurant_name = request.data.get('restaurant')
            restaurant = RESTAURANT[restaurant_name] if restaurant_name else None

            user = self.DeleteUserUsecase(
                user_id=requester_user.user_id, 
                validate_user=validate_user, 
                restaurant=restaurant
                )

            viewmodel = DeleteUserViewmodel(user=user)

            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:   
            return BadRequest(body=f"Missing parameter: {err.message}")
        
        except MissingParameters as err:   
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])
        