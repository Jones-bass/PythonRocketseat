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
        
    def insert_pessoa_juridica(
            self,
            razao_social: str,
            cnpj: str,
            email: str,
            telefone: str,
            cidade: str
        ) -> None:

            with self.__db_connection as database:

                try:

                    juridica = PessoaJuridicaTable(
                        razao_social=razao_social,
                        cnpj=cnpj,
                        email=email,
                        telefone=telefone,
                        cidade=cidade
                    )

                    database.session.add(juridica)
                    database.session.commit()

                except Exception as exception:
                    database.session.rollback()
                    raise exception
    
    def delete_pessoa_juridica(self, id: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(PessoaJuridicaTable)
                    .filter(PessoaJuridicaTable.id == id)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception