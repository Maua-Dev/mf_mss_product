from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import UnregisteredEmployee, UnregisteredUser, UserNotAllowed, NoItemsFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_schedule_by_id_usecase import GetScheduleByIdUsecase 

from .get_schedule_by_id_viewmodel import GetScheduleByIdViewmodel

from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import Forbidden, InternalServerError, OK, BadRequest, NotFound
from src.shared.helpers.errors.domain_errors import EntityError



class GetScheduleByIdController:
    def __init__(self, usecase: GetScheduleByIdUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get('schedule_id') is None:
                raise MissingParameters('schedule_id')

            schedule_id = request.data.get('schedule_id')

            schedule = self.usecase(user_id= requester_user.user_id, schedule_id=schedule_id)

            viewmodel = GetScheduleByIdViewmodel(schedule=schedule)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except UnregisteredUser as err:
            return NotFound(body=err.message)

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
