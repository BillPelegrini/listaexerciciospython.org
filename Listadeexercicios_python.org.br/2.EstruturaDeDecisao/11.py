# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

def percentual(percent, salario):
    return int((percent * salario) / 100)
    
salario = int(input('Digite o salário do colaborador: '))

if salario <= 280:
    percent = 20
elif salario > 280 and salario < 700:
    percent = 15
elif salario > 700 and salario < 1500:
    percent = 10
elif salario > 1500:
    percent = 5

resultado = percentual(salario, percent)
salario_final = salario + resultado
print(f'Salario antes do reajuste {salario}')
print(f'Percentual aplicado foi {percent}')
print(f'Valor do aumento: {resultado}')
print(f'Novo salario: {salario_final}')