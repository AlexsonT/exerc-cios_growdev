# 5) Escreva um algoritmo que leia três números fornecidos pelo usuário e mostre se a soma de dois deles resulta no terceiro.

num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))
num3 = float(input('Insira o terceiro número: '))

if(num1+num2 == num3):
    print('A soma de dois números resulta em um terceiro!')
elif(num2+num3 == num1):
    print('A soma de dois números resulta em um terceiro!')
elif(num1+num3 == num2):
    print('A soma de dois números resulta em um terceiro!')
else:
    print('A soma de dois números NÃO resulta em um terceiro!')
