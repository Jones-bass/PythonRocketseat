import pytest
from src.controllers.pessoa_juridica_create_controller import PessoaJuridicaCreateController


class MockPessoaJuridicaRepository:
    def insert_pessoa_juridica(
        self,
        razao_social: str,
        cnpj: str,
        email: str,
        telefone: str,
        cidade: str
    ):
        pass


def test_create():
    pessoa_juridica_info = {
        "razao_social": "Fulano de Tal",
        "cnpj": "11222333000181",
        "email": "fulano@email.com",
        "telefone": "79999999999",
        "cidade": "Aracaju"
    }

    controller = PessoaJuridicaCreateController(
        MockPessoaJuridicaRepository()
    )

    response = controller.create(pessoa_juridica_info)

    assert response["data"]["type"] == "PessoaJuridica"
    assert response["data"]["attributes"] == pessoa_juridica_info


def test_create_error_razao_social_invalido():
    pessoa_juridica_info = {
        "razao_social": "Fulano123",
        "cnpj": "11222333000181",
        "email": "fulano@email.com",
        "telefone": "79999999999",
        "cidade": "Aracaju"
    }

    controller = PessoaJuridicaCreateController(
        MockPessoaJuridicaRepository()
    )

    with pytest.raises(Exception):
        controller.create(pessoa_juridica_info)


def test_create_error_cnpj_invalido():
    pessoa_juridica_info = {
        "razao_social": "Fulano de Tal",
        "cnpj": "123",
        "email": "fulano@email.com",
        "telefone": "79999999999",
        "cidade": "Aracaju"
    }

    controller = PessoaJuridicaCreateController(
        MockPessoaJuridicaRepository()
    )

    with pytest.raises(Exception):
        controller.create(pessoa_juridica_info)