# 9)Escreva um programa que peça ao usuário para fornecer um dia, mês e o ano arbitrários e determine se esses dados correspondem a uma data válida. Não deixe de considerar que existem meses com 30 e 31 dias, e que fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto. Considere que um ano é bissexto quando for divisível por 4.

d = int(input('Insira um dia: '))
while d <= 0 or d > 31:
    print('Dia inválido!')
    print('Selecione um dia entre 01 e 31.')
    d = int(input('Insira um dia: '))

m = int(input('Insira um mês: '))
while m <= 0 or m > 12:
    print('Mês inválido!')
    print('Digite um mês entre 01 e 12.')
    m = int(input('Insira um mês: '))

a = int(input('Insira um ano: '))
while a <= 1000 or a >= 9999:
    print('Ano inválido!')
    print('Insira um ano válido.')
    a = int(input('Insira um ano: '))

if m == 2 and d > 29:
    print(f'>>Esse mês não pode ter {d} dias!<<')
    print('>>Esta é uma data inválida!<<')
if m == 2 and d == 29:
    if a % 4 == 0 and a != 0 or a % 400 == 0:
        print('>>Esta é uma data válida!<<')
    else:
        print('>>Este ano NÃO é bissexto e Fevereiro tem 28 dias!<<')
        print('>>Esta é uma data inválida!<<')
if m == 2 and d <= 28:
    print('>>Esta é uma data válida!<<')
if m == 4 or m == 6 or m == 9 or m == 11:
    if d > 30 :
        print('>>O mês escolhido contém 30 dias!<<')
        print('>>Esta é uma data inválida!<<')
    else:
        print('>>Esta é uma data válida!<<')

if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print('>>Esta é uma data válida!<<')
    