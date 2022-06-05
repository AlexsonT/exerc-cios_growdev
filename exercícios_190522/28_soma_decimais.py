# 28) Escreva um programa que receba 3 valores e some as partes decimais de todos eles. Ex: 5.6, 2.3, 8.0, resultado deve ser 0.9.

n1 = float(input("Informe o primeiro número: "))

n2 = float(input("Informe o segundo número: "))

n3 = float(input("Informe o terceiro número: "))

frac_1 = n1 % 1
frac_2 = n2 % 1
frac_3 = n3 % 1

soma = frac_1 + frac_2 + frac_3

print(f'Soma: {soma}.')
