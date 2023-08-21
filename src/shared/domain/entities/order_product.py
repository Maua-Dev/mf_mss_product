import abc

from src.shared.helpers.errors.domain_errors import EntityError


class OrderProduct(abc.ABC):
    product_name: str
    product_id: str
    quantity: int
    PRODUCT_ID_LENGTH = 36

    def __init__(self,
                 product_name: str,
                 product_id: str,
                 quantity: int):
        
        if type(product_name) != str:
            raise EntityError("product_name")
        self.product_name = product_name

        if not self.validate_product_id(product_id=product_id):
            raise EntityError("product_id")
        self.product_id = product_id

        if not self.validate_quantity(quantity=quantity):
            raise EntityError("quantity")
        self.quantity = quantity

    @staticmethod
    def validate_product_id(product_id: str) -> bool:
        if type(product_id) != str: return False
        if len(product_id) != OrderProduct.PRODUCT_ID_LENGTH: return False
        return True
    
    @staticmethod
    def validate_quantity(quantity: int) -> bool:
        if type(quantity) != int:
            return False
        if quantity < 1:
            return False
        return True
    
    def __repr__(self):
        return f"OrderProducts(product_name={self.product_name}, product_id={self.product_id}, quantity={self.quantity})"
