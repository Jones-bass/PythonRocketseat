from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaRepositoryInterface(ABC):
    @abstractmethod
    def list_pessoas_juridicas(self) -> list[PessoaJuridicaTable]:
        pass

    @abstractmethod
    def delete_pessoa_juridica(self, id: str) -> None:
        pass
