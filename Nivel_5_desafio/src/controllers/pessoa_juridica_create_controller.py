from typing import Dict
import re
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.pessoa_juridica_repository_interfaces import PessoaJuridicaRepositoryInterface
from .interfaces.pessoa_juridica_create_controller import PessoaJuridicaCreateControllerInterface


class PessoaJuridicaCreateController(PessoaJuridicaCreateControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def create(self, pessoa_juridica_info: Dict) -> Dict:
        razao_social = pessoa_juridica_info["razao_social"]
        cnpj = pessoa_juridica_info["cnpj"]
        email = pessoa_juridica_info.get("email")
        telefone = pessoa_juridica_info.get("telefone")
        cidade = pessoa_juridica_info.get("cidade")

        self.__validate_razao_social(razao_social)
        self.__validate_cnpj(cnpj)

        self.__insert_pessoa_juridica_in_db(
            razao_social, cnpj, email, telefone, cidade
        )

        return self.__format_response(pessoa_juridica_info)

    def __validate_razao_social(self, razao_social: str) -> None:
        non_valid_characters = re.compile(r'[^a-zA-ZÀ-ÿ\s]')

        if non_valid_characters.search(razao_social):
            raise HttpBadRequestError("razao_social da pessoa inválido!")

    def __validate_cnpj(self, cnpj: str) -> None:
        cnpj = re.sub(r'\D', '', cnpj)

        if len(cnpj) != 14:
            raise HttpBadRequestError("CNPJ inválido!")

        if cnpj == cnpj[0] * 14:
            raise HttpBadRequestError("CNPJ inválido!")

        def calculate_digit(cnpj_base: str, weights: list[int]) -> str:
            total = sum(
                int(digit) * weight
                for digit, weight in zip(cnpj_base, weights)
            )

            remainder = total % 11

            if remainder < 2:
                return "0"

            return str(11 - remainder)

        first_weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        second_weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        first_digit = calculate_digit(cnpj[:12], first_weights)
        second_digit = calculate_digit(cnpj[:12] + first_digit, second_weights)

        if cnpj[-2:] != first_digit + second_digit:
            raise HttpBadRequestError("CNPJ inválido!")

    def __insert_pessoa_juridica_in_db(
        self,
        razao_social: str,
        cnpj: str,
        email: str,
        telefone: str,
        cidade: str
    ) -> None:
        self.__pessoa_juridica_repository.insert_pessoa_juridica(
            razao_social, cnpj, email, telefone, cidade
        )

    def __format_response(self, pessoa_juridica_info: Dict) -> Dict:
        return {
            "data": {
                "type": "PessoaJuridica",
                "attributes": pessoa_juridica_info
            }
        }