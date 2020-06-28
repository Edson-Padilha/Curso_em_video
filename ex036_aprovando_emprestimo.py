print('\033[1;32m-=-\033[m'*20)
print(' '*15, '\033[4;32mAnálise de Crédito\033[m')
valor = float(input('\033[1;32mQual o valor do imóvel? R$ \033[m'))
salário = float(input('\033[1;32mQual o valor do seu salário atual? R$ \033[m'))
anos = int(input('\033[1;32mEm quantos anos vai pagar? \033[m'))
meses = anos * 12
parcelas = valor / meses
percentual = salário * 30 / 100
if parcelas <= percentual:
    print('\033[4;36mEmpréstimo Aprovado\033[m')
    print('\033[1;32mO valor das parcelas será de R$ \033[4m{:.2f} em {} meses.\033[m'.format(parcelas, meses))
else:
    print('\033[1;32;46mEmpréstimo NEGADO!\033[m')
    print('\033[4;36mPara pagar um imóvel de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}\033[m'.format(valor, anos, parcelas))
