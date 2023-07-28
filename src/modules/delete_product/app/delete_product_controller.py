from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.usecase_errors import UserNotAllowed
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .delete_product_viewmodel import DeleteProductViewmodel
from .delete_product_usecase import DeleteProductUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import Forbidden, InternalServerError, OK, BadRequest, NotFound


class DeleteProductController:
    def __init__(self, usecase: DeleteProductUsecase):
        self.DeleteProductUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get("product").get("restaurant") is None:
                raise MissingParameters("restaurant")

            restaurant = request.data.get("product").get('restaurant')
            if restaurant not in [restaurant_value.value for restaurant_value in RESTAURANT]:
                raise EntityError('restaurant')
            
            if request.data.get("product").get("product_id") is None:
                raise MissingParameters("product_id")

            product = self.DeleteProductUsecase(
                product_id=request.data.get("product").get("product_id"),
                restaurant=RESTAURANT[restaurant],
                user_id=requester_user.user_id)
            
            viewmodel = DeleteProductViewmodel(product=product)
            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except UserNotAllowed as err:
            return Forbidden(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])

