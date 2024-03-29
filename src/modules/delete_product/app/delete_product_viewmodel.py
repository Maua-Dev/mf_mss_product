from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class ProductViewmodel:
    available: bool
    price: float
    name: str
    description: str
    meal_type: MEAL_TYPE
    photo: str
    product_id: str
    last_update: int
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
             "available": self.available,
             "price": self.price,
             "name": self.name,
             "description": self.description,
             "prepare_time": self.prepare_time,
             "meal_type": self.meal_type.value,
             "photo": self.photo,
             "product_id": self.product_id,
             "last_update": self.last_update,
             "restaurant": self.restaurant.value       
            }

class DeleteProductViewmodel:

    def __init__(self, product: Product):
        self.product = ProductViewmodel(product=product)

    def to_dict(self):
        return{
            "product": self.product.to_dict(),
            "message": "the product was deleted"
        }