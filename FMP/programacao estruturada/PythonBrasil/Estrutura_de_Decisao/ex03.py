#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
s = str(input('Qual seu sexo? ')).strip() .upper()

if s == "M":
    print('Masculino')

elif s == "F":
    print('Feminino')
else:
    print('Sexo inválido.')