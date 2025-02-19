'''import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
random.sample(n1, n2, n3, n4, 8)
print('A ordem de apresentação será: ')
print(lista)
'''

import random

nomes = ["Ana", "Carlos", "Mariana", "Pedro",
         "João", "Laura", "Felipe", "Beatriz"]
sorteados = random.sample(nomes, 4)

print("Nomes sorteados:", sorteados)
