print('\033[1;36m-=-\033[m'*20)
print(' '*15,'\033[4;36m Base de Conversão \033[m')
numero = int(input('\033[1;36mDigite um numero para conversão: \033[m'))
print('\33[36m \33[m'*20)
opcao = int(input('''\033[1;36mEscolha a base para conversão: 
[1] BINÁRIO 
[2] OCTAL 
[3] HEXADECIMAL
 Sua opção: \33[m'''))
if opcao == 1:
    print('\033[1;36mO numero {} convertido para BINÁRIO é: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('\033[1;36mO numero {} convertido para OCTAL é: {}'.format(numero, oct(numero)[2:]))
elif opcao ==3:
    print('\033[1;36mO numero {} convertido para HEXADECIMAL é: {}\033[m'.format(numero, hex(numero)[2:]))
else:
    print('\033[4;36;40m OPÇÃO INCORRETA \033[m')
