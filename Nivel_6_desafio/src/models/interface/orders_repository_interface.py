from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def create_order(self, user_id: int, product_name: str, quantity: int) -> None:
        pass