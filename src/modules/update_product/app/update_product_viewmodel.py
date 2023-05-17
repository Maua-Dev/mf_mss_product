from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class ProductViewmodel:
    available: bool = None
    price: float = None
    name: str = None
    description: str = None
    meal_type: MEAL_TYPE = None
    photo: str = None
    product_id: str 
    last_update: int = None
    restaurant: RESTAURANT
    prepare_time: int = None

    def __init__(self, product: Product):
        self.available = product.available
        self.price = product.price
        self.name = product.name
        self.description = product.description
        self.meal_type = product.meal_type
        self.photo = product.photo
        self.product_id = product.product_id
        self.last_update = product.last_update
        self.restaurant = product.restaurant
        self.prepare_time = product.prepare_time

    def to_dict(self) -> dict:
        return{
            "product_id": self.product_id,
            "restaurant": self.restaurant.value,
            "available": self.available,
            "price": self.price,
            "name": self.name,
            "description": self.description,
            "meal_type": self.meal_type.value,
            "photo": self.photo, 
            "last_update": self.last_update,
            "prepare_time": self.prepare_time,
        }

class UpdateProductViewmodel:
    product: ProductViewmodel

    def __init__(self, product: Product):
        self.product = ProductViewmodel(product=product)

    def to_dict(self):
        return{
            "product": self.product.to_dict(),
            "message": "the product was updated"
        }