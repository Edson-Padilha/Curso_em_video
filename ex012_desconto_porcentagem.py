print('-' * 70)
preço = float(input('Qual o valor do produto R$ '))
novo = preço - (preço * 5 / 100)
print('O valor do produto é R$ {:.2f} com desconto de 5% vai custar R$ {:.2f} '.format(preço, novo))
print('-' * 70)