# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade atual do carro?  '))
limite = 80
multa = 7

if v > limite:
    excesso = v - limite
    m = excesso*multa
    print(f'Você foi multado! Ultrapassou o limite de {limite}Km/h.')
    print(f'\033[31m Você deve pagar uma multa de R${m}\033[0m]')
print('Tenha um bom dia! Dirija com segurança!')


'''
print("\033[31mTexto em vermelho\033[0m")  # 31 = vermelho
print("\033[32mTexto em verde\033[0m")    # 32 = verde
print("\033[33mTexto em amarelo\033[0m")  # 33 = amarelo
print("\033[34mTexto em azul\033[0m")     # 34 = azul
'''
