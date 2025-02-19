nome = str(input('Analisando seu nome: ')).strip()
print('Seu nome em maiusculo é:', nome.upper())  # tudo em maiusculo

print('Seu nome em minusculo é:', nome.lower())  # tudo em minusculo

# quantas letras em na string inteira

# -nome.count('') para contar sem espaços
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras no total',)

dividido = nome.split()  # gerar lista com o nome

print(nome.split())  # imprimir nome separado

print(len(dividido[0]))  # imprimir quantos caracteres tem no  primeiro nome

sem_espacos = ''.join(nome.split())  # remover espaço entre os caracteres

print(len(sem_espacos))  # imprimir string sem caracteres

print('')
