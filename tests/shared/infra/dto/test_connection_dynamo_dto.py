from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.dto.connection_dynamo_dto import ConnectionDynamoDTO


class Test_ConnectionDynamoDTO:

    def test_from_entity(self):
        connection = Connection(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )

        connection_dynamo_dto = ConnectionDynamoDTO.from_entity(connection)

        expected_connection_dynamo_dto = ConnectionDynamoDTO(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )

        assert connection_dynamo_dto.connection_id == expected_connection_dynamo_dto.connection_id
        assert connection_dynamo_dto.api_id == expected_connection_dynamo_dto.api_id
        assert connection_dynamo_dto.expire_date_seconds == expected_connection_dynamo_dto.expire_date_seconds
        assert connection_dynamo_dto.creation_time_seconds == expected_connection_dynamo_dto.creation_time_seconds
        assert connection_dynamo_dto.user_id == expected_connection_dynamo_dto.user_id
        assert connection_dynamo_dto.restaurant == expected_connection_dynamo_dto.restaurant

    def test_to_dynamo_restaurant_none(self):
        connection_dynamo_dto = ConnectionDynamoDTO(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )
        expected_dynamo = {
            "connection_id":"4b1e0f88-2c34-3t",
            "api_id":"63c02df8-d",
            "expire_date_seconds":1693418400,
            "creation_time_seconds":1693414800,
            "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48abb",
            "restaurant":"CANTINA_DO_MOLEZA",
            "entity": "connection"
        }

        assert expected_dynamo == connection_dynamo_dto.to_dynamo()

    def test_to_dynamo(self):
        connection_dynamo_dto = ConnectionDynamoDTO(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb"
        )
        expected_dynamo = {
            "connection_id":"4b1e0f88-2c34-3t",
            "api_id":"63c02df8-d",
            "expire_date_seconds":1693418400,
            "creation_time_seconds":1693414800,
            "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48abb",
            "entity": "connection"
        }

        assert expected_dynamo == connection_dynamo_dto.to_dynamo()

    def test_from_entity_to_dynamo(self):
        connection = Connection(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )

        connection_dynamo_dto = ConnectionDynamoDTO.from_entity(connection)

        expected_dynamo = {
            "connection_id":"4b1e0f88-2c34-3t",
            "api_id":"63c02df8-d",
            "expire_date_seconds":1693418400,
            "creation_time_seconds":1693414800,
            "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48abb",
            "restaurant":"CANTINA_DO_MOLEZA",
            "entity": "connection"
        }

        assert expected_dynamo == connection_dynamo_dto.to_dynamo()

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {"connection_id":"4b1e0f88-2c34-3t",
                                "api_id":"63c02df8-d",
                                "expire_date_seconds":1693418400,
                                "creation_time_seconds":1693414800,
                                "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48abb",
                                "restaurant":"CANTINA_DO_MOLEZA",
                                'entity': 'connection'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        connection_dto = ConnectionDynamoDTO.from_dynamo(connection_data=dynamo_dict["Item"])

        expected_connection_dto = ConnectionDynamoDTO(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )

        assert connection_dto == expected_connection_dto

    def test_from_dynamo_restaurant_none(self):
        dynamo_dict = {'Item': {"connection_id":"4b1e0f88-2c34-3t",
                                "api_id":"63c02df8-d",
                                "expire_date_seconds":1693418400,
                                "creation_time_seconds":1693414800,
                                "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48abb",
                                'entity': 'connection'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        connection_dto = ConnectionDynamoDTO.from_dynamo(connection_data=dynamo_dict["Item"])

        expected_connection_dto = ConnectionDynamoDTO(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb"
        )

        assert connection_dto == expected_connection_dto

    def test_to_entity(self):
        connection_dynamo_dto = ConnectionDynamoDTO(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )

        expected_connection = Connection(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )

        connection = connection_dynamo_dto.to_entity()

        assert type(expected_connection) == type(connection)
        assert expected_connection.connection_id == connection.connection_id
        assert expected_connection.api_id == connection.api_id
        assert expected_connection.expire_date_seconds == connection.expire_date_seconds
        assert expected_connection.creation_time_seconds == connection.creation_time_seconds
        assert expected_connection.user_id == connection.user_id
        assert expected_connection.restaurant == connection.restaurant

    def test_from_dynamo_to_entity(self):
        dynamo_dict = {'Item': {"connection_id":"4b1e0f88-2c34-3t",
                                "api_id":"63c02df8-d",
                                "expire_date_seconds":1693418400,
                                "creation_time_seconds":1693414800,
                                "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48abb",
                                "restaurant":"CANTINA_DO_MOLEZA",
                                'entity': 'connection'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        connection_dto = ConnectionDynamoDTO.from_dynamo(connection_data=dynamo_dict["Item"])

        expected_connection = Connection(
            connection_id="4b1e0f88-2c34-3t",
            api_id="63c02df8-d",
            expire_date_seconds=1693418400,
            creation_time_seconds=1693414800,
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA
        )

        connection = connection_dto.to_entity()

        assert type(expected_connection) == type(connection)
        assert expected_connection.connection_id == connection.connection_id
        assert expected_connection.api_id == connection.api_id
        assert expected_connection.expire_date_seconds == connection.expire_date_seconds
        assert expected_connection.creation_time_seconds == connection.creation_time_seconds
        assert expected_connection.user_id == connection.user_id
        assert expected_connection.restaurant == connection.restaurant
