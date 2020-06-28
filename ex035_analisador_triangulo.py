print('-='*20)
print('\033[1;34mAnalisador de Triângulos\033[m')
print('-='*20)
p = float(input('Primeira medida: '))
s = float(input('Segunda medida: '))
t = float(input('Terceira medida: '))
if p < s + t and s < p + t and t < s + p:
            print('\033[4;36;40m Sim, existe a condição de existência de um triangulo.\033[m')
else:
    print('\033[4;30;41m Não existe a condição de um retângulo.\033[m')