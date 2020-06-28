print('-' * 65)
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
t = area/2
print('Sua parede tem {} x {} e sua área é de {}m²'.format (l, a, area))
print('Você vai precisar de {:.2f} litros de tinta para pintar a parede.'.format(t))
print('-' * 65)