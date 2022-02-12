# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

def verificacasadecimal(lista):     
        if len(lista) == 3:
            if lista[0] == 1:
                centenas = f'{lista[0]} centena'
            else:
                centenas = f'{lista[0]} centenas'
            if lista[1] == 1:
                dezenas = f'{lista[1]} dezena'
            else:
                dezenas = f'{lista[1]} dezenas'
            if lista[2] == 1:
                unidades = f'{lista[2]} unidade'
            else:
                unidades = f'{lista[2]} unidades'
            return [centenas, dezenas, unidades]

        if len(lista) == 2:
            if lista[0] == 1:
                dezenas = f'{lista[0]} dezena'
            else:
                dezenas = f'{lista[0]} dezenas'
            if lista[1] == 1:
                unidades = f'{lista[1]} unidade'
            else:
                unidades = f'{lista[1]} unidades'
            return [dezenas, unidades]

        if len(lista) == 1:
            if lista[0] == 1:
                unidades = f'{lista[0]} unidade'
            else:
                unidades = f'{lista[0]} unidades'
            return [unidades]



num = input('Digite um numero entre 0 e 1000: ')


if int(num) > 1000 or int(num) < 0:
    print('ERRO! Numero somente entre 0 e 1000!')
else:
    lista = [int(x) for x in str(num)]
    if len(lista) == 4:
        milhar,centena,dezena,unidade = lista
        print(f'1 milhar, 0 centenas, 0 dezenas e 0 unidades')
    elif len(lista) == 3:
        resultado = verificacasadecimal(lista)
        print(num, f'= {resultado[0]}, {resultado[1]} e {resultado[2]}')
    elif len(lista) == 2:
        resultado = verificacasadecimal(lista)
        print(num, f'= {resultado[0]} e {resultado[1]}')
    elif len(lista) == 1:
        resultado = verificacasadecimal(lista)
        print(num, f'= {resultado[0]}')
