from sqlite3 import Connection
from src.models.interface.user_repository_interface import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str, email: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (username, password, email)
            VALUES (?, ?, ?);
            """,
            (username, password, email)
        )
        self.__conn.commit()

    def get_user_by_username(self, email: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT id, email, password, email
            FROM users
            WHERE email = ?
            """,
            (email,)
        )

        return cursor.fetchone()