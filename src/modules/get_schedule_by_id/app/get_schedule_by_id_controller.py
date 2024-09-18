from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import UnregisteredEmployee, UnregisteredUser, UserNotAllowed
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_schedule_by_id_usecase import GetScheduleByIdUsecase 

from .get_schedule_by_id_viewmodel import ScheduleByIdViewmodel

from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import Forbidden, InternalServerError, OK, BadRequest
from src.shared.helpers.errors.domain_errors import EntityError


class GetScheduleByIdController:
    def __init__(self, usecase: GetScheduleByIdUsecase):
        self.GetScheduleByIdUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            schedule = self.GetScheduleByIdUsecase(user_id=requester_user.user_id)
            
            viewmodel = ScheduleByIdViewmodel(schedule=schedule)

            return OK(viewmodel.to_dict())

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)
        
        except UnregisteredUser as err:
            return BadRequest(body=err.message)
        
        except UnregisteredEmployee as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])