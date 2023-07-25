from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .update_product_usecase import UpdateProductUsecase
from .update_product_viewmodel import UpdateProductViewmodel
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound


class UpdateProductController:
    def __init__(self, usecase: UpdateProductUsecase):
        self.UpdateProductUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            
            if request.data.get("product").get("restaurant") is None:
                raise MissingParameters("restaurant")

            restaurant = request.data.get("product").get('restaurant')
            if restaurant not in [restaurant_value.value for restaurant_value in RESTAURANT]:
                raise NoItemsFound('restaurant')

            meal_type = request.data.get("product").get('new_meal_type')
            if meal_type not in [meal_type_value.value for meal_type_value in MEAL_TYPE]:
                raise NoItemsFound('new_meal_type')
            
            if request.data.get("product").get("product_id") is None:
                raise MissingParameters("product_id")

            product = self.UpdateProductUsecase(
                product_id=str(request.data.get("product").get("product_id")),
                restaurant=RESTAURANT[restaurant],
                new_available=bool(request.data.get("product").get("new_available")),
                new_price=float(request.data.get("product").get("new_price")),
                new_name=str(request.data.get("product").get("new_name")),
                new_description=str(request.data.get("product").get("new_description")),
                new_prepare_time=int(request.data.get("product").get("new_prepare_time")),
                new_meal_type=MEAL_TYPE(request.data.get("product").get("new_meal_type")),
                new_photo=str(request.data.get("product").get("new_photo")),
                user_id=str(requester_user.user_id))
            
            viewmodel = UpdateProductViewmodel(product=product)

            return OK(viewmodel.to_dict())
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
