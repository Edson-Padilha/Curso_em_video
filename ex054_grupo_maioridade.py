from datetime import date
cont = 0
menor = 0
maior = 0
for c in range(1,8):
    cont = cont + 1
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(cont)))
    atual = date.today().year - ano
    if atual <= 17:
       menor = menor + 1
    elif atual >= 18:
         maior = maior + 1
print('Ao todo tivemos {} pessoas menor de idade e também tivemos {} pessoas maiores de idade.'.format(menor, maior))