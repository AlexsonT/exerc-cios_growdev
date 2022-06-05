#2) Faça um algoritmo que receba um valor negativo e retorne o seu valor absoluto (ex: recebe -5 e retorna 5).

num = float(input('Insira um número: '))

if(num < 0):
    print(f'O valor absoluto do seu número é: {num*-1}')
else:
    print(f'O valor absoluto do seu número é: {num}')
