from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.view_interface import ViewInterface

class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        email = http_request.body.get("email")
        password = http_request.body.get("password")
        self.__validate_inputs(email, password)

        response = self.__controller.create(email, password)
        return HttpResponse(body={ "data": response }, status_code=200)

    def __validate_inputs(self, email: any, password: any) -> None:
        if (
            not email
            or not password
            or not isinstance(email, str)
            or not isinstance(password, str)
        ): raise HttpBadRequestError("Invalid Input")
