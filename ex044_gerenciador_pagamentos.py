print('{:=^40}'.format('\033[4;31m LOJAS ISADORA \033[m'))
valor = float(input('Valor do produto: R$ '))
print('''Opções de Pagamento
[1] Á vista em dinheiro ou cheque
[2] Á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Opção escolhida: '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} cada parcela '.format(totalparc, parcela))
else:
    total = valor
    print('\033[4;30;42mOPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!\033[m')
print('Sua compra é de R$ {:.2f} vai pagar R$ {:.2f} no final'.format(valor, total))
