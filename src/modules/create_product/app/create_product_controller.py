from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterError, \
    EntityParameterExcededMaximumValue
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from .create_product_usecase import CreateProductUsecase
from .create_product_viewmodel import CreateProductViewmodel
from src.shared.domain.entities.product import Product
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import Forbidden, InternalServerError, BadRequest, Created
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class CreateProductController:

    def __init__(self, usecase: CreateProductUsecase):
        self.CreateProductUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get("available") is None:
                raise MissingParameters("available")

            if request.data.get("price") is None:
                raise MissingParameters("price")

            if request.data.get("name") is None:
                raise MissingParameters("name")

            if request.data.get("description") is None:
                raise MissingParameters("description")

            if request.data.get("meal_type") is None:
                raise MissingParameters("meal_type")

            meal_type = request.data.get('meal_type')
            if meal_type not in [meal_type_value.value for meal_type_value in MEAL_TYPE]:
                raise EntityError('meal_type')

            if request.data.get('restaurant') is None:
                raise MissingParameters("restaurant")

            restaurant = request.data.get('restaurant')
            if restaurant not in [restaurant_value.value for restaurant_value in RESTAURANT]:
                raise EntityError('restaurant')

            if type(request.data.get("prepare_time")) == int and request.data.get("prepare_time") < 0:
                raise EntityParameterError("prepare_time can't be less than zero")

            product = self.CreateProductUsecase(available=request.data.get("available"),
                                                price=float(request.data.get("price")) if type(request.data.get("price")) == int else request.data.get("price"),
                                                name=request.data.get("name"),
                                                description=request.data.get("description"),
                                                meal_type=MEAL_TYPE[meal_type],
                                                photo=request.data.get("photo"),
                                                restaurant=RESTAURANT[restaurant],
                                                prepare_time=int(request.data.get("prepare_time")) if type(request.data.get("prepare_time")) == int else request.data.get("prepare_time"),
                                                user_id=requester_user.user_id)

            viewmodel = CreateProductViewmodel(product=product)

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

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
