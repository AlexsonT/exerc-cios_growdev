# 9) Modifique o programa anterior para exibir as seguintes estatísticas.
# a) Acertos em água
# b) Acertos em Navios
# c) Porcentagem de acertos em água
# d) Porcentagem de acertos em Navios
# e) Acertos ininterruptos (maior quantidade de acertos em sequência)
from random import randint

acertos_em_sequencia = 0
seguidos = 1
acertos = 0

l = [[0 for j in range(20)]for i in range(20)]    

tabuleiro = [[0] * 20] * 20

for linha in range(20):
    coluna = randint(0,19)
    tabuleiro[linha][coluna] = 1

tentativas = 0
acertos = 0

while tentativas <= 3 or acertos < 2:
    linha = int(input('Informe a linha: '))
    coluna = int(input('Informe a coluna: '))
    
    if tabuleiro[linha][coluna] == 1:
        print('Você acertou um navio!')
        tabuleiro[linha][coluna] = 0
        acertos += 1

        if seguidos > 0: 
            if  acertos_em_sequencia <= seguidos:
                acertos_em_sequencia = seguidos
        seguidos += 1

    else:
        print('Infelizmente você errou!')
        tentativas +=1
        seguidos = 0

if acertos == 2:
    print('Parabéns, você ganhou!!!')
else:
    print('Continue tentando!')  

print('*'*50)
print(f'Você acertou {tentativas} vezes na água!')
print(f'O que equivale a: {tentativas / (tentativas + acertos)*100: .2f} %')
print(f'Você acertou {acertos} vezes em navios!')
print(f'O que equivale a: {acertos / (tentativas + acertos)*100: .2f} %')
print(f'Você acumulou o máximo de {acertos_em_sequencia} acertos em sequência!')
print('*'*50)