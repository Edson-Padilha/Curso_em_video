from datetime import time
inicio = float(input('Qual o horário de inicio: '))
final = float(input('Que horas terminou: '))
horas = float(final) - float(inicio)
valor = horas * 15
print('O total de horas é {:2f} O valor total a receber é R$ {:.2f}'.format(horas, valor))