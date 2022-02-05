#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produtos = input('Digite o valor de 3 produtos e pressione Enter: ')
lista = produtos.split()
print(f'O Produto mais barato custa R${min(lista)}')