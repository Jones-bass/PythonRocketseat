from src.controllers.interfaces.pessoa_fisica_delete_controller import PessoaFisicaDeleteControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PessoaFisicaDeleteView(ViewInterface):
    def __init__(self, controller: PessoaFisicaDeleteControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.param["id"]
        self.__controller.delete(id)

        return HttpResponse(status_code=204)
