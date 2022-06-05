# 23) Faça um programa que receba um valor no intervalo entre 0 e 1000, e converta para o valor correspondente ao intervalo -1 e 1.

val = int(input('Insira um valor entre 0 e 1000:'))

if(val < 0):
    print('O valor deve ficar entre 0 e 1000')
elif(val > 1000):
    print('O valor deve ficar entre 0 e 1000')
else:
    print(f'O valor retornado é: {(val/500)-1}')