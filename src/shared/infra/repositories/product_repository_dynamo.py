from typing import List

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
        pass

    def get_all_products_group_by_restaurant(self) -> List[Product]:
        pass

    def create_product(self, new_product: Product) -> Product:
        product_dto = ProductDynamoDTO.from_entity(product=new_product)
        item = product_dto.to_dynamo()

        resp = self.dynamo.put_item(partition_key=self.partition_key_format(new_product.restaurant),
                                    sort_key=self.sort_key_format(new_product.product_id), item=item,
                                    is_decimal=True)

        return new_product

    def delete_product(self, product_id: str) -> Product:
        pass

    def update_product(self, product_id: str, new_available: bool = None, new_price: float = None, new_name: str = None, new_description: str = None, new_prepare_time: int = None, new_meal_type: MEAL_TYPE = None, new_photo: str = None, new_last_update: int = None) -> Product:
        pass

    def get_all_products_by_restaurant(self, restaurant: RESTAURANT) -> List[Product]:
        pass