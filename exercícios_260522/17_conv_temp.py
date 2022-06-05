# 17) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida conversão.

convert = str(input('Quer converter Fahrenheit ou Celsius? '))

if convert == 'fahrenheit':
    temp1 = float(input('Insira a temperatura em °F: '))
    print(f'A temperatura em Celsius é de {(temp1-32) * 5/9: .2f}°C')

if convert == 'celsius':
    temp2 = float(input('Insira a temperatura em °C: '))
    print(f'A temperatura em Fahrenheit é de {(temp2 * (9/5))+32}°F')
