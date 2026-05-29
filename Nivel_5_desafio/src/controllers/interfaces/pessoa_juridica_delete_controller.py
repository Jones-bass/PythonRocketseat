from abc import ABC, abstractmethod

class PessoaJuridicaDeleteControllerInterface(ABC):

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
