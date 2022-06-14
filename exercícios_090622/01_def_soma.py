#1) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

# Definindo a função
def soma(num1, num2, num3):
    s = num1 + num2 + num3
    return s

# Atribuindo valores
num1 = int(input('Insira um número para soma:'))
num2 = int(input('Insira um número para soma:'))
num3 = int(input('Insira um número para soma:'))   

# Imprime resultado na tela
print('='*30)
print(f'O resultado da soma é: {soma(num1, num2, num3)}')
print('='*30)