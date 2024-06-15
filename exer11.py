largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
área = largura * altura
print('A sua parede tem {} x {} e sua área é de {:.2f}m²'.format(largura, altura, área))
tinta = área / 2
print('Preciso de {:.2f}l de tinta pata pintar toda a parede.'.format(tinta))

