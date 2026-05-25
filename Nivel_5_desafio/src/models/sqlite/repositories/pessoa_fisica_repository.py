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

    def insert_person(
        self,
        nome: str,
        cpf: str,
        email: str,
        telefone: str,
        cidade: str
    ) -> None:

        with self.__db_connection as database:

            try:

                pessoa = PessoaFisicaTable(
                    nome=nome,
                    cpf=cpf,
                    email=email,
                    telefone=telefone,
                    cidade=cidade
                )

                database.session.add(pessoa)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception