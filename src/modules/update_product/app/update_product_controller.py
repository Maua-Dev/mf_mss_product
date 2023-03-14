from src.modules.update_product.app.update_product_usecase import UpdateProductUsecase
from src.modules.update_product.app.update_product_viewmodel import UpdateProductViewmodel
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError


class UpdateProductController:
    def __init__(self, usecase: UpdateProductUsecase):
        self.UpdateProductUsecase = usecase

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
            
            meal_types = list()
            for item in MEAL_TYPE:
                meal_types.append(item.value)

            if request.data["new_meal_type"] not in meal_types:
                raise EntityError("new_meal_type")

            product = self.UpdateProductUsecase(
                product_id=str(request.data.get("product_id")),
                restaurant=RESTAURANT(request.data.get("restaurant")),
                new_available=bool(request.data.get("new_available")),
                new_price=float(request.data.get("new_price")),
                new_name=str(request.data.get("new_name")),
                new_description=str(request.data.get("new_description")),
                new_prepare_time=int(request.data.get("new_prepare_time")),
                new_meal_type=MEAL_TYPE(request.data.get("new_meal_type")),
                new_photo=str(request.data.get("new_photo")),
                new_last_update=int(request.data.get("new_last_update"))
                )
            
            viewmodel = UpdateProductViewmodel(product=product)

            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
