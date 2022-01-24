#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
cel = int(input('Informe a temperatura em Celsius: '))
result = lambda x: 9 / 5 * x + 32
print(result(cel))