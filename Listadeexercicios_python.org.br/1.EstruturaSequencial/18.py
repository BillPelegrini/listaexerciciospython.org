# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivomb = int(input('Informe o tamanho do arquivo em MB: '))
link = int(input('Informe a velocidade do link de Download em Mbps: '))

#File Size In Megabytes / (Download Speed In Megabits / 8) = Time In Seconds

tempo_segundos = arquivomb / (link / 8 )
minutes = tempo_segundos / 60
print(f'O download do arquivo levará {minutes:.1f} minutos')