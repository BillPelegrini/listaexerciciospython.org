#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
fah = int(input('Informe a temperatura em Fahrenheit: '))
result = lambda x: 5 * ((x - 32) / 9) 
print(result(fah))