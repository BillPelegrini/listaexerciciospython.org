# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lados = [float(x) for x in input('Digite o valor dos lados do triangulo e pressione Enter: ').split()]

if 0 in lados:
    print('Não é possivel formar um triangulo')
else:
    print('É possivel formar um triangulo')

if lados[0] == lados[1] and  lados[0] == lados[2] and lados[1] == lados[2]:
    print('Equilátero')
elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
    print('Escaleno')
else:
    print('Isósceles')