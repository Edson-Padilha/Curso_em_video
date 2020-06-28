nome = str(input('Digite seu nome completo: ')).upper().strip()
nome = nome.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo sobrenome é: {}'.format(nome[len(nome)-1]))