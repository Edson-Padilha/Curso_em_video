from datetime import date
print('\033[1;33m-=\033[m'*20)
print(' '*10, '\033[4;33m CATEGORIAS \033[m')
nascimento = int(input('\033[1;34m Ano de nascimento: \033[m'))
categoria = date.today().year - nascimento
print('\033[1;33m Você tem {} anos, sua categoria é:\033[m'.format(categoria))
if categoria <= 9:
    print('\033[4;33m MIRIM \033[m')
elif categoria <= 14:
    print('\033[4;33m INFANTIL \033[m')
elif categoria <= 19:
    print('\033[4;33m JÚNIOR \033[m')
elif categoria <= 20:
    print('\033[4;33m SÊNIOR \033[m')
else:
    print('\033[4;33m MASTER \033[m')