print('\033[1;33m-=\033[m'*40)
from datetime import date
ano = int(input('\033[4;35m Digite o ano ou zero para ano atual, para saber se é bissexto:\033[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('\033[4;32m{}\033[m é um ano bissexto.'.format(ano))
else:
    print('\033[4;32m{}\033[m não é um ano bissexto.'.format(ano))
