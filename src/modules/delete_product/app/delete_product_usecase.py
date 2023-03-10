from src.shared.domain.entities.product import Product
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteProductUsecase:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def __call__(self, product_id: str, restaurant: RESTAURANT) -> Product:
        if not Product.validate_product_id(product_id=product_id):
            raise EntityError("product_id")

        if type(restaurant) != RESTAURANT:
            raise EntityError("restaurant")

        product = self.repo.delete_product(product_id=product_id,restaurant=restaurant)

        if product is None:
            raise NoItemsFound("product_id and restaurant")
        
        return product