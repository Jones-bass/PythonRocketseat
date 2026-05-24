from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.pessoa_fisica_repository_interfaces import PessoaFisicaRepositoryInterface


class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pessoas_fisicas(self) -> list[PessoaFisicaTable]:
        with self.__db_connection as database:
            pessoas = (
                database.session
                .query(PessoaFisicaTable)
                .all()
            )
            return pessoas