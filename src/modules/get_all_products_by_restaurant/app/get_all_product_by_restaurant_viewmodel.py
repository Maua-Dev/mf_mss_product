from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.product import Product
from typing import List

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
             "restaurant": self.product.restaurant.value,
             "prepareTime": self.product.prepareTime 
            }


class GetAllProductsByRestaurantViewmodel:
    all_products: List[ProductViewmodel]
    
    def __init__(self, all_products: List[Product]):
        self.products = [product for product in all_products]

    def to_dict(self) -> dict:
        return{
            "all_products": [ProductViewmodel(product).to_dict() for product in self.products],
            "message": "the products were retrieved"
        }

    
        
    