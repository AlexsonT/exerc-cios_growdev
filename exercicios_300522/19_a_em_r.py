# 19) Escreva um programa que leia um valor inicial A e uma razão R e imprima uma sequência em P.A. contendo 10 valores.

termo = int(input('Insira o valor inicial: '))
razao = int(input('Insira o valor da progressão: '))
decimo = termo + (10 - 1) * razao
pa = 0
for i in range(termo, decimo + razao, razao):
    pa += razao
    print(pa)
