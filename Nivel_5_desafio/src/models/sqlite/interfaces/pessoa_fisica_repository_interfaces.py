from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepositoryInterface(ABC):
    @abstractmethod
    def list_pessoas_fisicas(self) -> list[PessoaFisicaTable]:
        pass