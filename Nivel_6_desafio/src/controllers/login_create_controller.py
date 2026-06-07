from typing import Dict

from src.models.interface.user_repository_interface import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler
from src.errors.error_types.http_unauthorized import HttpUnauthorizedError

from .interfaces.login_create_interface import LoginCreatorInterface


class LoginCreateController(LoginCreatorInterface):

    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()

    def create(self, email: str, password: str) -> Dict:
        user = self.__find_user(email)

        user_id = user[0]
        user_email = user[2]
        hashed_password = user[3]

        self.__verify_correct_password(password, hashed_password)

        token = self.__create_jwt_token(user_id)

        return self.__format_response(user_email, token)

    def __find_user(self, email: str) -> Dict:
        user = self.__user_repository.get_user_by_email(email)

        if not user:
            raise HttpUnauthorizedError("Email ou senha inválidos")

        return user

    def __verify_correct_password(self, password: str, hashed_password: str) -> None:
        is_password_correct = self.__password_handler.check_password(
            password,
            hashed_password
        )

        if not is_password_correct:
            raise HttpUnauthorizedError("Email ou senha inválidos")

    def __create_jwt_token(self, user_id: int) -> str:
        payload = {
            "user_id": user_id
        }

        token = self.__jwt_handler.create_jwt_token(payload)

        return token

    def __format_response(self, email: str, token: str) -> Dict:
        return {
            "access": True,
            "email": email,
            "token": token
        }