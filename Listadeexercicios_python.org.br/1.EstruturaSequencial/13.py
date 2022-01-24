# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # Para homens: (72.7*h) - 58
    # Para mulheres: (62.1*h) - 44.7

alt = float(input('Informe sua altura: '))
pesoh = lambda x: (72.7 * x) - 58
pesof = lambda x: (62.1 * x) - 44.7
print(f' Peso ideal para homens: {pesoh(alt):.1f}')
print(f' Peso ideal para mulheres: {pesof(alt):.1f}')