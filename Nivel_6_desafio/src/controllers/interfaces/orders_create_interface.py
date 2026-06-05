from typing import Dict
from abc import ABC, abstractmethod

class OrdersCreatorInterface(ABC):

    @abstractmethod
    def create(self, orders_info: Dict) -> Dict:    
        pass
