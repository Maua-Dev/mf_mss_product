import datetime
from typing import Dict, List
from decimal import Decimal
import uuid
import boto3

from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.environments import Environments
from src.shared.infra.dto.product_dynamo_dto import ProductDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class ProductRepositoryDynamo(IProductRepository):
    S3_BUCKET_NAME: str


    @staticmethod
    def partition_key_format(restaurant: RESTAURANT) -> str:
        return f"{restaurant.value}"

    @staticmethod
    def sort_key_format(product_id: str) -> str:
        return f"product#{product_id}"

    @staticmethod
    def gsi_partition_key_format(product_id: str) -> str:
        return f"{product_id}"

    @staticmethod
    def gsi_sort_key_format(restaurant: RESTAURANT) -> str:
        return f"product#{restaurant.value}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url_product,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name_product,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key_product,
                                       sort_key=Environments.get_envs().dynamo_sort_key_product,
                                       gsi_partition_key=Environments.get_envs().dynamo_gsi_partition_key,
                                       gsi_sort_key=Environments.get_envs().dynamo_gsi_sort_key)
        
        self.S3_BUCKET_NAME = Environments.get_envs().s3_bucket_name
        self.s3_client = boto3.client('s3',region_name=Environments.get_envs().region)

    def get_product(self, product_id: str, restaurant: RESTAURANT) -> Product:

        product_data = self.dynamo.get_item(partition_key=self.partition_key_format(restaurant=restaurant),
                                            sort_key=self.sort_key_format(product_id=product_id))

        if 'Item' not in product_data:
            return None

        product = ProductDynamoDTO.from_dynamo(product_data.get("Item")).to_entity()

        return product

    def get_all_products_group_by_restaurant(self) -> Dict[RESTAURANT, List[Product]]:
        response = self.dynamo.get_all_items()

        if 'Items' not in response:
            return None

        products = dict()

        for item in response["Items"]:
            restaurant = RESTAURANT[item["restaurant"]]
            if restaurant not in products.keys():
                products[restaurant] = list()

            products[restaurant].append(ProductDynamoDTO.from_dynamo(product_data=item).to_entity())

        return products

    def create_product(self, new_product: Product) -> Product:
        product_dto = ProductDynamoDTO.from_entity(product=new_product)
        item = product_dto.to_dynamo()

        item[self.dynamo.gsi_partition_key] = self.gsi_partition_key_format(new_product.product_id)
        item[self.dynamo.gsi_sort_key] = self.gsi_sort_key_format(new_product.restaurant)

        resp = self.dynamo.put_item(partition_key=self.partition_key_format(new_product.restaurant),
                                    sort_key=self.sort_key_format(new_product.product_id), item=item,
                                    is_decimal=True)

        return new_product

    def delete_product(self, product_id: str, restaurant: RESTAURANT) -> Product:

        delete_product = self.dynamo.delete_item(partition_key=self.partition_key_format(restaurant=restaurant),
                                                 sort_key=self.sort_key_format(product_id=product_id))

        if 'Attributes' not in delete_product:
            return None

        return ProductDynamoDTO.from_dynamo(delete_product['Attributes']).to_entity()

    def update_product(self, restaurant: RESTAURANT, product_id: str, new_available: bool = None,
                       new_price: float = None, new_name: str = None, new_description: str = None,
                       new_prepare_time: int = None, new_meal_type: MEAL_TYPE = None, new_photo: str = None,
                       new_last_update: int = None) -> Product:

        product_to_update = self.get_product(product_id=product_id, restaurant=restaurant)

        if product_to_update is None:
            return None

        correct_description_value = ''
        correct_prepare_time_value = -1

        if new_description is not None and new_description != '':
            correct_description_value = new_description
        else:
            correct_description_value = None

        if new_prepare_time is not None and new_prepare_time >= 0:
            correct_prepare_time_value = new_prepare_time
        else:
            correct_prepare_time_value = None

        update_dict = {
            "available": new_available,
            "price": Decimal(str(new_price)) if new_price is not None else None,
            "name": new_name,
            "description": correct_description_value,
            "prepare_time": Decimal(str(correct_prepare_time_value)) if correct_prepare_time_value is not None else None,
            "meal_type": new_meal_type.value if new_meal_type is not None else None,
            "photo": new_photo,
            "last_update": Decimal(str(new_last_update)) if new_last_update is not None else None
        }

        update_dict_without_none_values = {k: v for k, v in update_dict.items() if v is not None}

        response = self.dynamo.update_item(
            partition_key=self.partition_key_format(restaurant=restaurant),
            sort_key=self.sort_key_format(product_id=product_id),
            update_dict=update_dict_without_none_values)

        if "Attributes" not in response:
            return None

        return ProductDynamoDTO.from_dynamo(response["Attributes"]).to_entity()

    def generate_key(self, product_id: str, time_created: int):
        
        key = f"{product_id}/product-{time_created}.jpeg"
        return key
    
    def request_upload_product_photo(self, product_id: str, user_id: str) -> dict:
       
        time_created=int(datetime.datetime.now().timestamp()*1000)

        key = self.generate_key(product_id=product_id,time_created=time_created)

        meta = {
            "product_id": product_id,
            "user_id": user_id,
            "time_created": str(time_created)
        }

        try:
            presigned_url = self.s3_client.generate_presigned_url(
                ClientMethod='put_object',
                Params={
                    'Bucket': self.S3_BUCKET_NAME,
                    'Key': key,
                    'Metadata': meta,
                },
                ExpiresIn=600,
            )

        except Exception as e:
            print("Error while trying to upload file to S3")
            print(e)
            raise e

        return {
            "url": presigned_url,
            "metadata": meta
        }