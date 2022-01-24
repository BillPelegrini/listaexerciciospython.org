#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
alt = float(input('Informe a sua altura: '))
peso = lambda x: (72.7 * x) - 58
print(f'Seu peso ideal é: {peso(alt):.1f}')