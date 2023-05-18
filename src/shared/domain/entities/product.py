import abc

from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError

class Product(abc.ABC):
    available: bool
    price: float
    name: str
    description: str
    meal_type: MEAL_TYPE
    photo: str
    product_id: str
    last_update: int  #miliseconds
    restaurant: RESTAURANT
    prepare_time: int = None #min
    PRODUCT_ID_LENGTH = 36
    
    def __init__(self,
                available: bool,
                price: float,
                name: str,
                description: str,
                meal_type: MEAL_TYPE,
                photo: str,
                product_id: str,
                last_update: int,
                restaurant: RESTAURANT,
                prepare_time: int = None):
        
        if type(available) != bool:
            raise EntityError("available")
        self.available = available
        
        if type(price) != float:
            raise EntityError("price")
        self.price = price
        
        if type(name) != str:
            raise EntityError("name")
        self.name = name
        
        if type(description) != str:
            raise EntityError("description")
        self.description = description
        
        if type(meal_type) != MEAL_TYPE:
            raise EntityError("meal_type")
        self.meal_type = meal_type
        
        if type(photo) != str:
            raise EntityError("photo")
        self.photo = photo
        
        if not self.validate_product_id(product_id=product_id):
            raise EntityError("product_id")
        self.product_id = product_id
        
        if type(last_update) != int:
            raise EntityError("last_update")
        self.last_update = last_update
       
        if type(restaurant) != RESTAURANT:
            raise EntityError("restaurant")
        self.restaurant = restaurant
        
        if prepare_time is not None:
            if type(prepare_time) != int:
                raise EntityError("prepare_time")
        self.prepare_time = prepare_time
        
    
    @staticmethod
    def validate_product_id(product_id: str) -> bool:
        if type(product_id) != str: return False
        if len(product_id) != Product.PRODUCT_ID_LENGTH: return False
        return True
            
            
    def __repr__(self):
        return f"Product(available={self.available}, price={self.price}, name='{self.name}', description='{self.description}', meal_type='{self.meal_type.value}', photo='{self.photo}', product_id={self.product_id}, last_update={self.last_update}, restaurant='{self.restaurant.value}', prepare_time={self.prepare_time})"