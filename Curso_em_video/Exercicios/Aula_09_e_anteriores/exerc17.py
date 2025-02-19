import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# hip = (co ** 2 + ca ** 2) ** (1/2)
# print('a hipotenusa vai medir {:.2f}'.format(hip))

hip = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hip))
