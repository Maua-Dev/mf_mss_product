from src.shared.domain.entities.product import Product


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
             "prepare_time": self.product.prepare_time,
             "meal_type": self.product.meal_type.value,
             "photo": self.product.photo,
             "product_id": self.product.product_id,
             "last_update": self.product.last_update,
             "restaurant": self.product.restaurant.value       
            }

class DeleteProductViewmodel:
    product: ProductViewmodel

    def __init__(self, product: Product):
        self.product = ProductViewmodel(product=product)

    def to_dict(self):
        return{
            "product": self.product.to_dict(),
            "message": "the product was deleted"
        }