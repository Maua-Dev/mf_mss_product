from abc import ABC, abstractmethod
from typing import Dict, List
from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class IProductRepository(ABC):
    
    @abstractmethod
    def get_all_products_group_by_restaurant(self) -> Dict[RESTAURANT, List[Product]]:
        pass
    
    @abstractmethod
    def delete_product(self, product_id: int, restaurant: RESTAURANT) -> Product:
        pass

    @abstractmethod
    def get_all_products_by_restaurant(self, restaurant: RESTAURANT) -> List[Product]:
        pass

    @abstractmethod
    def create_product(self, product:Product) -> Product:
        pass

    @abstractmethod
    def update_product(self, available: bool, price: float, name: str, description: str, prepare_time: int, meal_type: MEAL_TYPE, photo: str, last_update: int, restaurant: RESTAURANT) -> Product:
        pass