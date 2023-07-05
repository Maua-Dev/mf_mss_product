from abc import ABC, abstractmethod
from typing import Optional

from src.shared.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def update_user_by_id(self, user_id: str, new_name: Optional[str] = None, new_email: Optional[str] = None) -> User:
        pass

    @abstractmethod
    def delete_user_by_id(self, user_id: str) -> Optional[User]:
        pass
