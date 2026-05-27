from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepositoryInterface(ABC):
    @abstractmethod
    def list_pessoas_fisicas(self) -> list[PessoaFisicaTable]:
        pass

    @abstractmethod
    def delete_pessoa_fisica(self, id: str) -> None:
        pass
