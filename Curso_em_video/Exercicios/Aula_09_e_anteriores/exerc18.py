import math
ang = float(input('Digite o Ângulo: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tang))
