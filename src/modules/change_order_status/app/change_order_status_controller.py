from .change_order_status_usecase import ChangeOrderStatusUsecase
from .change_order_status_viewmodel import ChangeOrderViewmodel
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterError, \
    EntityParameterExcededMaximumValue
from src.shared.helpers.errors.usecase_errors import UserNotAllowed, UnregisteredUser, NoItemsFound, \
    UserNotRelatedToRestaurant
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class ChangeOrderStatusController:
    def __init__(self, usecase: ChangeOrderStatusUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get("order_id") is None:
                raise MissingParameters("order_id")

            order_id = request.data.get("order_id")

            if request.data.get('new_status') is None:
                raise MissingParameters("new_status")
            new_status = STATUS[request.data.get('new_status')]

            order = self.usecase(
                order_id=order_id,
                user_id=requester_user.user_id,
                new_status=new_status
            )
            viewmodel = ChangeOrderViewmodel(order)

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
