# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
def conceito(media):
    if media >= 9.0 or media == 10:
        return 'A'
    elif media >= 7.5 and media < 9:
        return 'B'
    elif media >= 6 and media < 7.5:
        return 'C'
    elif media >= 4 and media < 6:
        return 'D'
    elif media >= 4 and media == 0:
        return 'E'

notas = [int(x) for x in input('Digite suas notas e pressione Enter: ').split()]
media = sum(notas) / len(notas)
apr = ['A', 'B', 'C']
repr = ['D', 'E']

print(f'Notas do aluno: {notas}')
print(f'Média do aluno: {media}')
print(f'Conceito: {conceito(media)}')
if conceito(media) in apr:
    print('APROVADO')
else:
    print('REPROVADO')