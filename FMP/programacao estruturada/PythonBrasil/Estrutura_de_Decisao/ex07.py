# Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

menor = n1
if n2 < n3 and n3 < n2:
    menor = n2
if n3 < n2 and n2 < n3:
    menor = n3
print(f'O menor valor é {menor}')

maior = n1
if n2 > n3 and n3 < n2:
    maior = n2
if n3 > n2 and n2 < n3:
    maior = n3
print(f'O número maior é : {maior}')
