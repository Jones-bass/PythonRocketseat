from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_create_controller import PessoaJuridicaCreateController
from src.views.pessoa_juridica_create_view import PessoaJuridicaCreateView

def pessoa_juridica_create_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaCreateController(model)
    view = PessoaJuridicaCreateView(controller)

    return view
