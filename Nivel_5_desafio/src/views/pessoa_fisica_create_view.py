from src.controllers.interfaces.pessoa_fisica_create_controller import PessoaFisicaCreateControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PessoaFisicaCreateView(ViewInterface):
    def __init__(self, controller: PessoaFisicaCreateControllerInterface) -> None:
         self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        response = self.__controller.create(body)

        return HttpResponse(
            status_code=201,
            body=response
        )

