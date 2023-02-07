from src.shared.domain.enums.restaurant_enum import RESTAURANT
from .delete_products_by_restaurant_viewmodel import DeleteProductsByRestaurantViewmodel
from .delete_products_by_restaurant_usecase import DeleteProductsByRestaurantUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import InternalServerError, OK, BadRequest, NotFound


class DeleteProductsByRestaurantController:
    def __init__(self, usecase: DeleteProductsByRestaurantUsecase):
        self.DeleteProductsByRestaurantUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('product_id') is None:
                raise MissingParameters('product_id')    

            if request.data.get('restaurant') is None:
                raise MissingParameters('restaurant')

            restaurants = list()
            for item in RESTAURANT:
                restaurants.append(item.value)

            if request.data["restaurant"] not in restaurants:
                raise EntityError("restaurant")

            product = self.DeleteProductsByRestaurantUsecase(product_id=int(request.data.get("product_id")), restaurant=RESTAURANT(request.data.get("restaurant")))
            viewmodel = DeleteProductsByRestaurantViewmodel(product=product)
            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])

