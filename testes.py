import os
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
FOLHA_DE_PAGAMENTO = create_engine("sqlite:///folha de pagamento.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=FOLHA_DE_PAGAMENTO)
session = Session()


# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("emai", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=FOLHA_DE_PAGAMENTO)

# Salvar no banco de dados.
os.system("cls || clear")
