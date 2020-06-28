
peso = []
for c in range(1,6):
    peso.append(float(input('Peso da {}° pessoa: '.format(c))))
print('O maior peso lido foi {}kg'.format(max(peso)))
print('O menor peso lido foi {}kg'.format(min(peso)))
