from .get_product_usecase import GetProductUsecase
from .get_product_viewmodel import GetProductViewmodel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.domain_errors import EntityError

class GetProductController:

    def __init__(self, usecase:GetProductUsecase):
        self.GetProductUsecase = usecase

    def __call__(self, request:IRequest) -> IResponse:
        try:
            if request.data.get("product_id") is None:
                raise MissingParameters("product_id")
            
            product = self.GetProductUsecase(product_id=request.data.get("product_id"))

            viewmodel = GetProductViewmodel(product)

            return OK (viewmodel.to_dict())
        
        except NoItemsFound as err:
            message = err.message.lower()

            if message == "product":
                return NotFound(body=f"Produto não encontrado")
            
            else:
                return NotFound(body=f"{message} não encontrado")
            
        except MissingParameters as err:

            return BadRequest(body=f"Parâmetro ausente: {err.message}")
        
        except EntityError as err:

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:

            return InternalServerError(body=err.args[0])
