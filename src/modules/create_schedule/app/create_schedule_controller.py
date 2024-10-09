from datetime import datetime, time
from src.modules.create_schedule.app.create_schedule_usecase import CreateScheduleUsecase

from src.modules.create_schedule.app.create_schedule_viewmodel import CreateScheduleViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, RestaurantNotFound, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError

from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Conflict, Created, Forbidden, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.http_models import HttpResponse
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO

from src.shared.domain.enums.restaurant_enum import RESTAURANT

class CreateScheduleController:
    def __init__(self, create_schedule_use_case: CreateScheduleUsecase):
        self.CreateScheduleUsecase = create_schedule_use_case

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get("schedule_id") is None:
                raise MissingParameters('schedule_id')
            
            if type(request.data.get("schedule_id")) != str:
                raise EntityError('schedule_id')
            
            if request.data.get("initial_time") is None:
                raise MissingParameters('initial_time')
            
            if type(request.data.get("initial_time")) != str:
                raise EntityError('initial_time')
            
            initial_time = datetime.strptime(request.data.get('initial_time'), "%H:%M:%S").time()

            if request.data.get("end_time") is None:
                raise MissingParameters('end_time')
            
            if type(request.data.get("end_time")) != str:
                raise EntityError('end_time')
            
            end_time = datetime.strptime(request.data.get('end_time'), "%H:%M:%S").time()
            
            schedule = self.CreateScheduleUsecase(
                                        initial_time=initial_time,
                                        end_time=end_time,
                                        user_id=requester_user.user_id
                                    )
            
            viewmodel = CreateScheduleViewmodel(schedule=schedule)

            return Created(viewmodel.to_dict())
        
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

            
            