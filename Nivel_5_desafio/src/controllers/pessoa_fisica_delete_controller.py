from src.models.sqlite.interfaces.pessoa_fisica_repository_interfaces import PessoaFisicaRepositoryInterface
from .interfaces.pessoa_fisica_delete_controller import PessoaFisicaDeleteControllerInterface

class PessoaFisicaDeleteController(PessoaFisicaDeleteControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def delete(self, id: str) -> None:
        self.__pessoa_fisica_repository.delete_pessoa_fisica(id)
