from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_delete_controller import PessoaJuridicaDeleteController
from src.views.pessoa_juridica_delete_view import PessoaJuridicaDeleteView

def pessoa_juridica_delete_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaDeleteController(model)
    view = PessoaJuridicaDeleteView(controller)

    return view
