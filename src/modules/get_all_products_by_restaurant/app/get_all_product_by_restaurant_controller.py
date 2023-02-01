from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.modules.get_all_products_by_restaurant.app.get_all_product_by_restaurant_usecase import GetAllProductsByRestaurantUsecase
from src.modules.get_all_products_by_restaurant.app.get_all_product_by_restaurant_viewmodel import GetAllProductsByRestaurantViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import InternalServerError, OK, BadRequest, NotFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetAllProductByRestaurantController:
    def __init__(self, usecase: GetAllProductsByRestaurantUsecase):
        self.GetAllProductsByRestaurantUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get("restaurant") is None:
                raise MissingParameters('restaurant')

            restaurants = list()
            for item in RESTAURANT:
                restaurants.append(item.value)

            if request.data.get("restaurant") not in restaurants:
                raise EntityError('restaurant')

            all_products = self.GetAllProductsByRestaurantUsecase(
                restaurant=RESTAURANT[request.data.get('restaurant')]
                )
            viewmodel = GetAllProductsByRestaurantViewmodel(all_products=all_products)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])