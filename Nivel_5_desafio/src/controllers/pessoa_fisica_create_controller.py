from typing import Dict
import re
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.pessoa_fisica_repository_interfaces import PessoaFisicaRepositoryInterface
from .interfaces.pessoa_fisica_create_controller import PessoaFisicaCreateControllerInterface


class PessoaFisicaCreateController(PessoaFisicaCreateControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def create(self, pessoa_fisica_info: Dict) -> Dict:
        nome = pessoa_fisica_info["nome"]
        cpf = pessoa_fisica_info["cpf"]
        email = pessoa_fisica_info.get("email")
        telefone = pessoa_fisica_info.get("telefone")
        cidade = pessoa_fisica_info.get("cidade")

        self.__validate_nome(nome)
        self.__validate_cpf(cpf)

        self.__insert_person_in_db(nome, cpf, email, telefone, cidade)

        return self.__format_response(pessoa_fisica_info)

    def __validate_nome(self, nome: str) -> None:
        non_valid_characters = re.compile(r'[^a-zA-ZÀ-ÿ\s]')

        if non_valid_characters.search(nome):
            raise HttpBadRequestError("Nome da pessoa inválido!")

    def __validate_cpf(self, cpf: str) -> None:
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11:
            raise HttpBadRequestError("CPF inválido!")

    def __insert_person_in_db(self, nome: str, cpf: str, email: str, telefone: str, cidade: str) -> None:
        self.__pessoa_fisica_repository.insert_person(nome, cpf, email, telefone, cidade)

    def __format_response(self, pessoa_fisica_info: Dict) -> Dict:
        return {
            "data": {
                "type": "PessoaFisica",
                "attributes": pessoa_fisica_info
            }
        }