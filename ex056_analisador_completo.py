soma = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1,5):
    print('-'*10,'{}° PESSOA'.format(c),'-'*10)
    nome = str(input('Nome: ')).strip().title()#retira os espacos
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    media = soma / 4
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mas velho tem {} anos e se chama {}. '.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos. '.format(totmulher20))




