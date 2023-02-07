import datetime
from typing import List

from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.product import Product
from src.shared.helpers.errors.domain_errors import EntityError

class CreateProductUsecase:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def __call__(self, product:Product) -> Product:
        
        return self.repo.create_product(product)