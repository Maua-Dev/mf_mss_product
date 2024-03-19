from .get_average_feedback_by_restaurant_usecase import GetAverageFeedbackByRestaurantUsecase

from src.shared.helpers.external_interfaces.http_codes import *
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse


class GetAverageFeedbackByRestaurantController:
    def __init__(self, usecase: GetAverageFeedbackByRestaurantUsecase):
        self.GetAverageFeedbackByRestaurantUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            if requester_user is None:
                raise MissingParameters('requester_user')

            average_feedback = self.GetAverageFeedbackByRestaurantUsecase(requester_user.user_id)
            return OK(average_feedback)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except UnregisteredUser as err:
            return BadRequest(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])