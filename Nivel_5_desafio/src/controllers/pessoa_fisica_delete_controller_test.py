from unittest.mock import Mock
from src.controllers.pessoa_fisica_delete_controller import PessoaFisicaDeleteController

def test_delete_pessoa_fisica():
    mock_repository = Mock()

    controller = PessoaFisicaDeleteController(mock_repository)
    controller.delete("<int:id>")

    mock_repository.delete_pessoa_fisica.assert_called_once_with("<int:id>")