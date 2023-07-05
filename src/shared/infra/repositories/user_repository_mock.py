from typing import List, Optional

from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users_list: List[User]

    def __init__(self):
        self.users_list = [
            User(name="Lucas Duez", email="lucas.bolinha@gmail.com", role=ROLE.ADMIN,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", restaurant=None),
            User(name="Vitebas de Soleia", email="big.boss@maua.br", role=ROLE.ADMIN,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae5", restaurant=None),
            User(name="Laura Carolina", email="email.da.laura@gmail.com", role=ROLE.OWNER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb", restaurant=RESTAURANT.CANTINA_DO_MOLEZA),
            User(name="Eh o brancas", email="ex.big.boss@gmail.com", role=ROLE.OWNER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48af4", restaurant=RESTAURANT.SOUZA_DE_ABREU),
            User(name="Lucas Milas", email="seila@maua.br", role=ROLE.USER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", restaurant=None),
            User(name="Rodas", email="rodando@carros.br", role=ROLE.USER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48af9", restaurant=None),
        ]

    def create_user(self, user: User) -> User:
        self.users_list.append(user)
        return user

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        for user in self.users_list:
            if user_id == user.user_id:
                return user
        return None

    def update_user_by_id(self, user_id: str, new_name: Optional[str] = None, new_email: Optional[str] = None):
        user_to_update = self.get_user_by_id(user_id)

        if user_to_update is None:
            return None

        if new_name is not None and User.validate_name(new_name):
            user_to_update.name = new_name

        if new_email is not None and User.validate_email(new_email):
            user_to_update.email = new_email

        return user_to_update

    def delete_user_by_id(self, user_id: str) -> Optional[User]:
        for user in self.users_list:
            if user_id == user.user_id:
                self.users_list.remove(user)
                return user
        return None
