#Faça um Programa que leia três números e mostre o maior e o menor deles.
nums = input('Digite 3 números e pressione Enter: ')
lista = nums.split()
print(f'O maior numero é {max(lista)}, e o menor é {min(lista)}')