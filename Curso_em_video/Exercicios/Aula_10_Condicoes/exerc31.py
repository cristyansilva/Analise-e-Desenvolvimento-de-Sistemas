# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem?  '))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    valor = (0.5*distancia)
    print(f"O preço por Km é 0.5. O preço da passagem ficou R${valor:.2f}")
else:
    distancia > 200
    valor2 = (0.45*distancia)
    print(f'O preço por KM é 0.45. O preço da passagem ficou: R${valor2:.2f}')
