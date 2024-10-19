import os
from sqlalchemy import create_engine, Column, String, Integer, FLOAT
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
FOLHA_DE_PAGAMENTO = create_engine("sqlite:///folha de pagamento.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=FOLHA_DE_PAGAMENTO)
session = Session()


# Criando tabela.
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "Funcionários"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    email = Column("Email", String)
    senha = Column("Senha", String)
    salario = Column("Salário", FLOAT)
    vale_transporte = Column("Vale transporte", FLOAT)
    vale_refeicao = Column("Vale refeição", FLOAT)
    dependentes = Column("Dependentes", Integer)

    # Definindo atributos da classe.
    def __init__(self, email: str, salario:float, senha:str, vale_transporte:float, vale_refeicao: float, dependentes: int):
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
def exibindo_funcionario(funcionario):
    print(f"{funcionario.id} - Email: {funcionario.email} - Senha: {funcionario.senha} - Salário: {funcionario.salario} - Vale transporte: {funcionario.vale_transporte} - Vale refeição: {funcionario.vale_refeicao} - Dependentes: {funcionario.dependentes}")

def adicionar_folha_de_pagamento():
    funcionario = Funcionario(
        email=input("Digite sua matrícula: "),
        senha=input("Digite sua senha: "),
        salario=float(input("Digite quanto você recebe de salário: ")),
        vale_transporte=float(input("Digite quanto ganha de vale transporte: ")),
        vale_refeicao=float(input("Digite quanto ganha de vale refeição: ")),
        dependentes=int(input("Digite quantos dependentes você tem: "))
    )
    session.add(funcionario)
    session.commit()
    
def inss(salario):
    if salario <= 1100:
        return salario * 0.075
    elif salario <= 2203:
        return salario * 0.09
    elif salario <= 3305:
        return salario * 0.12
    elif salario <= 6433:
        return salario * 0.14
    else: 
        return 0
    
def irrf(salario, dependente):
    if salario <= 2259.20:
        return 0
    elif salario <= 2826.65:
        calculo_dependentes = 189.59 * dependente
        return (salario * 0.075) - calculo_dependentes
    elif salario <= 3751.05:
        calculo_dependentes = 189.59 * dependente
        return (salario * 0.15) - calculo_dependentes
    elif salario <= 4664.68:
        calculo_dependentes = 189.59 * dependente
        return (salario * 0.225) - calculo_dependentes
    else:
        calculo_dependentes = 189.59 * dependente
        return (salario * 0.275) - calculo_dependentes

def vale_refeicao(salario):
    calculo_refeicao = salario * 0.2
    return calculo_refeicao

def vale_transporte(salario):
    calculo_transporte = salario * 0.06
    return calculo_transporte

def plano_de_saude(depedente):
    calculo_dependente = 150 * depedente
    return calculo_dependente

def calcular_salario_liquido(salario, descontos, beneficios):
    calculo_salario = salario - descontos + beneficios
    return calculo_salario

inss_valor = inss()
irrf_valor = irrf()
vale_refeicao_valor = vale_refeicao()
vale_transporte_valor = vale_transporte()
plano_saude_valor = plano_de_saude()

# Calcular o salário líquido
descontos = inss_valor + irrf_valor
beneficios = vale_refeicao_valor + vale_transporte_valor
salario_liquido = calcular_salario_liquido

# Exibir resultados
#print(f"Salário Bruto: R$ {:.2f}")
print(f"INSS: R$ {inss_valor:.2f}")
print(f"IRRF: R$ {irrf_valor:.2f}")
print(f"Vale Refeição: R$ {vale_refeicao_valor:.2f}")
print(f"Vale Transporte: R$ {vale_transporte_valor:.2f}")
print(f"Plano de Saúde: R$ {plano_saude_valor:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

        
        
    
        

    

