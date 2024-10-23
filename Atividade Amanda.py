import os
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

os.system("cls || clear")

DADOS = create_engine('sqlite:///funcionarios.db')
Session = sessionmaker(bind=DADOS)
Base = declarative_base()

# Definindo a tabela de funcionários
class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    matricula = Column(String)
    senha = Column(String)
    salario = Column(Float)

Base.metadata.create_all(bind=DADOS)

# Calcular INSS
def calcular_inss(salario):
    if salario <= 1100.00:
        return salario * 0.075
    elif salario <= 2203.48:
        return salario * 0.09
    elif salario <= 3305.22:
        return salario * 0.12
    elif salario <= 6433.57:
        return salario * 0.14
    else:
        return 854.36

# Calcular IRRF
def calcular_irrf(salario, dependentes):
    if salario <= 2259.20:
        return 0
    elif salario <= 2826.65:
        return salario * 0.075 - (189.59 * dependentes)
    elif salario <= 3751.05:
        return salario * 0.15 - (189.59 * dependentes)
    elif salario <= 4664.68:
        return salario * 0.225 - (189.59 * dependentes)
    else:
        return salario * 0.275 - (189.59 * dependentes)

# Calcular salário líquido
def calcular_salario_liquido(salario, vale_transporte, vale_refeicao, dependentes):
    inss = calcular_inss(salario)
    irrf = calcular_irrf(salario, dependentes)
    desconto_vale_transporte = 0.06 * salario if vale_transporte.lower() == 's' else 0
    desconto_vale_refeicao = 0.20 * vale_refeicao

    total_descontos = inss + irrf + desconto_vale_transporte + desconto_vale_refeicao
    return salario - total_descontos

# Configuração do banco de dados
engine = create_engine('sqlite:///funcionarios.db')  # Removido echo=True
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adicionar funcionário para testes
def adicionar_funcionario(matricula, senha, salario):
    if session.query(Funcionario).filter_by(matricula=matricula).first() is None:
        novo_funcionario = Funcionario(matricula=matricula, senha=senha, salario=salario)
        session.add(novo_funcionario)
        session.commit()
        print(f"Funcionário {matricula} adicionado com sucesso.")
    else:
        print(f"Funcionário {matricula} já existe.")

# Função principal
def main():
        if session.query(Funcionario).count() == 0:
            matricula = input("Digite a matrícula: ").strip()
            senha = input("Digite a senha: ").strip()
            salario = float(input("Digite o salário: R$ "))
            adicionar_funcionario(matricula, senha, salario)

        # Solicitar matrícula e senha
        matricula = input("Digite sua matrícula: ").strip()
        senha = input("Digite sua senha: ").strip()

        funcionario = session.query(Funcionario).filter_by(matricula=matricula, senha=senha).first()

        if funcionario:
            salario = funcionario.salario
            dependentes = 1  # Considerando 1 dependente
            vale_transporte = input("Deseja receber vale transporte (s/n)? ")
            vale_refeicao = float(input("Digite o valor do vale refeição: R$ "))

            salario_liquido = calcular_salario_liquido(salario, vale_transporte, vale_refeicao, dependentes)
            print(f"Salário Líquido: R$ {salario_liquido:.2f}")
        else:
            print("Matrícula ou senha inválidos. Verifique os dados e tente novamente.")

main()

# Fechar a sessão
session.close()
