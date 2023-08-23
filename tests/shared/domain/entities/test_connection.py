import pytest
from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Connection:
    def test_connection_without_restaurant(self):
        connection = Connection(
            connection_id="66575282-1c20-49e",
            api_id="47c02df8-c1",
            expire_date_seconds=1692140512,
            creation_time_seconds=1692140549,
            user_id="f3c395bc-d496-4503-885c-36ada2b4e651",
            restaurant=None
        )

        assert type(connection) == Connection
        assert connection.connection_id == "66575282-1c20-49e"
        assert connection.api_id == "47c02df8-c1"
        assert connection.expire_date_seconds == 1692140512
        assert connection.creation_time_seconds == 1692140549
        assert connection.user_id == "f3c395bc-d496-4503-885c-36ada2b4e651"
        assert connection.restaurant == None

    def test_connection_with_restaurant(self):
        connection = Connection(
            connection_id="66575282-1c20-49e",
            api_id="47c02df8-c1",
            expire_date_seconds=1692140512,
            creation_time_seconds=1692140549,
            user_id="f3c395bc-d496-4503-885c-36ada2b4e651",
            restaurant=RESTAURANT.HORA_H
        )

        assert type(connection) == Connection
        assert connection.connection_id == "66575282-1c20-49e"
        assert connection.api_id == "47c02df8-c1"
        assert connection.expire_date_seconds == 1692140512
        assert connection.creation_time_seconds == 1692140549
        assert connection.user_id == "f3c395bc-d496-4503-885c-36ada2b4e651"
        assert connection.restaurant == RESTAURANT.HORA_H

    def test_invalid_id(self):
        with pytest.raises(EntityError):
            connection = Connection(
                connection_id=True,
                api_id="47c02df8-c116-4539-b3df-536175640101",
                expire_date_seconds=1692140512,
                creation_time_seconds=1692140549,
                user_id="f3c395bc-d496-4503-885c-36ada2b4e651",
                restaurant=None
            )

    def test_wrong_connection_id_length(self):
        with pytest.raises(EntityError):
            connection = Connection(
                connection_id="66575282-1c20-49e7-93c0-6d9146e30dc0",
                api_id="47c02df8-c1",
                expire_date_seconds=1692140512,
                creation_time_seconds=1692140549,
                user_id="f3c395bc-d496-4503-885c-36ada2b4e651",
                restaurant=None
            )

    def test_wrong_api_id_length(self):
        with pytest.raises(EntityError):
            connection = Connection(
                connection_id="66575282-1c20-49e",
                api_id="47c02df8-c116-4539-b3df",
                expire_date_seconds=1692140512,
                creation_time_seconds=1692140549,
                user_id="f3c395bc-d496-4503-885c-36ada2b4e651",
                restaurant=None
            )

    def test_wrong_user_id_length(self):
        with pytest.raises(EntityError):
            connection = Connection(
                connection_id="66575282-1c20-49e",
                api_id="47c02df8-c1",
                expire_date_seconds=1692140512,
                creation_time_seconds=1692140549,
                user_id="f3c395bc-d496-4503",
                restaurant=None
            )

    def test_invalid_expire_date_seconds(self):
        with pytest.raises(EntityError):
            connection = Connection(
                connection_id="66575282-1c20-49e",
                api_id="47c02df8-c1",
                expire_date_seconds="1692140512",
                creation_time_seconds=1692140549,
                user_id="f3c395bc-d496-4503-885c-36ada2b4e651",
                restaurant=None
        )

    def test_invalid_creation_time_seconds(self):
        with pytest.raises(EntityError):
            connection = Connection(
                connection_id="66575282-1c20-49e",
                api_id="47c02df8-c1",
                expire_date_seconds=1692140512,
                creation_time_seconds="1692140549",
                user_id="f3c395bc-d496-4503-885c-36ada2b4e651",
                restaurant=None
        )

    def test_invalid_restaurant(self):
        with pytest.raises(EntityError):
            connection = Connection(
                connection_id="66575282-1c20-49e",
                api_id="47c02df8-c1",
                expire_date_seconds=1692140512,
                creation_time_seconds=1692140549,
                user_id="f3c395bc-d496-4503-885c-36ada2b4e651",
                restaurant="Souzinhas de Abreu"
        )