# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número para saber se é impar ou par:  '))
r = n % 2
if r == 0:
    print(f'O número {n} \033[32mé PAR\033[0m.')
else:
    print(f'O número {n} \033[31mé ÍMPAR\033[0m.')
