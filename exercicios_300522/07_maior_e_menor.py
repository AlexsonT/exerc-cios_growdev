#7) Escreva um programa que leia 10 valores e encontre o maior e o menor deles. Mostre o resultado.

maior = menor = 0
for n in range(1,10):
    num = int(input('Insira um número: '))
    if n == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('*'*50)            
print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')  
print('*'*50)                  