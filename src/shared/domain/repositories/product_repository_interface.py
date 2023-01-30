from abc import ABC, abstractmethod
from typing import List
from src.shared.domain.entities.product import Product
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class IProductRepository(ABC):
    
    @abstractmethod
    def get_all_products_by_restaurant(self, restaurant: RESTAURANT) -> List[Product]:
        pass