# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00


def percentual(percent, salario):
    return int((percent * salario) / 100)

def imposto_de_renda(bruto):
    if bruto <= 900:
        irpf = 0
    elif bruto > 900 and bruto <= 1500:
        irpf = 5
    elif bruto > 1500 and bruto < 2500:
        irpf = 10
    elif bruto > 2500:
        irpf = 20
    return irpf

def previdencia(bruto):
    if bruto <= 1100:
        inss = 7.5
    elif bruto > 1100 and bruto <= 2203.48:
        inss = 9
    elif bruto > 2203.49 and bruto <= 3305.22:
        inss = 12
    elif bruto > 3305.23 or bruto >= 6433.57:
        inss = 14
    return inss

valorhora = int(input('Digite o seu valor hora: '))
horastrab = int(input('Digite a quantida de horas trabalhadas: '))
bruto = valorhora * horastrab
irpf = percentual(imposto_de_renda(bruto),bruto)
imp_inss = percentual(previdencia(bruto),bruto)
sindicato = percentual(3,bruto)
fgts = percentual(11,bruto)
descontos = irpf + imp_inss + sindicato
salario = bruto - descontos

print ( 
f''' 
Salário Bruto: ({valorhora} * {horastrab})        : R$ {bruto:.2f}
(-) IR ({imposto_de_renda(bruto)}%)                     : R$ {irpf:.2f}  
(-) INSS ({previdencia(bruto)}%)                 : R$ {imp_inss:.2f}
(-) Sindicato (3%)              : R$ {sindicato:.2f}
FGTS (11%)                      : R$ {fgts:.2f}
Total de descontos              : R$ {descontos:.2f}
Salário Liquido                 : R$ {salario:.2f}
'''
)




