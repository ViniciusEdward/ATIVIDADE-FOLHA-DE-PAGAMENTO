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
    email = Column("Email", String)
    senha = Column("Senha", String)
    salario = Column("Salário", float)
    vale_transporte = Column("Vale transporte", float)
    vale_refeicao = Column("Vale refeição", float)
    dependentes = Column("Dependentes", String)

    # Definindo atributos da classe.
    def __init__(self, email: str, salario:float, senha:str, vale_transporte:float, vale_refeicao: float, dependentes: str):
        self.email = email
        self.senha = senha
        self.salario = salario
        self.vale_transporte = vale_transporte
        self.vale_refeicao = vale_refeicao
        self.dependentes = dependentes

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=FOLHA_DE_PAGAMENTO)

# Salvar no banco de dados.
os.system("cls || clear")
def adicionar_folha_de_pagamento():
    inserir_email = input("Digite sua matrícula: ")
    inserir_senha = input("Digite sua senha: ")
    inserir_salario = input("Digite quanto você recebe de salário: ")
    inserir_vale_transporte = input("Digite quanto ganha de vale transporte: ")
    inserir_vale_refeicao = input("Digite quanto ganha de vale refeição: ")
    inserir_dependentes = input("Digite quantos dependentes você tem: ")
    session.add(FOLHA_DE_PAGAMENTO)
    session.commit()



        

