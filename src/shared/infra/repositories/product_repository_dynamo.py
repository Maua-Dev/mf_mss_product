from typing import Dict, List

from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.product_dynamo_dto import ProductDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class ProductRepositoryDynamo(IProductRepository):

    @staticmethod
    def partition_key_format(restaurant: RESTAURANT) -> str:
        return f"{restaurant.value}"

    @staticmethod
    def sort_key_format(product_id: str) -> str:
        return f"product#{product_id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)
        
    def get_product(self, product_id: str) -> Product:
        
        product_data = self.dynamo.get_item(partition_key=self.partition_key_format(RESTAURANT.value),
                                            sort_key=self.sort_key_format(product_id))

        product = ProductDynamoDTO.from_dynamo(product_data.get("Item")).to_entity()

    def get_all_products_group_by_restaurant(self) -> Dict[RESTAURANT, List[Product]]:
        response = self.dynamo.get_all_items()

        products_dict = list()
        restaurant = dict()
        for item in response["Items"]:
            if item["entity"] == "product":
                products_dict.append(item)

            elif item["entity"] == "restaurant":
                restaurant[item["restaurant"]] = restaurant.get(item["restaurant"], list())
                restaurant[item["restaurant"]].append(ProductDynamoDTO.from_dynamo(product_data=item).to_entity())

        products = list()
        for product in products_dict:
            product_to_add = product
            products.append(ProductDynamoDTO.from_dynamo(product_to_add).to_entity())

        return restaurant, products

    def create_product(self, new_product: Product) -> Product:
        product_dto = ProductDynamoDTO.from_entity(product=new_product)
        item = product_dto.to_dynamo()

        resp = self.dynamo.put_item(partition_key=self.partition_key_format(new_product.restaurant),
                                    sort_key=self.sort_key_format(new_product.product_id), item=item,
                                    is_decimal=True)

        return new_product

    def delete_product(self, product_id: str, restaurant: RESTAURANT) -> Product:
        pass

    def update_product(self, restaurant: RESTAURANT, product_id: str, new_available: bool = None, new_price: float = None, new_name: str = None, new_description: str = None, new_prepare_time: int = None, new_meal_type: MEAL_TYPE = None, new_photo: str = None, new_last_update: int = None) -> Product:
        update_product = Product(
            restaurant=restaurant,
            product_id=product_id,
            available=new_available,
            price=new_price,
            name=new_name,
            description=new_description,
            prepare_time=new_prepare_time,
            meal_type=new_meal_type,
            photo=new_photo,
            last_update=new_last_update
            )
        
        update_product_dto = ProductDynamoDTO.from_entity(product=update_product).to_dynamo()

        response = self.dynamo.hard_update_item(
            partition_key=self.partition_key_format(restaurant=restaurant),
            sort_key=self.sort_key_format(product_id=product_id),
            item=update_product_dto,
            is_decimal=True
        )

        return update_product

    def get_all_products_by_restaurant(self, restaurant: RESTAURANT) -> List[Product]:
        pass