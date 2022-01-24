#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
sal_por_hora = float(input('Informe quanto você ganha por hora: '))
num_horas = float(input('Informe a quantidade de horas trabalhadas: '))
result = sal_por_hora * num_horas
print(f'O salario total para este mês é: R${result:.2f}')