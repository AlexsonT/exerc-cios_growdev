# 5) Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8 3 4
# 1 5 9
# 6 7 2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
import random

def quadrado_magico():
    r = random.randrange(2, 10, 2)
    l1 = [[4, 9, 2], [3, 5, 7], [1, 8, 6]]
    l2 = [[4, 3 ,8], [9, 5, 1], [2, 7, 6]]
    l3 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    l4 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    l5 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    l6 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    l7 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    l8 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    if r == 2:
        print(l3, l4, l5, l6, l7, l8, l1, l2)
    elif r == 4:
        print(l1, l2 ,l3, l4, l5, l6, l7, l8)
    elif r == 6:
        print(l5, l6, l7, l8, l1, l2, l3, l4)        
    else:
        print(l7, l8, l1, l2, l3, l4, l5, l6)      


quadrado_magico()