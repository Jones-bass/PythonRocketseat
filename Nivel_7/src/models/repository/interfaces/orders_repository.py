from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def insert_document(self, document: dict) -> None: pass
