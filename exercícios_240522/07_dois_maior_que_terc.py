# 7) Escreva um algoritmo que receba 3 números, faça a soma dos dois primeiros e verifique se o resultado da soma é maior que o terceiro número lido.

num1 = float(input('Insira o seu primeiro número: '))
num2 = float(input('Insira o seu segundo número: '))
num3 = float(input('Insira o seu terceiro número: '))

if(num1 + num2 > num3):
    print('A soma dos dois primeiros números é maior que o terceiro!')
else:
    print('A somados dois primeiros números não é maior que o terceiro número!')
