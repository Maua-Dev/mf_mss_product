from src.shared.helpers.errors.usecase_errors import NoItemsFound, UserNotAllowed, UnregisteredUser
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .update_product_usecase import UpdateProductUsecase
from .update_product_viewmodel import UpdateProductViewmodel
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound, Forbidden


class UpdateProductController:
    def __init__(self, usecase: UpdateProductUsecase):
        self.UpdateProductUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            product_id = request.data.get("product_id")
            restaurant = request.data.get("restaurant")
            new_avaible = request.data.get("new_available")
            new_price = request.data.get("new_price")
            new_name = request.data.get("new_name")
            new_description = request.data.get("new_description")
            new_meal_type = request.data.get("new_meal_type")
            new_photo = request.data.get("new_photo")

            new_prepare_time = -1     # Since prepare time can be none, I am dealing with it in a different way
            if 'new_prepare_time' in request.data.keys():
                new_prepare_time = request.data.get('new_prepare_time')
                if new_prepare_time is not None:
                    new_prepare_time = int(new_prepare_time)

            if product_id is None:
                raise MissingParameters('product_id')

            if restaurant is None:
                raise MissingParameters('restaurant')

            restaurants = list()
            for item in RESTAURANT:
                restaurants.append(item.value)

            if restaurant.value not in restaurants:
                raise NoItemsFound("restaurant")

            meal_types = list()
            for item in MEAL_TYPE:
                meal_types.append(item.value)

            if new_meal_type is not None and new_meal_type.value not in meal_types:
                raise NoItemsFound("new_meal_type")

            product = self.UpdateProductUsecase(
                product_id=str(product_id),
                restaurant=RESTAURANT(restaurant),
                new_available=bool(new_avaible) if new_avaible is not None else None,
                new_price=float(new_price) if new_price is not None else None,
                new_name=str(new_name) if new_name is not None else None,
                new_description=str(new_description) if new_description is not None else None,
                new_prepare_time=new_prepare_time,
                new_meal_type=MEAL_TYPE(new_meal_type) if new_meal_type is not None else None,
                new_photo=str(new_photo) if new_photo is not None else None,
                user_id=requester_user.user_id
            )

            viewmodel = UpdateProductViewmodel(product=product)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)

        except UnregisteredUser as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
