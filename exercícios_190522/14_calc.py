# 14) Escreva um programa que leia dois números e faça a adição, subtração, divisão e multiplicação dos dois números, e após, exiba os 4 resultados calculados.
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print((f'O resultado da sua adição é: {adicao}'))
print(f'O resultado da sua subtração é: {subtracao}')
print(f'O resultado da sua multiplicação é: {multiplicacao}')
print((f'O resultado da sua divisão é: {divisao}'))
