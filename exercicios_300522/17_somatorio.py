#17) Crie um programa para que retorne o somatório de todos os números entre 1 e um valor fornecido pelo usuário. Por exemplo, se o usuário fornecer o número 4, o computador deverá calcular o somatório 1+ 2 + 3 + 4 = 10.

num = int(input('Insira o número para cálculo: '))
n = 1
soma = 0
while n <= num:
    soma += n
    n += 1
print(soma)