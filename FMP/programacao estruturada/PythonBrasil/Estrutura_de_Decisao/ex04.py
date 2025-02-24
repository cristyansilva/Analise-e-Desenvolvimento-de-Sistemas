# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(
    input('Digite uma letra para ver se é vogal ou consoante: ')).strip() .upper()
if letra in 'AEIOU':
    print('Essa letra é uma vogal!')
else:
    print('Essa letra é uma consoante!')
