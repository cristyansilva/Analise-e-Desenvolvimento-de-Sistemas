# Manipulando texto#

# Fatiamento: Frase[9] (mostra o caracter posicionado em 9 (V))

frase = 'Curso em Video Python'
# print(frase[9])  #(v)
# print(frase[9:13]) #Vide  vai do 9 ao 13, ignorando o ultimo que é o 13
# print(frase[:5])    #do inicio até a casa 5
# print(frase[15:])   #da casa 15 até o final da string
# print(frase[9::3])  #(VePh) inicia no 9 e vai pulando de 3 em 3 casas

# Análise
# 'len(frase)'  mostra o total de caracteres na string (Lean=comprimento)
# frase.count('o') = pedindo pra contar quantos 'o' tem na string
# frase.find('deo')  = find = encontrar (encontrar onde começou 'deo') -1 = nao encontrado
# print(frase.find('deo'))
# in = 'Curso' in frase = existe curso em frase ? True/False


# Transformação
# print(frase.replace('Python', 'Android')) #Substitui Python por Android
# print(frase.upper())   # todo o texto em maiusculo
# print(frase.lower())   #poe tudo em minusculo
# print(frase.capitalize())  #primeira letra da string em maiucsula apenas
# print(frase.title())   #primeira letra de cada palavra em maiuscula
# print(frase.strip()) # remove os espaços antes e depois da string "ex:       oi"
# print(frase.rstrip())  # remove somente os ultimos espaços r=direita
# print(frase.lstrip())   # remove somente os primeiros espaços l=esquerda

# Divisão

# print(frase.split())  # gera uma lista de todas as palavras dos caracteres 'Curso', 'em'

#junção

# print('-'.join(frase))  #poe um - no meio de cada letra
