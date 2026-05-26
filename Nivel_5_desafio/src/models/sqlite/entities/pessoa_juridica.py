from sqlalchemy import Column, String, Integer
from src.models.sqlite.settings.base import Base

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String(100), nullable=False)
    cnpj = Column(String(11), nullable=False, unique=True)
    email = Column(String(100), nullable=True)
    telefone = Column(String(20), nullable=True)
    cidade = Column(String(100), nullable=True)

    def __repr__(self):
        return (
            f"PessoaJuridica("
            f"id={self.id}, razao_social={self.razao_social}, cnpj={self.cnpj})"
        )
    

