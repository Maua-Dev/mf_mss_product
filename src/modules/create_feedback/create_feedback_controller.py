from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterError, \
    EntityParameterExcededMaximumValue, EntityParameterHaveMinValue
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from .create_feedback_usecase import CreateFeedbackUsecase
from .create_feedback_viewmodel import CreateFeedbackViewmodel
from src.shared.domain.entities.feedback import Feedback
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import Forbidden, InternalServerError, BadRequest, Created
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO

class CreateFeedbackController:

    def __init__(self, usecase: CreateFeedbackUsecase):
        self.CreateFeedbackUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get("order_id") is None:
                raise MissingParameters("order_id")

            if request.data.get('restaurant') is None:
                raise MissingParameters("restaurant")

            restaurant = request.data.get('restaurant')
            if restaurant not in [restaurant_value.value for restaurant_value in RESTAURANT]:
                raise EntityError('restaurant')

            if request.data.get("value") is None:
                raise MissingParameters("value")

            if type(request.data.get("value")) == int and request.data.get("value") < 1:
                raise EntityParameterError("value can't be less than one")
            
            if type(request.data.get("value")) == int and request.data.get("value") > 5:
                raise EntityParameterError("value can't be more than five")

            feedback = self.CreateFeedbackUsecase(order_id=request.data.get("order_id"),
                                                  user_id=requester_user.user_id,
                                                  restaurant=RESTAURANT[restaurant],
                                                  value=int(request.data.get("value"))
                                                )

            viewmodel = CreateFeedbackViewmodel(feedback=feedback)

            return Created(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)
        
        except UnregisteredUser as err:
            return BadRequest(body=err.message)

        except EntityParameterError as err:
            return BadRequest(body=err.message)

        except EntityParameterExcededMaximumValue as err:
            return BadRequest(body=err.message)
        
        except EntityParameterHaveMinValue as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])