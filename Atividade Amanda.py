import os
import sqlite3
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

os.system("cls || clear")

#Calcular INSS
def calcular_inss(salario):
    if salario <= 1100.00:
        desconto = salario * 0.075
    elif salario <= 2203.48:
        desconto = salario * 0.09
    elif salario <= 3305.22:
        desconto = salario * 0.12
    elif salario <= 6433.57:
        desconto = salario * 0.14
    else:
        desconto = 854.36
    return desconto

#Calcular IRRF
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

#Calcular os descontos e o salário líquido
def calcular_salario_liquido(salario, vale_transporte, vale_refeicao, dependentes):
    inss = calcular_inss(salario)
    irrf = calcular_irrf(salario, dependentes)
    desconto_vale_transporte = 0.06 * salario if vale_transporte.lower() == 's' else 0
    desconto_vale_refeicao = 0.20 * vale_refeicao

    total_descontos = inss + irrf + desconto_vale_transporte + desconto_vale_refeicao
    salario_liquido = salario - total_descontos
    
    return salario_liquido

#Conexão com o banco
conn = sqlite3.connect('funcionarios.db')
cursor = conn.cursor()

# Criar tabela de funcionários
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    matricula TEXT PRIMARY KEY,
    senha TEXT,
    salario REAL
)
''')

#Matrícula e senha
matricula = input("Digite sua matrícula: ")
senha = input("Digite sua senha: ")

#Consultar funcionário
cursor.execute("SELECT salario FROM funcionarios WHERE matricula = ? AND senha = ?", (matricula, senha))
resultado = cursor.fetchone()

if resultado:
    salario = resultado[0]
    dependentes = 1  # Considerando 1 dependente
    vale_transporte = input("Deseja receber vale transporte (s/n)? ")
    vale_refeicao = float(input("Digite o valor do vale refeição: R$ "))

    salario_liquido = calcular_salario_liquido(salario, vale_transporte, vale_refeicao, dependentes)
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
else:
    print("Matrícula ou senha inválidos.")

#Fechar a conexão
conn.close()