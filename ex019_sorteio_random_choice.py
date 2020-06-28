from  random import choice
print('=' * 40)
n1 = str(input('Nome do aluno 1: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto e ultimo aluno: '))
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print('O aluno sorteado é: {}'.format (sorteio))
print('=' * 40)