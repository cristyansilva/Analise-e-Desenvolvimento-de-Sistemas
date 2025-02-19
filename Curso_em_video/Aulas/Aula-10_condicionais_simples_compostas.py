# como utilizar estruturas condicionais simples e compostas

# if = se    = simples
# else  = se nao    = composta

'''
exemplo1: 
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:  # se o carro for menor ou igual a 3 anos
    print('Carro novo')  # é novo
else:  # se não
    print('Carro velho')
print('--FIM__')
'''
# exemplo2
n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
n3 = float(input('Digite a Terceira nota: '))
s = ((n1*2) + (n2*2) + (n3*1))/5
print(f'Sua média foi: {s}.')
if s >= 7:
    print('Parabéns, você foi Aprovado!')
else:
    print('Reprovado! Estude mais no próximo semestre!')
