from typing import Dict, List
from src.models.sqlite.interfaces.pessoa_juridica_repository_interfaces import PessoaJuridicaRepositoryInterface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.controllers.interfaces.pessoa_juridica_lister_controller import PessoaJuridicaListerControllerInterface

class PessoaJuridicaListerController(PessoaJuridicaListerControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def list(self) -> Dict:
        juridicas = self.__get_juridica_in_db()
        response = self.__format_response(juridicas)
        return response

    def __get_juridica_in_db(self) -> List[PessoaJuridicaTable]:
        return self.__pessoa_juridica_repository.list_pessoas_juridicas()

    def __format_response(self, juridicas: List[PessoaJuridicaTable]) -> Dict:
        formatted_juridica = []

        for juridica in juridicas:
           formatted_juridica.append({
                "id": juridica.id,
                "nome": juridica.razao_social,
                "cpf": juridica.cnpj,
                "email": juridica.email,
                "telefone": juridica.telefone,
                "cidade": juridica.cidade,
            })

        return {
            "data": {
                "type": "PessoaFisica",
                "count": len(formatted_juridica),
                "attributes": formatted_juridica
            }
        }