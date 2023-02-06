from abc import ABC, abstractmethod
from typing import Dict, List
from src.shared.domain.entities.product import Product
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class IProductRepository(ABC):
    
    @abstractmethod
    def get_all_products_group_by_restaurant(self) -> Dict[RESTAURANT, List[Product]]:
        pass
    
    @abstractmethod
    def delete_products_by_restaurant(self, product_id: int, restaurant: RESTAURANT) -> Dict[RESTAURANT, List[Product]]:
        pass