# 20) Escreva um programa que leia um valor inicial A e uma razão R e imprima uma sequência em P.G. contendo 10 valores.

termo = int(input('Insira o primeiro valor: '))
razao = int(input('Insira a razão: '))
decimo = termo + (10 - 1) * razao
pg = 1
for i in range(termo, decimo + razao, razao):
    pg = pg * razao
    print(pg)
