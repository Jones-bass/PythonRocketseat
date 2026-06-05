from sqlite3 import Connection
from src.models.interface.orders_repository_interface import OrdersRepositoryInterface

class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_order(self, user_id: int, product_name: str, quantity: int) -> None:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
                INSERT INTO orders (user_id, product_name, quantity)
                VALUES (?, ?, ?)
            """,
            (user_id, product_name, quantity)
        )

        self.__conn.commit()