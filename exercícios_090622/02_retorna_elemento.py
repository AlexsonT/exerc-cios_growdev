# 2) Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def pn(n):
    if n > 0:
        print('Positivo = P')
    elif n == 0:
        print('Nulo = N')
    else:
        print('Negativo = N')

print('POSITIVO OU NEGATIVO')
n = int(input('digite um número: '))
print('Este número é', end=' ')
pn(n)