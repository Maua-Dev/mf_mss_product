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
    def create_product(self, product:Product) -> Product:
        pass

    @abstractmethod
    def update_product(self, product_id: str, restaurant: RESTAURANT, new_available: bool = None, new_price: float = None, new_name: str = None, new_description: str = None, new_prepare_time: int = None, new_meal_type: MEAL_TYPE = None, new_photo: str = None, new_last_update: int = None) -> Product:
        pass
        
    @abstractmethod   
    def get_product(self, product_id: str, restaurant: RESTAURANT) -> Product:
        pass

    @abstractmethod   
    def request_upload_product_photo(self, product_id: str) -> dict:
        pass
    
