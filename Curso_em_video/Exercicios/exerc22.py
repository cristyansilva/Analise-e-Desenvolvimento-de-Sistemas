nome = str(input('Digite seu nome: '))
print(nome.upper())  # tudo em maiusculo
print(nome.lower())  # tudo em minusculo
print(len(nome))  # quantas letras em na string inteira
dividido = nome.split()  # gerar lista com o nome
print(nome.split())  # imprimir nome separado
print(len(dividido[0]))  # imprimir quantos caracteres tem no  primeiro nome
sem_espacos = ''.join(nome.split())  # remover espaço entre os caracteres
print(len(sem_espacos))  # imprimir string sem caracteres
