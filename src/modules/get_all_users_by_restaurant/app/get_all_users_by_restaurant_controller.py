from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_usecase import GetAllUsersByRestaurantUseCase
from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_viewmodel import GetAllUsersByRestaurantViewModel
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.controller_errors import MissingParameters, RestaurantNotFound, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Conflict, Forbidden, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class GetAllUsersByRestaurantController:
    def __init__(self, usecase: GetAllUsersByRestaurantUseCase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get("restaurant") is None:
                raise MissingParameters('restaurant')

            restaurant = request.data.get('restaurant')
            if restaurant not in [restaurant_value.value for restaurant_value in RESTAURANT]:
                raise RestaurantNotFound(restaurant)
            
            users = self.usecase(
                user_id=requester_user.user_id, 
                restaurant=restaurant
            ) #como o usuario ira criar um restaurante, ta certo passar pelo requester_user?

            viewmodel = GetAllUsersByRestaurantViewModel(users=users)
            
            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except UserNotAllowed as error:
            return Forbidden(body=error.message)
        
        except UnregisteredUser as error:
            return Conflict(body=error.message)
        
        except WrongTypeParameter as error:
            return BadRequest(body=error.message)
        
        except EntityError as error:
            return BadRequest(body=error.message)
        
        except RestaurantNotFound as error:
            return NotFound(body=error.message)
        
        except Exception as error:
            return InternalServerError(body=error.args[0])