from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaRepositoryInterface(ABC):
    @abstractmethod
    def list_pessoas_juridicas(self) -> list[PessoaJuridicaTable]:
        pass