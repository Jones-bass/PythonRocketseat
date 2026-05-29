from src.controllers.interfaces.pessoa_juridica_delete_controller import PessoaJuridicaDeleteControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PessoaJuridicaDeleteView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaDeleteControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.param["id"]
        self.__controller.delete(id)

        return HttpResponse(status_code=204)
