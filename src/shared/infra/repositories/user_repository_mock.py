from typing import List, Optional

from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users_list: List[User]

    def __init__(self):
        self.users_list = [
            User(name="Lucas Duez", email="lucas.santos@gmail.com", role=ROLE.ADMIN,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", restaurant=None, photo="https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=2000"),
            User(name="Vitor Sollas", email="vitinho.dev@maua.br", role=ROLE.ADMIN,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae5", restaurant=None, photo="https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D&w=1000&q=80"),
            User(name="Laura Carolina", email="email.da.laura@gmail.com", role=ROLE.OWNER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb", restaurant=RESTAURANT.CANTINA_DO_MOLEZA, photo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg"),
            User(name="João Brancas", email="brancas.dev@gmail.com", role=ROLE.OWNER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48af4", restaurant=RESTAURANT.SOUZA_DE_ABREU, photo="https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*"),
            User(name="Lucas Milas", email="milas@maua.br", role=ROLE.USER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", restaurant=None, photo="https://img.freepik.com/free-photo/puppy-that-is-walking-snow_1340-37228.jpg"),
            User(name="Rodrigo Morales", email="rodrigo.morales@gmail.com", role=ROLE.USER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48af9", restaurant=None, photo="https://static.vecteezy.com/system/resources/thumbnails/017/323/715/small/3d-render-adorable-close-up-of-a-american-eskimo-dog-holding-red-rose-in-mouth-on-white-background-photo.jpg"),
            User(name="José", email="ze@porteiros.br", role=ROLE.USER,
                 user_id="93bc6ada-c0d1-7054-66ab-e17414c48af1", restaurant=None, photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0oeGAfSu9iKLTHqTxUM77GOOftgh6D-cTtQ&usqp=CAU"),
            User(name="Vilardi Bruno", email="deus@aws.br", role=ROLE.SELLER,
                 user_id="93bc6ada-c0d1-7054-66ab-egu923c48af1", restaurant=RESTAURANT.HORA_H, photo="https://img.freepik.com/fotos-premium/cachorro-araffe-usando-oculos-em-forma-de-coracao-em-um-cobertor-vermelho-ai-generativo_900321-60981.jpg?w=826"),
            User(name="Hector Guerrini", email="mago@ronaldo.br", role=ROLE.SELLER,
                 user_id="93bc6ada-c0d1-ab53-66ab-e17414c48af1", restaurant=RESTAURANT.CANTINA_DO_MOLEZA, photo="https://img.freepik.com/fotos-premium/cachorrinho-dachshund-vestido-com-fantasia-engracada-de-halloween-de-bruxa_220770-4618.jpg?w=1380"),
            User(name="Gabriel G Godoy", email="warrior@ww2.flutter", role=ROLE.USER,
                 user_id="93bc6ada-c0d1-7054-42je-e17414c48af1", restaurant=None, photo="https://img.freepik.com/fotos-gratis/pug-bonito-em-roupas-de-exercito_23-2148348097.jpg?w=826&t=st=1693438194~exp=1693438794~hmac=cce4d75839448ae01788d50b6c61881e23c57ca290b8a8c60dea932d73a387ac")
        ]

    def create_user(self, user: User) -> User:
        self.users_list.append(user)
        return user

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        for user in self.users_list:
            if user_id == user.user_id:
                return user
        return None

    def update_user_by_id(self, user_id: str, new_name: Optional[str] = None, new_photo: Optional[str] = None):
        user_to_update = self.get_user_by_id(user_id)

        if user_to_update is None:
            return None

        if new_name is not None:
            user_to_update.name = new_name
            
        if new_photo is not None:
            user_to_update.photo = new_photo

        # if new_email is not None:
        #     user_to_update.email = new_email

        return user_to_update

    def delete_user_by_id(self, user_id: str) -> Optional[User]:
        for user in self.users_list:
            if user_id == user.user_id:
                self.users_list.remove(user)
                return user
        return None
