from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.controllers.pessoa_fisica_lister_controller import PessoaFisicaListerController


class MockPessoaFisicaRepository:
    def list_pessoas_fisicas(self):
        return [
            PessoaFisicaTable(
                id=1,
                nome="João Silva",
                cpf="12345678901",
                email="joao@email.com",
                telefone="11999999999",
                cidade="São Paulo"
            ),
            PessoaFisicaTable(
                id=2,
                nome="Maria Souza",
                cpf="98765432100",
                email="maria@email.com",
                telefone="11888888888",
                cidade="Rio de Janeiro"
            ),
        ]


def test_list_pessoas_fisicas():
    controller = PessoaFisicaListerController(MockPessoaFisicaRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "PessoaFisica",
            "count": 2,
            "attributes": [
                {
                    "id": 1,
                    "nome": "João Silva",
                    "cpf": "12345678901",
                    "email": "joao@email.com",
                    "telefone": "11999999999",
                    "cidade": "São Paulo",
                },
                {
                    "id": 2,
                    "nome": "Maria Souza",
                    "cpf": "98765432100",
                    "email": "maria@email.com",
                    "telefone": "11888888888",
                    "cidade": "Rio de Janeiro",
                }
            ]
        }
    }

    assert response == expected_response