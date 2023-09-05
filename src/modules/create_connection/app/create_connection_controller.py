from typing import Any
from .create_connection_usecase import CreateConnectionUsecase
from .create_connection_viewmodel import CreateConnectionViewmodel
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.controller_errors import MissingParameters, RestaurantNotFound
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.dynamo_event_parser import DynamoEventParser
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class CreateConnectionController:

    def __init__(self, usecase: CreateConnectionUsecase):
        self.CreateConnectionUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
                
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get('connection_id') is None:
                raise MissingParameters('connection_id')
            
            if request.data.get('api_id') is None:
                raise MissingParameters('api_id')
            
            if request.data.get('restaurant') is None:
                raise MissingParameters("restaurant")

            restaurant = request.data.get('restaurant')
            if restaurant not in [restaurant_value.value for restaurant_value in RESTAURANT]:
                raise RestaurantNotFound(restaurant)
            
            connection = self.CreateConnectionUsecase(connection_id=str(request.data.get('connection_id')),
                                                      api_id=str(request.data.get('api_id')),
                                                      user_id=str(requester_user.user_id),
                                                      restaurant=RESTAURANT[restaurant])
            
            viewmodel = CreateConnectionViewmodel(connection)

            return Created(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except RestaurantNotFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])