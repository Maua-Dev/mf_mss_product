import os
from typing import Any

from src.shared.helpers.errors.usecase_errors import NoItemsFound, UserNotAllowed
from .manage_connection_usecase import ManageConnectionUsecase
from .manage_connection_viewmodel import ManageConnectionViewmodel
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.controller_errors import MissingParameters, RestaurantNotFound, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
import requests


class ManageConnectionController:

    def __init__(self, usecase: ManageConnectionUsecase):
        self.ManageConnectionUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('connection_id') is None:
                raise MissingParameters('connection_id')

            auth = request.data.get('Authorization')

            if request.data.get('restaurant') is None:
                raise MissingParameters("restaurant")

            restaurant = request.data.get('restaurant')
            if restaurant not in [restaurant_value.value for restaurant_value in RESTAURANT]:
                raise RestaurantNotFound(restaurant)

            requested_user = requests.get(os.getenv('GET_USER_URL'), headers={'Authorization': auth}).json()

            if requested_user.get('user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(requested_user.get('user'))

            if request.data.get('api_id') is None:
                raise MissingParameters('api_id')

            connection = self.ManageConnectionUsecase(connection_id=str(request.data.get('connection_id')), 
                                                      api_id=str(request.data.get('api_id')), 
                                                      user_id=str(requester_user.user_id), 
                                                      restaurant=RESTAURANT[restaurant],
                                                      route_key=str(request.data.get('route_key')))

            viewmodel = ManageConnectionViewmodel(connection)

            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except RestaurantNotFound as err:
            return NotFound(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except UserNotAllowed as err:
            return NotFound(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])