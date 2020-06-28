soma = cont = n = 0

n = int(input('Digite um número e [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número e [999 para parar]: '))
print('Você digitou {} números e a soma é: {}'. format(cont, soma))
print('Fim do Programa!!!')
