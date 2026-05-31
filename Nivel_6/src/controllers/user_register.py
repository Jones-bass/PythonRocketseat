from src.models.interface.user_repository import UserRepositoryInterface
from .interfaces.user_register import UserRegisterInterface

class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        pass