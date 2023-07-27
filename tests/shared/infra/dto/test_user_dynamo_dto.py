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
            "role": repo.users_list[0].role.value
        }

        assert user_dynamo == expected_dict

    def test_from_entity_to_dynamo(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO.from_entity(user=repo.users_list[2])

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

    def test_from_dynamo_restaurant_none(self):
        dynamo_dict = {'Item': {'name': 'Lucas Milas',
                                'email' : 'milas@maua.br',
                                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48gbf',
                                'role': 'USER',
                                'PK': '93bc6ada-c0d1-7054-66ab-e17414c48gbf',
                                'entity': 'user'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        user_dto = UserDynamoDTO.from_dynamo(user_data=dynamo_dict["Item"])

        expected_user_dto = UserDynamoDTO(
            name="Lucas Milas",
            email="milas@maua.br",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf",
            role=ROLE.USER,
        )

        assert user_dto == expected_user_dto

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'name': 'Laura Carolina',
                                'email' : 'email.da.laura@gmail.com',
                                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48abb',
                                'role': 'OWNER',
                                'restaurant': "CANTINA_DO_MOLEZA",
                                'PK': '93bc6ada-c0d1-7054-66ab-e17414c48abb',
                                'entity': 'user'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        user_dto = UserDynamoDTO.from_dynamo(user_data=dynamo_dict["Item"])

        expected_user_dto = UserDynamoDTO(
            name="Laura Carolina",
            email="email.da.laura@gmail.com",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            role=ROLE.OWNER,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )

        assert user_dto == expected_user_dto

    def test_to_entity(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO(
            name=repo.users_list[0].name,
            email=repo.users_list[0].email,
            user_id=repo.users_list[0].user_id,
            role=repo.users_list[0].role,
            restaurant=repo.users_list[0].restaurant,
        )

        user = user_dto.to_entity()

        assert user.name == repo.users_list[0].name
        assert user.email == repo.users_list[0].email
        assert user.user_id == repo.users_list[0].user_id
        assert user.role == repo.users_list[0].role
        assert user.restaurant == repo.users_list[0].restaurant

    def test_from_dynamo_to_entity(self):
        dynamo_item = {'Item': {'name': 'José',
                                'email': 'ze@porteiros.br',
                                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48af1',
                                'role': 'USER',
                                'state': 'APPROVED',
                                'PK': '93bc6ada-c0d1-7054-66ab-e17414c48af1',
                                'entity': 'user',
                                }}

        user_dto = UserDynamoDTO.from_dynamo(user_data=dynamo_item["Item"])

        user = user_dto.to_entity()

        expected_user = User(
            name='José',
            email='ze@porteiros.br',
            user_id='93bc6ada-c0d1-7054-66ab-e17414c48af1',
            role=ROLE.USER,
        )

        assert user.name == expected_user.name
        assert user.email == expected_user.email
        assert user.user_id == expected_user.user_id
        assert user.role == expected_user.role
       