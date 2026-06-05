from src.controllers.interfaces.user_register_interface import UserRegisterInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.view_interface import ViewInterface

class UserRegisterView(ViewInterface):
    def __init__(self, controller: UserRegisterInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")
        email = http_request.body.get("email")
        
        self.__validate_inputs(username, password, email)

        response = self.__controller.registry(username, password, email)
        return HttpResponse(body={ "data": response }, status_code=201)

    def __validate_inputs(self, username: any, password: any, email: str ) -> None:
        if (
            not username
            or not email
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ): raise HttpBadRequestError("Invalid Input")
