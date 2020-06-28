print('-' * 85)
celsius = float(input('Qual é a temperatura que deseja converter? °C '))
conversao = celsius * 9 / 5 + 32
kelvin = celsius + 273
print('A temperatura de: {:.1f} °C convertida para Fahrenheit é: {:.1f}°F e para Kelvin é: {:.1f}°K'.format(celsius, conversao, kelvin))
print('-' * 85)
