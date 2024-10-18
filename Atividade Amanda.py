import os
os.system("cls || clear")

calculo = 0
# Faixa salarial
faixa_salarial = int(input("Digite seu salario: "))

# Desconto INSS

if faixa_salarial <= 1100:
    calculo = faixa_salarial * 0.075
    print(f"Desconto: {calculo:.2f}")
elif faixa_salarial > 1100 or faixa_salarial < 2203:
    calculo = (faixa_salarial * 0.9) /100
    print(f"Desconto: {calculo:.2f}")
elif faixa_salarial > 2203 or faixa_salarial < 3305:
    calculo = (faixa_salarial * 0.12) /100
    print(f"Desconto: {calculo:.2f}")
elif faixa_salarial > 3305 or faixa_salarial < 6433:
    calculo = (faixa_salarial * 0.14) /100
    print(f"Desconto: {calculo:.2f}")

