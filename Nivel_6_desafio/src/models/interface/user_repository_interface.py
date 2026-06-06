from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def registry_user(self, username: str, password: str, email: str) -> None:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str):
        pass