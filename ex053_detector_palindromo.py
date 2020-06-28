frase = str(input('Digite uma frase: ' )).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('A frase digitada é {}'.format(frase))
print('O inverso de {} invertida é {}'.format(junto, inverso))
if inverso == junto:
    print('È PALÍNDROMO')
else:
    print('Não é PALÍNDROMO')