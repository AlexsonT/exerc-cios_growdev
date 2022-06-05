# 11) Sabendo que o lucro anual de uma empresa é, tipicamente, 23% do total de vendas, crie um programa que solicite ao usuário que entre com o valor projetado do total de vendas e, em seguida, calcule e exiba o lucro que deve ser obtido com esse valor.
fat = int(input('Insira o valor do faturamento bruto projetetado para o ano: '))


margem = fat*.23
print(f'A estimativa do lucro anual é de: {margem}')

# 12) Escreva um programa que receba a idade de 3 pessoas, e calcule o somatório dessas idades.
idade01 = int(input('Informe sua idade '))
idade02 = int(input('Informe sua idade '))
idade03 = int(input('Informe sua idade '))


soma = idade01 + idade02 + idade03
print(f'A soma total de suas idade é {soma} anos.')