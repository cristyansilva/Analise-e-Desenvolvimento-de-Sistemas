# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = str(input('Em qual turno você estuda? ')) .strip() .lower()
if 'manha' in turno:
    print('Bom dia!')
elif 'vespertino' in turno:
    print('Boa tarde!')
elif 'noturno' in turno:
    print('Boa noite!')
else:
    print('Valor inválido!')
