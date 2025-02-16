print('Para saber quanto de tinta você vai precisar, preencha os valores abaixo: ')
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura*largura
litros_tinta = area/2
print('Então você tem uma parede de {} m².'.format(area))
print('Sendo assim, você precisara de {:.2f}L, para pintar toda a parede'.format(
    litros_tinta))
