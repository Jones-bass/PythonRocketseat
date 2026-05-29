from src.models.sqlite.interfaces.pessoa_juridica_repository_interfaces import PessoaJuridicaRepositoryInterface
from .interfaces.pessoa_juridica_delete_controller import PessoaJuridicaDeleteControllerInterface

class PessoaJuridicaDeleteController(PessoaJuridicaDeleteControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def delete(self, id: str) -> None:
        self.__pessoa_juridica_repository.delete_pessoa_juridica(id)
