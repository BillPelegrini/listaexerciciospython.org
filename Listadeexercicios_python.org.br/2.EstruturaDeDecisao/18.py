# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Informe uma data no formato dd/mm/aaaa: ').split('/')

if len(data[0]) != 2:
    print('Formato de dia invalido')
elif len(data[1]) != 2:
    print('Formato de mês invalido')
elif len(data[2]) != 4:
    print('Formato de ano invalido')

dataint = [int(x) for x in data]
    
if dataint[0] > 31:
    print('Dia invalido: ', dataint[0])
elif dataint[1] > 12:
    print('Mês invalido: ', dataint[1])
elif dataint[2] < 0000 or dataint[2] > 9999:
    print('Ano inválido: ', dataint[2])
else:
    
    print(f"Data válida: " + "/".join(data))   