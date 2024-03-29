import json
import os

from src.shared.helpers.errors.usecase_errors import NoItemsFound, UserNotAllowed
from .manage_connection_usecase import ManageConnectionUsecase
from .manage_connection_viewmodel import ManageConnectionViewmodel
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.controller_errors import MissingParameters, RestaurantNotFound, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
import boto3

class ManageConnectionController:

    def __init__(self, usecase: ManageConnectionUsecase):
        self.ManageConnectionUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('connection_id') is None:
                raise MissingParameters('connection_id')

            if request.data.get('route_key') is None:
                raise MissingParameters('route_key')

            requester_user = None

            if request.data.get('route_key') == '$connect':
            
                if request.data.get('requester_user') is None:

                    raise MissingParameters('requester_user')

                requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get('api_id') is None:
                raise MissingParameters('api_id')

            connection = self.ManageConnectionUsecase(connection_id=str(request.data.get('connection_id')),
                                                      api_id=str(request.data.get('api_id')),
                                                      user_id=str(requester_user.user_id) if requester_user is not None else None,
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
            print(err)
            return InternalServerError(body=err.args[0])
