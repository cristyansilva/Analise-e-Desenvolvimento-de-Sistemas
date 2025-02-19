numero = int(input('Digite um Número de 0 a 9999: '))

# Obtendo cada casa decimal
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# exibindo os valores:

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
