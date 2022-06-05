# 16) Faça um programa que receba o cateto oposto e o cateto adjacente de um triângulo e retorne a hipotenusa do mesmo.
cat01 = float(input('Informe o valor do primeiro cateto: '))
cat02 = float(input('Informe o valor do segundo cateto:'))

hipotenusa = cat01 ** 2 + cat02 ** 2

print(f' A valor da hipotenusa correspondente aos catetos é: {hipotenusa}')