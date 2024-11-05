from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def update_user_by_id(self, user_id: str, new_name: Optional[str] = None, new_photo: Optional[str] = None) -> User:
        pass

    @abstractmethod
    def delete_user_by_id(self, user_id: str) -> Optional[User]:
        pass

    def get_average_feedback_by_restaurant(self):
        pass

    @abstractmethod
    def get_all_users_by_restaurant(self, restaurant: RESTAURANT) -> List[User]:
        pass
