from src.shared.domain.enums.restaurant_enum import RESTAURANT
from .get_product_usecase import GetProductUsecase
from .get_product_viewmodel import GetProductViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock

class GetProductController:

    def __init__(self, usecase:GetProductUsecase):
        self.GetProductUsecase = usecase

    def __call__(self, request:IRequest) -> IResponse:
        try:
            if request.data.get("product_id") is None:
                raise MissingParameters("product_id")
            
            if request.data.get('restaurant') is None:
                raise MissingParameters('restaurant')
            
            restaurants = list()
            for item in RESTAURANT:
                restaurants.append(item.value)

            if request.data["restaurant"] not in restaurants:
                raise EntityError("restaurant")
            
            product = self.GetProductUsecase(product_id=request.data.get("product_id"),restaurant=RESTAURANT(request.data.get("restaurant")))

            viewmodel = GetProductViewmodel(product)

            return OK (viewmodel.to_dict())
        
        except NoItemsFound as err:
        
            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)
        
        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
