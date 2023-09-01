from src.modules.create_connection.app.create_connection_viewmodel import CreateConnectionViewmodel
from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class Test_CreateConnectionViewmodel:
    def test_create_connection_viewmodel(self):

        connection = Connection(connection_id="yu120f88-2c34-45u", api_id="gdc02df8-j2", expire_date_seconds=1682265600, creation_time_seconds=1682262000, user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", restaurant=RESTAURANT.HORA_H)

        connection_viewmodel = CreateConnectionViewmodel(connection).to_dict()

        expected = {
            "connection":{
                "connection_id": "yu120f88-2c34-45u",
                "api_id": "gdc02df8-j2",
                "expire_date_seconds": 1682265600,
                "creation_time_seconds": 1682262000,
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                "restaurant": "HORA_H"
            },
            "message": "the connection was created"
        }

        assert expected == connection_viewmodel