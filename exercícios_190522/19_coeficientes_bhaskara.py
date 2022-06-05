# 19)Faça um programa que receba os coeficientes a, b e c da equação a seguir, e encontre as raízes por meio da fórmula de bhaskara. ax²+bx+c
import math

a = int(input('Digite o valor correspondente de A: '))
b = int(input('Digite o valor correspondente de B: '))
c = int(input('Digite o valor correspondente de C: '))

delta = b**2 - 4*a*c

if(delta < 0):
    print('Não tem raízes reais.')
elif(delta == 0):
    x = -b / (2*a)
    print(f'Temos duas raízes reais e iguais no valor de {x}.')
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print('Temos duas raízes reais e diferentes')
    print(f'x1 = {x1}')
    print(f'X2 = {x2}')