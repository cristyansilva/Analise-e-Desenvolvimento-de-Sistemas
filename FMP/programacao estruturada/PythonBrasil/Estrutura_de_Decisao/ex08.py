# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
prod1 = float(input('Digite o valor do macarrão1: '))
prod2 = float(input('Digite o valor do macarrão2: '))
prod3 = float(input('Digite o valor do macarrão3: '))
menor = prod1
if prod2 < prod3 and prod3 > prod2:
    menor = prod2
if prod3 < prod2 and prod2 > prod3:
    menor = prod3
print(
    f'Sabendo que a decição é sempre pelo mais barato, você deve comprar o de R${menor:.2f}!')
