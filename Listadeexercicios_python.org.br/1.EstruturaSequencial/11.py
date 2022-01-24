# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo.

num1, num2 = [int(x) for x in input('Digite dois numeros inteiros: ').split()]
num3 = float(input('Digite um numero real: '))

result1 = lambda a,b: (a * 2) * (b / 2)
print(f'O produto do dobro do primeiro com metade do segundo: {result1(num1,num2)}')

result2 = lambda a,b: (a * 3) + b
print(f'A soma do triplo do primeiro com o terceiro: {result2(num1,num3)}')

print(f'O terceiro elevado ao cubo: {num3 ** 3}')