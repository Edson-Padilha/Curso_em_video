v = float(input(' Qual velocidade do carro? '))
if v > 80:
    multa = (v-80)*7
    print('Você foi multado, velocidade acima do permitido 80km/h. Sua multa é de R$ {:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')
