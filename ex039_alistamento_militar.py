from datetime import date
print('\033[1;35m-=\033[m'*20)
print(' '*10,'\033[4;35mALISTAMENTO MILITAR\033[m')
ano = int(input('\033[1;35mAno de nascimento: \033[m'))
atual = date.today().year
idade = atual - ano
print('\033[1;32mQuem nasceu em {} tem {} anos em {}.\033[m'.format(ano, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('\033[1;32mAinda faltam {} anos para o alistamento.\033[m'.format(saldo))
    saldo = ano + 18
    print('\033[4;32mSeu alistamento será em {}.\033[m'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('\033[1;32mVocê já deveria ter se alistado há {} anos.\033[m'.format(saldo))
    saldo = ano + 18
    print('\033[1;32mSeu alistamento foi em {}\033[m'.format(saldo))
elif idade == 18:
    print('\033[1;32;40m Você tem que se alistar imediatamente! \033[m')