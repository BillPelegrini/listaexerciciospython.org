# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from sys import exit

def raiz(a,b,c):
    d = (b**2 - 4*a*c)
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)
    lista = [d,x1, x2]
    return lista


a = int(input('Digite um valor para a: '))

if a == 0:
    print('a = 0, a equação não é do segundo grau!')
    exit()
    
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))

if raiz(a,b,c)[0] < 0:
    print('Delta calculado é negativo, a equação não possui raizes reais. ')
elif raiz(a,b,c)[0] == 0:
    print(f'Delta calculado é igual a zero a equação possui apenas uma raiz real{raiz(a,b,c)[0]}')
elif raiz(a,b,c)[0] > 0:
    print(f'A equação possui duas raizes reais x1 = {raiz(a,b,c)[1]} e x2 = {raiz(a,b,c)[2]}')
