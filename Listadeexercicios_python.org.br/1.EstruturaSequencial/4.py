#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1, n2, n3, n4 = [int(x) for x in input('Digite as suas notas: ').split()]
print((n1+n2+n3+n4)/4)