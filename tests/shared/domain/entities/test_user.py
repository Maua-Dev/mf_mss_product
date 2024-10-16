import pytest

from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class Test_User:
    def test_user_without_restaurant(self):
        user = User(name="Lucas Duez", email="21.00304-2@maua.br", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant=None, photo="https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=2000")
        
        assert type(user) == User 
        assert user.name == "Lucas Duez"
        assert user.email == "21.00304-2@maua.br"
        assert user.role == ROLE.ADMIN
        assert user.user_id == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert user.validate_user == True
        assert user.restaurant == None
        assert user.photo == "https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=2000"

    def test_user_with_restaurant(self):
        user = User(name="Lucas Duez", email="21.00304-2@maua.br", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU)
        
        assert type(user) == User 
        assert user.name == "Lucas Duez"
        assert user.email == "21.00304-2@maua.br"
        assert user.role == ROLE.ADMIN
        assert user.user_id == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert user.validate_user == True
        assert user.restaurant.value == "SOUZA_DE_ABREU"

    def test_invalid_name_type(self):
        with pytest.raises(EntityError):
            user = User(name=42, email="21.00306-8@maua.br", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU)

    def test_invalid_name_length(self):
        with pytest.raises(EntityError):
            user = User(name="Lu", email="21.00306-8@maua.br", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU)

    def test_invalid_name_characters(self):
        with pytest.raises(EntityError):
            user = User(name="Lau#$&*ra@Balb#$&()_+=achan666420", email="21.00306-8@maua.br", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU)
        
    def test_invalid_email(self): # FIX .@gmail.com
        with pytest.raises(EntityError):
            user = User(name="Laura Balbachan", email="@gmail.com", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU)
        
    def test_invalid_role(self):
        with pytest.raises(EntityError):
            user = User(name="Lucas Duez", email="21.00306-8@maua.br", role=10, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU)

    def test_invalid_user_id_length(self):
        with pytest.raises(EntityError):
            user = User(name="Lucas Duez", email="21.00306-8@maua.br", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab", validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU)

    def test_invalid_user_id(self):
        with pytest.raises(EntityError):
            user = User(name="Laura Balbachan", email="21.00306-8@maua.br", role=ROLE.ADMIN, user_id=[], validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU)

    def test_invalid_restaurant(self):
        with pytest.raises(EntityError):
            user = User(name="Laura Balbachan", email="21.00306-8@maua.br", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant={})
            
    def test_invalid_photo(self):
        with pytest.raises(EntityError):
            user = User(name="Laura Balbachan", email="21.00306-8@maua.br", role=ROLE.ADMIN, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", validate_user=True, restaurant=RESTAURANT.SOUZA_DE_ABREU, photo=42)
    
    
