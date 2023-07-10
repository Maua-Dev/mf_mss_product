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
        self.dynamo = DynamoDatasource(endpoint_url_user=Environments.get_envs().endpoint_url_user,
                                       dynamo_table_name_user=Environments.get_envs().dynamo_table_name_user,
                                       region=Environments.get_envs().region,
                                       partition_key_user=Environments.get_envs().dynamo_partition_key_user,
                                       )


    def create_user(self, new_user: User) -> User:
        user_dto = UserDynamoDTO.from_entity(user=new_user)
        item = user_dto.to_dynamo()

        item[self.dynamo.partition_key] = self.partition_key_format(new_user.user_id)

        resp = self.dynamo.put_item(
        partition_key_user=self.partition_key_format(new_user.user_id),
        item=item,
        is_decimal=True
        )

        return new_user
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass

    def update_user_by_id(self, user_id: str, new_name: Optional[str] = None) -> User:
        pass

    def delete_user_by_id(self, user_id: str) -> Optional[User]:
        pass