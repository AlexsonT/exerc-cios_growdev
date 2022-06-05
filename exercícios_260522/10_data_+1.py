#10) Construa um algoritmo que leia uma data qualquer (dia, mês e ano) e calcule a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias. Lembre-se que um ano é bissexto quando for divisível por 4.

d = int(input('Insira um dia: '))
while d <= 0 or d > 31:
    print('Insira um dia válido!')
    print('Dias de 01 a 31!')
    d = int(input('Insira um dia: '))

m = int(input('Insira um mês: '))
while m <= 0 or m > 12:
    print('Insira um mês válido!')
    print('Mês de 01 a 12!')
    m = int(input('Insira um mês: '))

a = int(input('Insira um ano: '))
while a <=999 or a > 9999:
    print('Insira um ano válido!')
    print('Utilizar 4 dígitos!')
    a = int(input('Insira um ano: '))

if m == 2 and d == 28:
    if a % 4 == 0 and a % 100 !=0 or a / 400 == 0:
        nova_data = print(f'A data seguinte é: {d+1}/{m}/{a}')
    else:
        nova_data = print(f'A data seguinte é: 01/{m+1}/{a}')    
if m == 2 and d == 29:
    if a % 4 == 0 and a % 100 !=0 or a / 400 == 0:
        nova_data = print(f'A data seguinte é: 01/{m+1}/{a}')
if m == 2 and d < 28:
    nova_data = print(f'A data seguinte é: {d+1}/{m}/{a}')

if m == 12 and d == 31:
    nova_data = print(f'A data seguinte é: 01/01/{a+1}')

if m == 4 or m == 6 or m == 9 or m == 11:
    if d == 30:
        nova_data = print(f'A data seguinte é: 01/{m+1}/{a}')
    if d == 31:
        print('Data inválida!')
        print('Mês com 30 dias!')
    if d < 30:
        nova_data = print(f'A data seguinte é: {d+1}/{m}/{a}')    

if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
    if d == 31:
        nova_data = print(f'A data seguinte é: 01/{m+1}/{a}')
    if d < 31:
        nova_data = print(f'A data seguinte é: {d+1}/{m}/{a}')




