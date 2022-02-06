#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input("Digite um numero de 1 a 7: "))
if dia not in range(1,8):
    print('Numero invalido, por favor digite um numero de 1 a 7')
else:
    dias_da_semana = ('Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado')
    print(f'O dia da semana é: {dias_da_semana[dia-1]}')