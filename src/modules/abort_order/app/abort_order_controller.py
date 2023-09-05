from .abort_order_usecase import AbortOrderUsecase
from .abort_order_viewmodel import AbortOrderViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterExcededMaximumValue, \
    EntityParameterError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, InternalServerError, NotFound, OK, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.helpers.errors.usecase_errors import UserNotAllowed, UnregisteredUser, NoItemsFound, \
    UserNotRelatedToRestaurant


class AbortOrderController:

    def __init__(self, usecase: AbortOrderUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get("order_id") is None:
                raise MissingParameters("order_id")
            order_id = request.data.get("order_id")

            if request.data.get("aborted_reason") is None:
                raise MissingParameters("aborted_reason")
            aborted_reason = request.data.get("aborted_reason")

            order = self.usecase(
                order_id=order_id,
                user_id=requester_user.user_id,
                new_aborted_reason=aborted_reason,
            )
            viewmodel = AbortOrderViewmodel(order)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)

        except UserNotRelatedToRestaurant as err:
            return Forbidden(body=err.message)

        except EntityParameterExcededMaximumValue as err:
            return BadRequest(body=err.message)

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except UnregisteredUser as err:
            return BadRequest(body=err.message)

        except EntityParameterError as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])


