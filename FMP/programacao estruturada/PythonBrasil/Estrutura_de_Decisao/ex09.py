# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
numeros = [n1, n2, n3]  # cria uma lista com os numeros
numeros.sort()  # ordena os numeros do menor para o maior.
print('Os números em ordem crescente são: ', numeros)
