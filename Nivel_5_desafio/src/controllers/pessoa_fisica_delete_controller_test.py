from src.controllers.pessoa_fisica_delete_controller import PessoaFisicaDeleteController

def test_delete_pessoa_fisica(mocker):
    mock_repository = mocker.Mock()
    controller = PessoaFisicaDeleteController(mock_repository)
    controller.delete("amiguinho")

    mock_repository.delete_pets.assert_called_once_with("amiguinho")
