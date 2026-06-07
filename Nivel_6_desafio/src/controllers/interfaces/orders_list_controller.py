from abc import ABC, abstractmethod
from typing import Dict


class OrdersListInterface(ABC):

    @abstractmethod
    def list(self, user_id: int) -> Dict:
        pass