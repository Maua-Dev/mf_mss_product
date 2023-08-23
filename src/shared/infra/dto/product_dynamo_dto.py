from decimal import Decimal
from typing import Optional

from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class ProductDynamoDTO:
    available: bool
    price: float
    name: str
    description: str
    prepare_time: int = None
    meal_type: MEAL_TYPE
    photo: Optional[str] = None
    product_id: str
    last_update: int
    restaurant: RESTAURANT

    def __init__(self, available: bool, price: float, name: str, description: str, meal_type: MEAL_TYPE, photo: str, product_id: str, last_update: int, restaurant: RESTAURANT, prepare_time: int = None):
        self.available = available
        self.price = price
        self.name = name
        self.description = description
        self.prepare_time = prepare_time
        self.meal_type = meal_type
        self.photo = photo
        self.product_id = product_id
        self.last_update = last_update
        self.restaurant = restaurant
        
        

    @staticmethod
    def from_entity(product: Product) -> "ProductDynamoDTO":
        """
        Parse data from Product to ProductDynamoDTO
        """
        return ProductDynamoDTO(
            available = product.available,
            price = product.price,    
            name = product.name,
            description = product.description,
            prepare_time = product.prepare_time,
            meal_type = product.meal_type,
            photo = product.photo,
            product_id = product.product_id,
            last_update = product.last_update,
            restaurant = product.restaurant,
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from ProductDynamoDTO to dict
        """
        data = {
            "entity": "product",
            "available": self.available,
            "price": Decimal(str(self.price)),
            "name": self.name,
            "description": self.description,
            "prepare_time": Decimal(str(self.prepare_time)) if self.prepare_time is not None else None,
            "meal_type": self.meal_type.value,
            "photo": self.photo,
            "product_id": self.product_id,
            "last_update": Decimal(str(self.last_update)),
            "restaurant": self.restaurant.value
        }
    
        data_without_none_values = {k: v for k, v in data.items() if v is not None}

        return data_without_none_values

    @staticmethod
    def from_dynamo(product_data: dict) -> "ProductDynamoDTO":
        """
        Parse data from DynamoDB to ProductDynamoDTO
        @param product_data: dict from DynamoDB
        """
        return ProductDynamoDTO(
            available=product_data["available"],
            price=float(product_data["price"]),
            name=str(product_data["name"]),
            description=str(product_data["description"]),
            prepare_time=int(product_data.get("prepare_time")) if product_data.get("prepare_time") is not None else None,
            meal_type=MEAL_TYPE(product_data["meal_type"]),
            photo=str(product_data["photo"]) if product_data.get('photo') is not None else None,
            product_id=str(product_data["product_id"]),
            last_update=int(product_data["last_update"]),
            restaurant=RESTAURANT(product_data["restaurant"]),
        )

    def to_entity(self) -> Product:
        """
        Parse data from UserDynamoDTO to Product
        """
        return Product(
            available=self.available,
            input_price=self.price,
            name=self.name,
            description=self.description,
            prepare_time=self.prepare_time,
            meal_type=self.meal_type,
            photo=self.photo,
            product_id=self.product_id,
            last_update=self.last_update,
            restaurant=self.restaurant
        )

    def __repr__(self):
        return f"ProductDynamoDto(available={self.available}, price={self.price}, name={self.name}, description={self.description}, prepare_time={self.prepare_time}, meal_type={self.meal_type}, photo={self.photo}, product_id={self.product_id}, last_update={self.last_update}, restaurant={self.restaurant})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__