print('\033[1;33m-='*20)
print(' '*10, '\033[4;33m CALCULAR IMC \033[m')
peso = float(input('Peso (Kg): '))
alt = float(input('Altura (m): '))
imc = peso / (alt**2)
print('Seu indice de massa corporal é {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('\033[4;30mPARABÉNS VOCÊ ESTÁ NO PESO IDEAL\033[m')
elif 25 <= imc < 30:
    print('\033[4;30mSOBREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[4;30mOBESIDADE\033[m')
else:
    print('\033[4;30mCUIDADO! OBESIDADE MÓRBIDA\033[m')
