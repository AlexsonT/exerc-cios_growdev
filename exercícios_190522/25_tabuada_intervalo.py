# 25) Escreva um programa que receba um número dentro do intervalo de 1 até 9, e exiba a tabuada desse número.

num = int(input('Insira um número inteiro de 1 a 9:'))

if(num > 9):
    print('Insira apenas números entre 1 e 9!')
elif(num < 1):
    print('Insira apenas números entre 1 e 9!')
else:
    print('{} x {:2} = {}'.format(num, 1, num*1))
    print('{} x {:2} = {}'.format(num, 2, num*2))
    print('{} x {:2} = {}'.format(num, 3, num*3))
    print('{} x {:2} = {}'.format(num, 4, num*4))
    print('{} x {:2} = {}'.format(num, 5, num*5))
    print('{} x {:2} = {}'.format(num, 6, num*6))
    print('{} x {:2} = {}'.format(num, 7, num*7))
    print('{} x {:2} = {}'.format(num, 8, num*8))
    print('{} x {:2} x {}'.format(num, 9, num*9))