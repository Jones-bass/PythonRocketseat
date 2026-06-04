from typing import Dict
from abc import ABC, abstractmethod

class UserRegisterInterface(ABC):

    @abstractmethod
    def registry(self, username: str, email: str, password: str) -> Dict: pass
