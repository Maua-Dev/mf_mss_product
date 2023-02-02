from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.product import Product
from typing import Dict, List

class ProductViewmodel:
    product: Product

    def __init__(self, product: Product):
        self.product = product

    def to_dict(self) -> dict:
        return{
             "available": self.product.available,
             "price": self.product.price,
             "name": self.product.name,
             "description": self.product.description,
             "meal_type": self.product.meal_type.value,
             "photo": self.product.photo,
             "product_id": self.product.product_id,
             "last_update": self.product.last_update,
             "prepareTime": self.product.prepareTime 
            }


class GetAllProductsGroupByRestaurantViewmodel:
    all_products: Dict[RESTAURANT, List[Product]]
    
    def __init__(self, all_products: Dict[RESTAURANT, List[Product]]):
        self.all_products = all_products

    def to_dict(self) -> dict:
        dict_return = {
            k.value: [ProductViewmodel(product=product).to_dict() for product in v] for k, v in self.all_products.items()     
        }
        dict_return["message"] = "the products were retrieved"
        return dict_return
        


    
        
    