from src.modules.create_product.app.create_product_usecase import CreateProductUsecase
from src.modules.create_product.app.create_product_viewmodel import CreateProductViewmodel
from src.shared.domain.entities.product import Product
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import InternalServerError,BadRequest, Created
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE


class CreateProductController:

    def __init__(self, usecase: CreateProductUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
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

            if request.data.get("photo") is None:
                raise MissingParameters("photo")

            if request.data.get("product_id") is None:
                raise MissingParameters("product_id")

            if request.data.get("last_update") is None:
                raise MissingParameters("last_update")

            if request.data.get("restaurant") is None:
                raise MissingParameters("restaurant")

            if request.data.get("prepareTime") is None:
                raise MissingParameters("prepareTime")

            product = Product(
                available=request.data.get("available"),
                price=request.data.get("price"),
                name=request.data.get("name"),
                description=request.data.get("description"),
                meal_type=MEAL_TYPE(request.data.get("meal_type")),
                photo=request.data.get("photo"),
                product_id=request.data.get("product_id"),
                last_update=request.data.get("last_update"),
                restaurant=RESTAURANT(request.data.get("restaurant")),
                prepareTime=request.data.get("prepareTime")
            )
            product = self.usecase(product)
            viewmodel = CreateProductViewmodel(product=product)

            return Created(viewmodel.to_dict())

        except MissingParameters as err:   
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])

             