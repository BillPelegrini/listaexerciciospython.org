#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('Informe seu turno de estudos:')
letra = input('M - Matutino, V - Vespertino ou N - Noturno: ').upper()
opcoes = ['M','V','N']
if letra in opcoes:
    print('Bom dia' if letra == 'M' else ('Boa tarde' if letra == 'V' else 'Boa noite'))
else:
    print('Valor Inválido! Por favor digite somente M, V ou N')