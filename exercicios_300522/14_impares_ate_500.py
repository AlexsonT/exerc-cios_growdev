#14) Desenvolver um programa que efetue a soma de todos os números ímpares que se encontram no conjunto dos números de 1 até 500.

soma = 0
for i in range(1, 500, 2):
    if i < 500:
        soma += i
print(soma)    