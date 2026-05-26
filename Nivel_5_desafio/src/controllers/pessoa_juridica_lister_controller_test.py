from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.controllers.pessoa_juridica_lister_controller import PessoaJuridicaListerController


class MockPessoaJuridicaRepository:
    def list_pessoas_juridicas(self):
        return [
            PessoaJuridicaTable(
                id=1,
                razao_social="João Mercado",
                cnpj="12345678000199",
                email="joao@email.com",
                telefone="11999999999",
                cidade="São Paulo"
            ),
            PessoaJuridicaTable(
                id=2,
                razao_social="Maria Panificadora",
                cnpj="12345678000100",
                email="maria@email.com",
                telefone="11888888888",
                cidade="Rio de Janeiro"
            ),
        ]


def test_list_pessoas_juridica():
    controller = PessoaJuridicaListerController(MockPessoaJuridicaRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "PessoaFisica",
            "count": 2,
            "attributes": [
                {
                    "id": 1,
                    "nome": "João Mercado",
                    "cpf": "12345678000199",
                    "email": "joao@email.com",
                    "telefone": "11999999999",
                    "cidade": "São Paulo",
                },
                {
                    "id": 2,
                    "nome": "Maria Panificadora",
                    "cpf": "12345678000100",
                    "email": "maria@email.com",
                    "telefone": "11888888888",
                    "cidade": "Rio de Janeiro",
                }
            ]
        }
    }

    assert response == expected_response