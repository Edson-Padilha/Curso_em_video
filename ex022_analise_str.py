nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letra maiuscula: {}'.format(nome.upper()))
print('Em letra minuscula: {}'.format(nome.lower()))
print('Seu nome tem no total: {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} tem: {} letras'.format(separa[0], len(separa[0])))