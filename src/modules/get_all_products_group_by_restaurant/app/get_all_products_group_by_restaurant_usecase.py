from typing import Dict, List

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.product import Product
from src.shared.domain.repositories.product_repository_interface import IProductRepository

class GetAllProductsGroupByRestaurantUsecase:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def __call__(self) -> Dict[RESTAURANT, List[Product]]:
        return self.repo.get_all_products_group_by_restaurant()