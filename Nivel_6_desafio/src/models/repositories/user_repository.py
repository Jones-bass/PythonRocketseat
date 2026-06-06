from sqlite3 import Connection, IntegrityError

from src.models.interface.user_repository_interface import UserRepositoryInterface
from src.errors.error_types.http_conflict import HttpConflictError


class UserRepository(UserRepositoryInterface):

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str, email: str) -> None:
        cursor = self.__conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users (username, password, email)
                VALUES (?, ?, ?);
                """,
                (username, password, email)
            )

            self.__conn.commit()

        except IntegrityError as error:
            error_message = str(error)

            if "UNIQUE constraint failed: users.email" in error_message:
                raise HttpConflictError("Email já cadastrado")

            if "UNIQUE constraint failed: users.username" in error_message:
                raise HttpConflictError("Nome de usuário já cadastrado")

            raise error

    def get_user_by_email(self, email: str):
        cursor = self.__conn.cursor()

        cursor.execute(
            """
            SELECT id, username, email, password
            FROM users
            WHERE email = ?;
            """,
            (email,)
        )

        return cursor.fetchone()