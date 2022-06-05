#1) Escrever um programa que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta  informação.
a = 0
for var in range(5):
    print('.'*60)
    num = int(input('Digite um valor: '))
    if num < 0:
        a += 1

print('*'*60)
print(f'A qauntidade de números negativos na amostra é de : {a}')      
print('*'*60)