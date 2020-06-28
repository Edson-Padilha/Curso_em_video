print('\033[1;35m-='*20)
print('\033[4;36mMaior e Menor Valor\033[m')
print('\033[1;35m-=-\033[m'*20)
p = int(input('\033[4mPrimeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: \033[m'))
maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t
menor = s
if p < s and p < t:
    menor = p
if t < p and t < s:
    menor = t
print('\033[4;31m O maior numero é: \033[1;36m{}\033[m'.format(maior))
print('\033[4;32m O menor numero é: \033[1;35m{}\033[m'.format(menor))