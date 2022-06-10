# 1) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

inverso = []

for i in range(10):
    numero = int(input('Insira um número: '))
    inverso.append(numero)
inverso.reverse()
print(inverso)    