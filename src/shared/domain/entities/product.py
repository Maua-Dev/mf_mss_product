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
    product_id: int
    last_update: int  #miliseconds
    restaurant: RESTAURANT
    prepareTime: int = None #min
    
    def __init__(self,
                available: bool,
                price: float,
                name: str,
                description: str,
                meal_type: MEAL_TYPE,
                photo: str,
                product_id: int,
                last_update: int,
                restaurant: RESTAURANT,
                prepareTime: int = None):
        
        if type(available) != bool:
            raise EntityError("avaiable")
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
        
        if type(product_id) != int:
            raise EntityError("product_id")
        self.product_id = product_id
        
        if type(last_update) != int:
            raise EntityError("last_update")
        self.last_update = last_update
       
        if type(restaurant) != RESTAURANT:
            raise EntityError("restaurant")
        self.restaurant = restaurant
        
        if type(prepareTime) != int and prepareTime is not None:
            raise EntityError("prepareTime")
        self.prepareTime = prepareTime
        
    
    
    
    