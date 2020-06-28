frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('Quantas vezes aparece a letra "A" na sua frase: {}'.format(frase.count('A')))
print('A primeira posição em que aparece é: {}'.format(frase.find('A') + 1))
print('A ultima posição em que aparece é: {}'.format(frase.rfind('A') + 1))