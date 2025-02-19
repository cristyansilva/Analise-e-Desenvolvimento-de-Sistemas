# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.


# n1 = str(input('Digite seu nome completo: ')).strip
nome = (input('Digite seu nome completo: ')) .strip
dividido = (nome.split())
print('Primeiro nome:', dividido[0])
print('Ultimo nome:', dividido[3])
