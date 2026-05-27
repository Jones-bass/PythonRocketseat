from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_delete_controller import PessoaFisicaDeleteController
from src.views.pessoa_fisica_delete_view import PessoaFisicaDeleteView

def pessoa_fisica_delete_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaDeleteController(model)
    view = PessoaFisicaDeleteView(controller)

    return view
