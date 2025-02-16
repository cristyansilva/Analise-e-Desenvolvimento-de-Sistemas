pao = int(input('Quantos Pãeszinhos foi vendido hoje? '))
broa = int(input('Quantas Broas foram vendidas hoje? '))
custo_pao = (pao * 0.12)
custo_broa = (broa * 1.50)
t1 = custo_pao + custo_broa
t2 = (t1 * 10/100)  # ou 0.10
print('Hoje foram vendidos {} pãeszinhos!'.format(pao))
print('Hoje foram vendidas {} broas!'. format(broa))
print('Hoje somando as vendas de Pães e Broas, tivemos um total de: R${}.'.format(t1))
print(
    'Desse valor, deve guardar (10%) do valor arrecadado, totalizando:R${:.2f}'.format(t2))
