# 1) Escreva um algoritmo que receba dois números, exiba as opções:
# a) 1 - adição
# b) 2 - subtração
# Então peça ao usuário para escolher uma das opções. Caso escolha a opção
# 1 o algoritmo deve realizar a soma dos dois números lidos e exibir. Caso escolha a opção 2 o algoritmo deve realizar a subtração dos dois números lidos e exibir.
from time import sleep

num01 = float(input('Insira o primeiro número da operação:'))
num02 = float(input('Insira o segundo número da operação:'))
opcao = 0
while opcao != 3:
    print('''    [1] ADIÇÃO
    [2] SUBTRAÇÃO
    [3] SAIR DO PROGRAMA''')
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
        print(f'O resultado de sua adição é: {num01+num02}')
    elif opcao == 2:
        print(f'O resultado de sua subtração é: {num01*num02}')
    elif opcao == 3:
        print('Finalizando...')
    else:
        print('Escolha uma das opções disponíveis!')
    print('-'*50)
    sleep(1.5)
print('Fim do programa!')
