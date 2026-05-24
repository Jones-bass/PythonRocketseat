from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepositoryInterface(ABC):

    @abstractmethod
    def insert_pessoa_fisica(
        self,
        nome: str,
        cpf: str,
        email: str,
        telefone: str,
        cidade: str
    ) -> None:
        pass

    @abstractmethod
    def list_pessoas_fisicas(self) -> list[PessoaFisicaTable]:
        pass