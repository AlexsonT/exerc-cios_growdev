# 8) Escreva um programa que leia a idade e salário de 10 pessoas. Informe em seguida:
# a) Qual é a média de idade entre as pessoas?
# b) Quantas pessoas há por faixa etária, considerando:
# i) jovens < 18
# ii) 18 <= adultos < 60
# iii) idosos >= 60
# c) Em seguida, mostre qual é a faixa etária que acumula o maior salário.

soma1 = soma2 = soma3 = maior = somai = faixa1 = faixa2 = faixa3 = i = 0
for i in range(5):
    salario = float(input('Informe um salário: '))
    idade = int(input('Informe uma idade: '))
    if idade < 18:
        faixa1 = i + 1
        somai += idade
        soma1 += salario
    elif idade >= 60:
        faixa3 = i + 1
        somai += idade
        soma3 += salario
    else:
        faixa2 = i + 1
        somai += idade
        soma2 += salario

print('*'*50)
print(f'A média das idades cadastradas foi de: {somai/(i+1)} anos.')
print(f'Foram cadastradas {faixa1} pessoas menores de 18 anos.')
print(f'Foram cadastradas {faixa2} pessoas entre 18 e 59 anos.')
print(f'Foram cadastradas {faixa3} pessoas acima de 59 anos.')

if soma1 > soma2 and soma1 > soma3:
    print('Jovens com menos de 18 anos acumulam a maior soma de salários! ')
elif soma3 > soma1 and soma3 > soma2:
    print('Idosos com idade igual ou maior a 60 anos acumulam a maior soma de salários! ')
else:
    print('Adualtos entre 18 e 59 anos acumulam a maior soma de salários!')
print('*'*50)