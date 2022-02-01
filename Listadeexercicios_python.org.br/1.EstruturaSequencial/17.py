# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
from math import ceil


metrosquad = int(input('Informe a metragem (m²): '))
litros = metrosquad / 6
lata = 18 * 6
galao = 3.6 * 6
valorlt = 80.00
valorgl = 25.00
qtdlatas = metrosquad / lata
qtdgaloes = metrosquad / galao
valortotal_lata = ceil(qtdlatas)* valorlt
valortotal_galao = ceil(qtdgaloes)* valorgl

# mistura de latas e galoes
mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

valor_mistura = ((mistura_lata * 80) + (mistura_galao * 25))

valor_total = valor_mistura + (valor_mistura / 10)

print(f'Serão necessarias {ceil(qtdlatas)} latas e o valor é de: R${valortotal_lata:.2f}')
print(f'Serão necessarias {ceil(qtdgaloes)} latas e o valor é de: R${valortotal_galao:.2f}')
print(f'Serão necessarias {mistura_lata} latas e {mistura_galao} galoes e o valor é de: R${valor_total:.2f}')

