from typing import Optional
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.environments import Environments
from src.shared.infra.dto.user_dynamo_dto import UserDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class UserRepositoryDynamo(IUserRepository):

    @staticmethod
    def partition_key_format(user_id: str) -> str:
        return f"{user_id}"
    
    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url_user,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name_user,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key_user,
                                       )


    def create_user(self, new_user: User) -> User:
        user_dto = UserDynamoDTO.from_entity(user=new_user)
        item = user_dto.to_dynamo()

        resp = self.dynamo.put_item(
        partition_key=self.partition_key_format(new_user.user_id),
        item=item,
        is_decimal=True
        )

        return new_user
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass
        # user_data = self.dynamo.get_item(partition_key=self.partition_key_format(user_id=user_id))                    
        
        # if 'Item' not in user_data:
        #     return None

        # user = UserDynamoDTO.from_dynamo(user_data.get("Item")).to_entity()

        # return user

    def update_user_by_id(self, user_id: str, new_name: Optional[str] = None) -> User:
        pass
        # if self.get_user_by_id(user_id=user_id) == None: 
        #     return None
        
        # update_user = User(
        #     name=new_name,
        #     )
            
        # update_user_dto = UserDynamoDTO.from_entity(user=update_user).to_dynamo()

        # response = self.dynamo.hard_update_item(
        #     partition_key=self.partition_key_format(user_id=user_id),
        #     item=update_user_dto,
        #     is_decimal=True
        # )

        # return update_user

    def delete_user_by_id(self, user_id: str) -> Optional[User]:
        pass
        # delete_product = self.dynamo.delete_item(partition_key=self.partition_key_format(user_id=user_id))
        
        # if 'users_list' not in delete_product:
        #     return None

        # return UserDynamoDTO.from_dynamo(delete_product["users_list"]).to_entity()