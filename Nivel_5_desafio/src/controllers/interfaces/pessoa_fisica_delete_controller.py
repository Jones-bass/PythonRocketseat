from abc import ABC, abstractmethod

class PessoaFisicaDeleteControllerInterface(ABC):

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
