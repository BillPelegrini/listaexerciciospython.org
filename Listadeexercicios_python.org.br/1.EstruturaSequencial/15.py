# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    # salário bruto.
    # quanto pagou ao INSS.
    # quanto pagou ao sindicato.
    # o salário líquido.
    # calcule os descontos e o salário líquido, conforme a tabela abaixo:
    # + Salário Bruto : R$
    # - IR (11%) : R$
    # - INSS (8%) : R$
    # - Sindicato ( 5%) : R$
    # = Salário Liquido : R$
    # Obs.: Salário Bruto - Descontos = Salário Líquido.

sal_por_hora = float(input('Informe quanto você ganha por hora: '))
num_horas = float(input('Informe a quantidade de horas trabalhadas: '))
bruto = sal_por_hora * num_horas
ir = 0.11 * bruto
inss = 0.08 * bruto
sindicato = 0.05 * bruto
descontos = ir + inss + sindicato
liquido = bruto - descontos
print(f'################ Total ###############')
print(f'+ Salário Bruto :...........R${bruto:.2f}')
print(f'- IR (11%):.................R${ir:.2f}')
print(f'- INSS (8%):................R${inss:.2f}')
print(f'- Sindicato (5%):...........R${sindicato:.2f}')
print(f'= Salário Liquido:..........R${liquido:.2f}')


