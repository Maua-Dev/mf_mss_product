from src.shared.domain.entities.product import Product
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class GetProductUsecase:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def __call__(self, product_id: str) -> Product:
        
        if type(product_id) is not str:
            raise EntityError("product_id")
        
        product = self.repo.get_product(product_id)

        if product is None:
            raise NoItemsFound("product")
        
        return product