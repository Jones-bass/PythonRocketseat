from typing import Dict, List
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.pessoa_fisica_repository_interfaces import PessoaFisicaRepositoryInterface
from src.controllers.interfaces.pessoa_fisica_lister_controller import PessoaFisicaListerControllerInterface

class PessoaFisicaListerController(PessoaFisicaListerControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def list(self) -> Dict:
        pessoas = self.__get_pessoas_in_db()
        response = self.__format_response(pessoas)
        return response

    def __get_pessoas_in_db(self) -> List[PessoaFisicaTable]:
        return self.__pessoa_fisica_repository.list_pessoas_fisicas()

    def __format_response(self, pessoas: List[PessoaFisicaTable]) -> Dict:
        formatted_pessoas = []

        for pessoa in pessoas:
           formatted_pessoas.append({
                "id": pessoa.id,
                "nome": pessoa.nome,
                "cpf": pessoa.cpf,
                "email": pessoa.email,
                "telefone": pessoa.telefone,
                "cidade": pessoa.cidade,
            })

        return {
            "data": {
                "type": "PessoaFisica",
                "count": len(formatted_pessoas),
                "attributes": formatted_pessoas
            }
        }