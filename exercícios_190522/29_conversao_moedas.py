# 29) Crie um algoritmo que calcule e exiba a conversão de uma determinada quantidade em reais em moedas de R$1.00, R$0.50, R$0.25, R$0.10, R$0.05 e R$0.01. Por exemplo, R$3.78 resulta em três moedas de um real, uma de cinquenta centavos, duas de dez centavos, uma de 5 centavos e três de um centavo.


reais = float(input('Informe a quantidade em reais: '))

moedas_1 = reais - reais % 1

reais -= moedas_1

moedas_50 = reais / 0.5
moedas_50 -= moedas_50 % 1
reais -= moedas_50 * 0.5

moedas_25 = reais / 0.25
moedas_25 -= moedas_25 % 1
reais -= moedas_25 * 0.25

moedas_10 = reais / 0.1
moedas_10 -= moedas_10 % 1
reais -= moedas_10 * 0.1

moedas_05 = reais / 0.05
moedas_05 -= moedas_05 % 1
reais -= moedas_05 * 0.05

print(reais)

moedas_01 = reais / 0.01
moedas_01 -= moedas_01 % 1
reais -= moedas_01 * 0.01

print(f'Moedas 1: {moedas_1}.')
print(f'Moedas 50: {moedas_50}.')
print(f'Moedas 25: {moedas_25}.')
print(f'Moedas 10: {moedas_10}.')
print(f'Moedas 5: {moedas_05}.')
print(f'Moedas 1: {moedas_01}.')
