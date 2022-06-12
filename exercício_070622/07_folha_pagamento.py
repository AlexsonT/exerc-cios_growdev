# #7) Crie um programa que calcule a folha de pagamento de uma empresa, conforme as instruções a seguir:

# a) O usuário pode inserir continuamente os nomes dos empregados até que escolha a opção de finalizar o informe de dados;
# b) Após informar o nome de cada empregado, o usuário deverá informar o valor do salário da hora trabalhada desse empregado e quantas horas ele trabalhou;
# c) O programa deve calcular o salário bruto de cada empregado, a percentagem de imposto retido na fonte (com base na tabela abaixo), o valor do imposto retido na fonte e o salário líquido (pagamento bruto menos imposto retido na fonte);
# d) Depois que o usuário inserir os dados do último empregado, o programa deve exibir o salário bruto, salário líquido, percentual de imposto e valor do imposto para cada funcionário;
# e) Por último, o programa deve exibir a soma de todas as horas trabalhadas, o total da folha de pagamento bruta, o total de imposto e a folha de pagamento líquida total.

# Percentuais de imposto
# Salário bruto Percentual
# Até R$ 2.999,99 10%
# Entre R$ 3.000,00 e R$ 5.499,99 13%
# Entre R$ 5.500,00 e R$ 7.999,99 16%
# Acima de R$ 8.000,00 20%

opcao = 0
bruto = []
liquido = []
irrf = []
val_irrf = []
total_trabalhado = []

while opcao != 2:
    print('Selecione sua opção conforme abaixo:')
    print('[1]Informar dados\n[2]Finalizar o informe de dados')
    opcao = int(input('Informe sua opção:'))

    if opcao == 2:
        break

    print('='*50)
    nome = str(input('Informe o nome do colaborador: '))
    valor_hora = float(input('Informe o valor hora: '))
    tot_trabalhado = float(input('Horas trabalhadas no período: '))
    salario_bruto = (valor_hora * tot_trabalhado)
    print(f'Salário bruto: {salario_bruto}')
    if salario_bruto < 3000:
        print('"%" do IFFR: 10%')
        ir = '10%'
        imposto = (salario_bruto * .1)
        salario_liquido = (salario_bruto * .9)
    elif salario_bruto >= 3000 and salario_bruto < 5500:    
        print('"%" do IFFR: 13%')
        ir = '13%'
        imposto = (salario_bruto * .13)
        salario_liquido = (salario_bruto * .87)
    elif salario_bruto >= 5500 and salario_bruto < 8000:
        print('"%" do IFFR: 16%')
        ir = '16%'
        imposto = (salario_bruto * .16)    
        salario_liquido = (salario_bruto * .84)
    else:
        print('"%" do IFFR: 20%')
        ir = '20%'
        imposto = (salario_bruto * .2)    
        salario_liquido = (salario_bruto * .8)
    print('='*50)
    bruto.append(salario_bruto)
    liquido.append(salario_liquido)
    irrf.append(ir)
    val_irrf.append(imposto)
    total_trabalhado.append(tot_trabalhado)
print('*'*50)    
print(bruto)
print(liquido)
print(irrf)
print(val_irrf)
print('*'*50)
print('='*50)
print('RESUMO FOLHA DE PAGAMENTO')
print('='*50)
print('TOTAL DE HORAS TRABALHADAS:')
print(sum(total_trabalhado))
print('TOTAL DO SALÁRIO BRUTO:')
print(sum(bruto))
print('TOTAL DO IMPOSTO:')
print(sum(val_irrf))
print('TOTAL DO SALÁRIO LÍQUIDO:')
print(sum(liquido))
print('='*50)