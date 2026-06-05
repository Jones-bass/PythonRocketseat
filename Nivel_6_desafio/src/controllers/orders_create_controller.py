from typing import Dict
from src.models.interface.orders_repository_interface import OrdersRepositoryInterface
from .interfaces.orders_create_interface import OrdersCreatorInterface

class OrdersCreateController(OrdersCreatorInterface):
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def create(self, orders_info: Dict) -> Dict:
        user_id = orders_info["user_id"]
        product_name = orders_info["product_name"]
        quantity = orders_info["quantity"]

        self.__insert_order_in_db(user_id, product_name, quantity)

        formatted_response = self.__format_response(orders_info)
        return formatted_response

    def __insert_order_in_db(
        self, user_id: int, product_name: str, quantity: int
    ) -> None:
        self.__orders_repository.create_order(user_id, product_name, quantity)

    def __format_response(self, orders_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Order",
                "count": 1,
                "attributes": orders_info
            }
        }