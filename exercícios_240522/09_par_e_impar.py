# 9) Escreva um algoritmo que receba um número e escreva “Par” caso esse número seja par e escreva “Impar” caso esse número seja impar.

num = int(input('Insira um número:'))

resto = num % 2

if(resto == 1):
    print('Impar')
else:
    print('Par')
