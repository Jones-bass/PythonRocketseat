from src.controllers.interfaces.orders_create_interface import OrdersCreatorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.view_interface import ViewInterface

class OrdersCreatorView(ViewInterface):
    def __init__(self, controller: OrdersCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.body.get("user_id")
        product_name = http_request.body.get("product_name")
        quantity = http_request.body.get("quantity")

        self.__validate_inputs(user_id, product_name, quantity)

        orders_info = {
            "user_id": user_id,
            "product_name": product_name,
            "quantity": quantity
        }

        response = self.__controller.create(orders_info)

        return HttpResponse(body=response, status_code=201)

    def __validate_inputs(
        self, user_id: any, product_name: any, quantity: any
    ) -> None:
        if (
            not user_id
            or not isinstance(user_id, int)
            or not product_name
            or not isinstance(product_name, str)
            or not quantity
            or not isinstance(quantity, int)
        ):
            raise HttpBadRequestError("Invalid Input")