#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ').lower()
vogais = ['a','e','i','o','u']
print('Consoante' if letra not in vogais else 'Vogal')