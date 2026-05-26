from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.sqlite.interfaces.pessoa_juridica_repository_interfaces import PessoaJuridicaRepositoryInterface

class PessoaJuridicaRepository(PessoaJuridicaRepositoryInterface):

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pessoas_juridicas(self) -> list[PessoaJuridicaTable]:

        with self.__db_connection as database:

            juridicas = (
                database.session
                .query(PessoaJuridicaTable)
                .all()
            )

            return juridicas
