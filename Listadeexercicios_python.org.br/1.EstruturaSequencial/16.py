# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metrosquad = int(input('Informe a metragem (m²): '))
lata = 54
valor = 80.00
qtdlatas = metrosquad / lata
valortotal = round(qtdlatas)* valor
print(f'Serão necessarias {round(qtdlatas)} latas e o valor é de: R${valortotal:.2f}')