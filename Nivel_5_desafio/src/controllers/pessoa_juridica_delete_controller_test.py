from unittest.mock import Mock
from src.controllers.pessoa_juridica_delete_controller import PessoaJuridicaDeleteController

def test_delete_pessoa_juridica():
    mock_repository = Mock()

    controller = PessoaJuridicaDeleteController(mock_repository)
    controller.delete("<int:id>")

    mock_repository.delete_pessoa_juridica.assert_called_once_with("<int:id>")