sexo = str(input('Informe seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'M F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))


