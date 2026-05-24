from sqlalchemy import Column, String, Integer, DateTime, func
from src.models.sqlite.settings.base import Base


class PessoaFisicaTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    email = Column(String(100), nullable=True)
    telefone = Column(String(20), nullable=True)
    cidade = Column(String(100), nullable=True)


    def __repr__(self):
        return (
            f"PessoaFisica("
            f"id={self.id}, nome={self.nome}, cpf={self.cpf})"
        )