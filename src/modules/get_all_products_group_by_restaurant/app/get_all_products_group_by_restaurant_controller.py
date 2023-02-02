from .get_all_products_group_by_restaurant_usecase import GetAllProductsGroupByRestaurantUsecase

from .get_all_products_group_by_restaurant_viewmodel import GetAllProductsGroupByRestaurantViewmodel

from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import InternalServerError, OK, BadRequest
from src.shared.helpers.errors.domain_errors import EntityError


class GetAllProductGroupByRestaurantController:
    def __init__(self, usecase: GetAllProductsGroupByRestaurantUsecase):
        self.GetAllProductsGroupByRestaurantUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            all_products = self.GetAllProductsGroupByRestaurantUsecase()
            viewmodel = GetAllProductsGroupByRestaurantViewmodel(all_products=all_products)

            return OK(viewmodel.to_dict())

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])