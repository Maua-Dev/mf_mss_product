import json
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal
from typing import List, Optional
from src.shared.domain.entities.connection import Connection
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.environments import Environments
from src.shared.infra.dto.connection_dynamo_dto import ConnectionDynamoDTO
from src.shared.infra.dto.order_dynamo_dto import OrderDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
import boto3
import os

class OrderRepositoryDynamo(IOrderRepository):

    @staticmethod
    def order_partition_key_format(restaurant: RESTAURANT) -> str:
        return f"{restaurant.value}"

    @staticmethod
    def order_sort_key_format(order_id: str) -> str:
        return f"order#{order_id}"
    
    @staticmethod
    def order_gsi_partition_key_format(order_id: str) -> str:
        return f"{order_id}"

    @staticmethod
    def order_gsi_sort_key_format(restaurant: RESTAURANT) -> str:
        return f"order#{restaurant.value}"
    
    @staticmethod
    def connection_partition_key_format(restaurant: RESTAURANT) -> str:
        return f"{restaurant.value}"

    @staticmethod
    def connection_sort_key_format(connection_id: str) -> str:
        return f"connection#{connection_id}"

    @staticmethod
    def connection_gsi_partition_key_format(connection_id:str) -> str:
        return f"{connection_id}"

    @staticmethod
    def connection_gsi_sort_key_format(restaurant: RESTAURANT) -> str:
        return f"connection#{restaurant.value}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url_product,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name_product,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key_product,
                                       sort_key=Environments.get_envs().dynamo_sort_key_product,
                                       gsi_partition_key=Environments.get_envs().dynamo_gsi_partition_key_product,
                                       gsi_sort_key=Environments.get_envs().dynamo_gsi_sort_key_product)

    def create_order(self, order: Order) -> Order:
        order_dto = OrderDynamoDTO.from_entity(order=order)
        item = order_dto.to_dynamo()

        item[self.dynamo.gsi_partition_key] = self.order_gsi_partition_key_format(
            order.order_id)
        item[self.dynamo.gsi_sort_key] = self.order_gsi_sort_key_format(
            order.restaurant)

        resp = self.dynamo.put_item(
        partition_key=self.order_partition_key_format(order.restaurant),
        sort_key=self.order_sort_key_format(order.order_id),
        item=item,
        is_decimal=True
        )

        return order

    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        query_string = Key(self.dynamo.gsi_partition_key).eq(self.order_gsi_partition_key_format(order_id))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES', IndexName='GSI1')

        if len(resp['Items']) == 0:
            return None

        restaurant = resp['Items'][0].get('PK')

        order_data = self.dynamo.get_item(partition_key=self.order_partition_key_format(RESTAURANT(restaurant)), sort_key=self.order_sort_key_format(order_id))

        if 'Item' not in order_data:
            return None

        order = OrderDynamoDTO.from_dynamo(order_data.get("Item")).to_entity()

        return order

    def get_all_active_orders_by_restaurant(self, restaurant: RESTAURANT) -> List[Order]:
        query_string = Key(self.dynamo.partition_key).eq(restaurant.value)
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')

        active_orders = []

        for item in resp.get('Items'):
            if item.get('status') == ('PENDING' or 'PREPARING'):
                active_orders.append(item)

        orders = list()
        for order in active_orders:
            orders.append(OrderDynamoDTO.from_dynamo(order).to_entity())

        return orders

    def update_order(self, order_id: str, 
                     new_products: Optional[List[OrderProduct]] = None,
                     new_status: Optional[STATUS] = None,
                     new_total_price: Optional[float] = None,
                     new_aborted_reason: Optional[str] = None):
        
        order_to_update = self.get_order_by_id(order_id=order_id)

        if order_to_update is None:
            return None
        
        update_dict={
            "products": new_products,
            "status": new_status.value, 
            "total_price": Decimal(str(new_total_price)) if new_total_price is not None else None, 
            "aborted_reason": new_aborted_reason}

        update_dict_without_none_values = {k: v for k, v in update_dict.items() if v is not None}

        response = self.dynamo.update_item(
            partition_key=self.order_partition_key_format(order_to_update.restaurant),
            sort_key=self.order_sort_key_format(order_id),
            update_dict=update_dict_without_none_values)

        if "Attributes" not in response:
            return None

        return OrderDynamoDTO.from_dynamo(response["Attributes"]).to_entity()

    def get_all_orders_by_user(self, user_id: str, exclusive_start_key: str = None, amount: int = None) -> List[Order]:
        resp = self.dynamo.get_all_items()

        orders = []
        for item in resp.get('Items'):
            if item.get('entity') == "order":
                orders.append(item)

        orders_to_sort = []
        for order in orders:
            if order.get('user_id') == user_id:
                orders_to_sort.append(order)

        user_sorted = sorted(orders_to_sort, key=lambda item: item.get('creation_time_milliseconds'), reverse=False)

        if amount is None: amount = 20

        order_id_position = None
        if exclusive_start_key:
            for index, item in enumerate(user_sorted):
                if item.get('order_id') == exclusive_start_key:
                    order_id_position = index
                    break

        if order_id_position is not None:
            user_sorted = user_sorted[order_id_position:order_id_position + amount]
            for index, item in enumerate(user_sorted):
                user_sorted[index] = OrderDynamoDTO.from_dynamo(item).to_entity()

        else:
            user_sorted = user_sorted[:amount]
            for index, item in enumerate(user_sorted):
                user_sorted[index] = OrderDynamoDTO.from_dynamo(item).to_entity()

        return user_sorted
        
        # if exclusive_start_key:
        #     for index, item in enumerate(user_sorted):
        #         if item.get('order_id') == exclusive_start_key:
        #             order_id_position = index
        #             user_sorted.append(OrderDynamoDTO.from_dynamo(item).to_entity())
        #             return user_sorted[order_id_position:order_id_position + amount]

        # else:
        #     for index, item in enumerate(user_sorted):
        #         user_sorted.append(OrderDynamoDTO.from_dynamo(item).to_entity())
        #         return user_sorted[:amount]

    def get_all_orders_by_restaurant(self, restaurant: RESTAURANT, exclusive_start_key: str = None, amount: int = None) -> List[Order]:
        query_string = Key(self.dynamo.partition_key).eq(self.order_partition_key_format(restaurant))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')

        orders_to_sort = []
        for order in resp.get('Items'):
            if order.get('entity') == 'order':
                orders_to_sort.append(order)

        restaurant_sorted = sorted(orders_to_sort, key=lambda item: item.get('creation_time_milliseconds'), reverse=False)

        if amount is None: amount = 20

        order_id_position = None
        if exclusive_start_key:
            for index, item in enumerate(restaurant_sorted):
                if item.get('order_id') == exclusive_start_key:
                    order_id_position = index
                    break
        
        if order_id_position is not None:
            restaurant_sorted = restaurant_sorted[order_id_position + 1:]
            for index, item in enumerate(restaurant_sorted):
                restaurant_sorted[index] = OrderDynamoDTO.from_dynamo(item).to_entity()
            return restaurant_sorted[:amount]

        else:
            restaurant_sorted = restaurant_sorted[:amount]
            for index, item in enumerate(restaurant_sorted):
                restaurant_sorted[index] = OrderDynamoDTO.from_dynamo(item).to_entity()
            return restaurant_sorted[:amount]

    def publish_order(self, connections_list: List[Connection], order: Order) -> bool:
        for connection in connections_list:
            self.push_data_to_client(connection.connection_id, order)
        return True

    def create_connection(self, connection: Connection) -> Connection:
        connection_dto = ConnectionDynamoDTO.from_entity(connection=connection)
        item = connection_dto.to_dynamo()

        item[self.dynamo.gsi_partition_key] = self.connection_gsi_partition_key_format(
            connection.connection_id)
        item[self.dynamo.gsi_sort_key] = self.connection_gsi_sort_key_format(
            connection.restaurant)

        resp = self.dynamo.put_item(
        partition_key=self.connection_partition_key_format(connection.restaurant),
        sort_key=self.connection_sort_key_format(connection.connection_id),
        item=item,
        is_decimal=True
        )

        return connection

    def abort_connection(self, connection_id: str) -> Connection:
        query_string = Key(self.dynamo.gsi_partition_key).eq(self.connection_gsi_partition_key_format(connection_id))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES', IndexName='GSI1')

        restaurant = resp['Items'][0].get('PK')

        abort_connection = self.dynamo.delete_item(partition_key=self.connection_partition_key_format(RESTAURANT(restaurant)), sort_key=self.connection_sort_key_format(connection_id))

        if 'Attributes' not in abort_connection:
            return None

        return ConnectionDynamoDTO.from_dynamo(abort_connection['Attributes']).to_entity()

    def get_all_connections_by_restaurant(self, restaurant: RESTAURANT) -> List[Connection]:
        query_string = Key(self.dynamo.partition_key).eq(restaurant.value)
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')

        connections_dict = []

        for item in resp["Items"]:
            if item["entity"] == "connection":
                connections_dict.append(item)

        connections = []
        for connection in connections_dict:
            connections.append(ConnectionDynamoDTO.from_dynamo(connection).to_entity())

        return connections

    def get_connection_by_connection_id(self, connection_id: str) -> Optional[Connection]:
        query_string = Key(self.dynamo.gsi_partition_key).eq(self.connection_gsi_partition_key_format(connection_id))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES', IndexName='GSI1')

        if len(resp['Items']) == 0:
            return None

        restaurant = resp['Items'][0].get('PK') 

        connection_data = self.dynamo.get_item(partition_key=self.connection_partition_key_format(RESTAURANT(restaurant)), sort_key=self.connection_sort_key_format(connection_id))                 
        
        if 'Item' not in connection_data:
            return None

        connection = ConnectionDynamoDTO.from_dynamo(connection_data.get("Item")).to_entity()

        return connection
    
    def push_data_to_client(self, connection_id, order:Order):
        apigw_management_api = boto3.client('apigatewaymanagementapi', endpoint_url=os.environ.get("WEBSOCKET_URL"))
    
        print('pushToConnection : ' + connection_id + ' feed  : ' + str(order.order_id))

        data = {
            "order_id": order.order_id,
            "user_name": order.user_name,
            "user_id": order.user_id,
            "products": [{
            "product_name": order_product.product_name,
            "product_id": order_product.product_id,
            "quantity": order_product.quantity,
            "observation": order_product.observation
        } for order_product in order.products],
            "creation_time_milliseconds": order.creation_time_milliseconds,
            "restaurant": order.restaurant.value,
            "status": order.status.value,
            "aborted_reason": order.aborted_reason,
            "total_price": order.total_price,
            "last_status_update": order.last_status_update_milliseconds
        }

        response = apigw_management_api.post_to_connection(ConnectionId=connection_id,Data=json.dumps(data))