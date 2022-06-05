#13) Sabendo que há 60 segundos em um minuto, 3.600 segundos em uma hora e 86.400 segundos em um dia, crie um algoritmo que a partir de uma determinada quantidade de segundos fornecida pelo usuário, converte-a da seguinte maneira:
#a) Se a quantidade de segundos for maior ou igual a 60, o programa deverá exibir o número de minutos equivalente;
#b) Se a quantidade de segundos for maior ou igual a 3.600, o programa deverá exibir o número de horas equivalente;
#c) Se a quantidade de segundos for maior ou igual a 86.400, o programa deverá exibir o número de dias equivalente.

print('*'*50)  
seg = int(input('Insira os segundos a converter: '))

if seg < 60:
    print(f'Obtemos: {seg} segundo(s).')
elif seg < 3600:
    print(f'Obtemos: {seg / 60: .2f} minuto(s).')
elif seg < 86400:
    print(f'Obtemos: {seg / 3600: .2f} hora(s).')
else:
    print(f'Obtemos: {seg / 86400: .2f} dia(s).') 

print('*'*50)               