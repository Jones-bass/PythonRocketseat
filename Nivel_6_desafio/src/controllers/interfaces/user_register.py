from typing import Dict
from abc import ABC, abstractmethod

class UserRegisterInterface(ABC):
    
    @abstractmethod
    def registry(self, username: str, password: str, email: str) -> Dict:
        pass