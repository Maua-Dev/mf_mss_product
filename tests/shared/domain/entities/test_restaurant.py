
from datetime import time

import pytest
from src.shared.domain.entities.restaurant import Restaurant
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTimeError

class Test_Restaurant:
    def test_restaurant(self):
        restaurant = Restaurant(
            name="HORA_H", 
            start_time=time(7, 0),
            end_time=time(8, 0),
            email="hora_h@gmail.com"
            )
        
        assert type(restaurant) == Restaurant
        assert restaurant.name == "HORA_H"
        assert restaurant.start_time == time(7, 0)
        assert restaurant.end_time == time(8, 0)
        assert restaurant.email == "hora_h@gmail.com"

    def test_restaurant_name_invalid(self):
        try:
            restaurant = Restaurant(
                name=111, 
                start_time=time(7, 0),
                end_time=time(8, 0),
                email="hora_h@gmail.com"
            )
        except EntityError as error:
            assert str(error)
    
    def test_invalid_start_time(self):
        try:
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=111,
                end_time=time(8, 0),
                email="hora_h@gmail.com"
            )
        except EntityError as error:
            assert str(error)
    
    def test_negative_start_time(self):
        try:
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=time(-1, 0),
                end_time=time(8, 0),
                email="hora_h@gmail.com"
            )
        except ValueError as error:
            assert str(error)
    
    def test_invalid_end_time(self):
        try:
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=time(7, 0),
                end_time=111,
                email="hora_@gmail.com"
            )
        except EntityError as error:
            assert str(error)

    def test_negative_end_time(self):
        try:
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=time(7, 0),
                end_time=time(-1, 0),
                email="hora_h@gmail.com"
            )
        except ValueError as error:
            assert str(error)
    
    def test_end_time_before_start_time(self):
        with pytest.raises(EntityParameterTimeError):
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=time(8, 0),
                end_time=time(7, 0),
                email="hora_h@gmail.com"
            )

    def test_invalid_email(self):
        try:
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=time(7, 0),
                end_time=time(8, 0),
                email=111
            )
        except EntityError as error:
            assert str(error)
    
    def test_restaurant_name_none(self):
        try:
            restaurant = Restaurant(
                name=None, 
                start_time=time(7, 0),
                end_time=time(8, 0),
                email="hora_h@gmail.com"
            )
        except EntityError as error:
            assert str(error)

    def test_start_time_none(self):
        try:
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=None,
                end_time=time(8, 0),
                email="hora_h@gmail.com"
            )
        except EntityError as error:
            assert str(error)

    def test_end_time_none(self):
        try:
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=time(7, 0),
                end_time=None,
                email="hora_h@gmail.com"
            )
        except EntityError as error:
            assert str(error)

    def test_email_none(self):
        try:
            restaurant = Restaurant(
                name="HORA_H", 
                start_time=time(7, 0),
                end_time=time(8, 0),
                email=None
            )
        except EntityError as error:
            assert str(error)