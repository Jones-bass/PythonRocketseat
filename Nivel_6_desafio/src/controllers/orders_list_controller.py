from typing import Dict
from src.controllers.interfaces.orders_list_controller import OrdersListInterface
from src.models.interface.orders_repository_interface import OrdersRepositoryInterface


class OrdersListController(OrdersListInterface):
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def list(self, user_id: int) -> Dict:
        orders = self.__orders_repository.get_orders_by_user_id(user_id)

        formatted_orders = []

        for order in orders:
            formatted_orders.append({
                "id": order[0],
                "user_id": order[1],
                "product_name": order[2],
                "quantity": order[3]
            })

        return {
            "data": {
                "type": "Orders",
                "count": len(formatted_orders),
                "attributes": formatted_orders
            }
        }