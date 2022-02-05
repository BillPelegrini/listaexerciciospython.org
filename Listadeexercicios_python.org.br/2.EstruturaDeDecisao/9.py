#Faça um Programa que leia três números e mostre-os em ordem decrescente.

nums = [int(x) for x in input('Digite 3 numeros e pressione Enter: ').split()]
print(*sorted(nums, reverse=True))
