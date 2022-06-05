#4) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
#a) média do salário da população;
#b) média do número de filhos;
#c) maior salário;
#d) percentual de pessoas com salário até R$2000,00.
#Escreva um programa que receba as informações necessárias de 5 pessoas conforme a descrição e responda às questões a, b, c e d anteriores.


somab = somaa = quant = maior = men2m = 0
for var in range(5):
    a = float(input('Insira o salário: '))
    b = int(input('Quantos filhos tem?:'))
    somaa = somaa + a
    somab = somab + b
    quant += 1
    if a > maior:
        maior = a
    if a < 2000:
        men2m += 1

print('=*'*40)
print('                   >>>RELATÓRIO DA AMOSTRA POPULACIONAL<<<')
print('=*'*40)
print(f'A média salarial da amostra é : R$ {somaa/quant: .2f}.')
print(f'A média da quantidade de filhos é de: {somab/quant: .2f} filhos. ')
print(f'O maior salário coletado foi de: R$ {maior: .2f}')
print(f'O percentual de pessoas com salário menor que R$ 2.000,00 é de : {men2m/quant: .2f}%.')
print('=*'*40)