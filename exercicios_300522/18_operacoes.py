#18) Desenvolver um programa que leia um número não determinado de valores e calcule e escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos.

num = int(input('Insira um número para calcular a média: '))
cont = 1
operacao = 0
soma = num
while operacao < 2:
    num = int(input('Insira um número para calcular a média: '))
    print('[1]DIGITAR VALOR \n[2...]CALCULAR')
    operacao = int(input('O que deseja fazer? '))
    print('*'*50)
    cont += 1
    soma += num 

print(soma)
print(cont)






