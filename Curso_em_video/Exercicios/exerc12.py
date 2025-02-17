valor_produto = float(input('Digite o preço do produto para ver o desconto: '))
desconto_produto = valor_produto - (valor_produto * 0.05)  # ou 5/100
print('O valor já aplicado o desconto ficaria: R$ {}'.format(desconto_produto))
