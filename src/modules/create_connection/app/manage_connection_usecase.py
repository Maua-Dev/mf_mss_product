import datetime
from typing import Any
from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser


class ManageConnectionUsecase:

    def __init__(self, repo_order: IOrderRepository, repo_user: IUserRepository):
        self.repo_order = repo_order
        self.repo_user = repo_user

    def __call__(self, connection_id: str, restaurant: RESTAURANT, api_id: str = None, user_id: str = None) -> Connection:

        if api_id == None and user_id == None:
            disconnected = self.repo_order.abort_connection(connection_id=connection_id, restaurant=restaurant)
            if disconnected is None:
                raise NoItemsFound("connection")
            
            return disconnected
            # connected = False

        else:
            user = self.repo_user.get_user_by_id(user_id=user_id)

            if user is None:
                raise UnregisteredUser()
        
            creation_time_seconds = int(datetime.datetime.now().timestamp())
            expire_date_seconds = creation_time_seconds + 3600

            connection = Connection(connection_id=connection_id, api_id=api_id, expire_date_seconds=expire_date_seconds, creation_time_seconds=creation_time_seconds, user_id=user_id, restaurant=restaurant)
            
            connected = self.repo_order.create_connection(connection=connection)

            return connected

        # if connected:
        #     return "the connection was created"
        # else:
        #     return "the connection was aborted"