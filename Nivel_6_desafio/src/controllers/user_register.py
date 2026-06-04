from typing import Dict
from src.models.interface.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from .interfaces.user_register import UserRegisterInterface


class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def registry(self, username: str, password: str, email: str) -> Dict:
        hashed_password = self.__create_hashed_password(password)

        self.__registry_new_user(username, hashed_password, email)

        return self.__format_response(username, email)

    def __create_hashed_password(self, password: str) -> str:
        return self.__password_handler.encrypt_password(password)

    def __registry_new_user(
        self, username: str, hashed_password: str, email: str
    ) -> None:
        self.__user_repository.registry_user(username, hashed_password, email)

    def __format_response(self, username: str, email: str) -> Dict:
        return {
            "type": "User",
            "count": 1,
            "username": username,
            "email": email
        }