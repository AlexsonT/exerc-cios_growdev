# 4) Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa.

l = 0

def retangulo():
    linhas = int(input('Informe o tamanho da linha de 1 a 20 caracteres: '))
    if linhas < 1:
        print('O valor informado está abaixo do solicitado e assumira o valor >> 01 <<')
        linhas = 1
    elif linhas > 20:
        print('O valor informado está acima do solicitado e assumira o valor >> 20 <<')
        linhas = 20
    
    colunas = int(input('Informe a altura da coluna de 1 a 20 caracteres: '))
    if colunas < 1:
        print('O valor informado está abaixo do solicitado e assumira o valor >> 01 <<')
        colunas = 1
    elif colunas > 20:
        print('O valor informado está acima do solicitado e assumira o valor >> 20 <<')
        colunas = 20
    
    while l < linhas:
        print('+' + ('-' * (linhas - 2)) + '+')
        for i in range(colunas - 2):
            print('|' + (' ' * (linhas - 2)) + '|')
        print('+' + ('-' * (linhas - 2)) + '+')    
        break
    
retangulo()    