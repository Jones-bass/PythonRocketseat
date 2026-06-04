from typing import Tuple
from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    def registry_user(self, username: str, email: str, password: str) -> None: pass
