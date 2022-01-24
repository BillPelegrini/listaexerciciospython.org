#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
r = int(input('Digite o raio do circulo: '))
result = math.pi * (r ** 2)
print(f'A área do circulo é :{result:.2f}')