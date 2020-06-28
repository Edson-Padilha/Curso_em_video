from time import sleep
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opcao = 0
maior = [n1, n2]
resultado = 0
while opcao != 5:
    print('''
             [1] Somar
             [2] Multiplicar
             [3] Maior
             [4] Novos Números
             [5] Sair do Programa''')

    opcao = int(input('>>>> Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é: {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print('A multiplicação de {} x {} é: {} '.format(n1, n2, multiplica))
    elif opcao == 3:
        resultado = max(maior)
        print('O maior numero de {} e {} é: {}'.format(n1, n2, resultado))
    elif opcao == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    elif opcao == 5:
        print('\033[33mFinalizando....\033[m')
    else:
        print('Opção Inválida!!!')
    print('-==' * 20)
    sleep(2)
print('Fim do Programa! Volte sempre!')











