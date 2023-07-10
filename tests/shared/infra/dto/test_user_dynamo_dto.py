from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.dto.user_dynamo_dto import UserDynamoDTO
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserDynamoDto:
    def test_from_entity(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO.from_entity(user=repo.users_list[0])

        expected_user_dto = UserDynamoDTO(
            name=repo.users_list[0].name,
            email=repo.users_list[0].email,
            user_id=repo.users_list[0].user_id,
            role=repo.users_list[0].role,
            restaurant=repo.users_list[0].restaurant,
        )

        assert user_dto == expected_user_dto

    def test_to_dynamo(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO(
            name=repo.users_list[2].name,
            email=repo.users_list[2].email,
            user_id=repo.users_list[2].user_id,
            role=repo.users_list[2].role,
            restaurant=repo.users_list[2].restaurant,
        )

        user_dynamo = user_dto.to_dynamo()

        expected_dict = {
            "entity": "user",
            "name": repo.users_list[2].name,
            "email": repo.users_list[2].email,
            "user_id": repo.users_list[2].user_id,
            "role": repo.users_list[2].role.value,
            "restaurant": repo.users_list[2].restaurant.value
        }

        assert user_dynamo == expected_dict

    def test_to_dynamo_restaurant_none(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO(
            name=repo.users_list[0].name,
            email=repo.users_list[0].email,
            user_id=repo.users_list[0].user_id,
            role=repo.users_list[0].role,
            restaurant=repo.users_list[0].restaurant,
        )

        user_dynamo = user_dto.to_dynamo()

        expected_dict = {
            "entity": "user",
            "name": repo.users_list[0].name,
            "email": repo.users_list[0].email,
            "user_id": repo.users_list[0].user_id,
            "role": repo.users_list[0].role.value,
            "restaurant": repo.users_list[0].restaurant.value if repo.users_list[0].restaurant is not None else None
        }

        assert user_dynamo == expected_dict

       