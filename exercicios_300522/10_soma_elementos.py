#10)Escreva um programa que recebe 10 valores e imprima o somatório dos elementos.

soma = 0
for i in range(10):
    num = int(input('Insira um número: '))
    soma += num
print('='*50)
print(f'A soma dos valores digitados é: {soma}')
print('*'*50)
