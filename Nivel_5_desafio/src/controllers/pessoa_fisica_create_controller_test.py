import pytest
from .pessoa_fisica_create_controller import PessoaFisicaCreateController


class MockPessoaFisicaRepository:
    def insert_person(
        self,
        nome: str,
        cpf: str,
        email: str,
        telefone: str,
        cidade: str
    ):
        pass


def test_create():
    pessoa_fisica_info = {
        "nome": "Fulano de Tal",
        "cpf": "12345678901",
        "email": "fulano@email.com",
        "telefone": "79999999999",
        "cidade": "Aracaju"
    }

    controller = PessoaFisicaCreateController(
        MockPessoaFisicaRepository()
    )

    response = controller.create(pessoa_fisica_info)

    assert response["data"]["type"] == "PessoaFisica"
    assert response["data"]["attributes"] == pessoa_fisica_info


def test_create_error_nome_invalido():
    pessoa_fisica_info = {
        "nome": "Fulano123",
        "cpf": "12345678901",
        "email": "fulano@email.com",
        "telefone": "79999999999",
        "cidade": "Aracaju"
    }

    controller = PessoaFisicaCreateController(
        MockPessoaFisicaRepository()
    )

    with pytest.raises(Exception):
        controller.create(pessoa_fisica_info)


def test_create_error_cpf_invalido():
    pessoa_fisica_info = {
        "nome": "Fulano de Tal",
        "cpf": "123",
        "email": "fulano@email.com",
        "telefone": "79999999999",
        "cidade": "Aracaju"
    }

    controller = PessoaFisicaCreateController(
        MockPessoaFisicaRepository()
    )

    with pytest.raises(Exception):
        controller.create(pessoa_fisica_info)