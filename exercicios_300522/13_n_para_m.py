#13)Faça um programa que leia um valor N e mostre os N termos da Série a seguir:
#a) S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m

n = int(input('Insira um valor:'))

dividendo = 1
divisor = 1
operacao = 0
while dividendo < n:
    operacao = dividendo / divisor
    print(f'{divisor}/{dividendo}')
    dividendo += 2
    divisor += 1
print(f'O resultado da operação é: {operacao: .2f}')    
