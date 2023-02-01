from typing import List

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.product import Product
from src.shared.domain.repositories.product_repository_interface import IProductRepository

class GetAllProductsByRestaurantUsecase:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def __call__(self, restaurant: RESTAURANT) -> List[Product]:
        return self.repo.get_all_products_by_restaurant(restaurant=restaurant)