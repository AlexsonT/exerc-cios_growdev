# 4) O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros comprados a cada mês. Os pontos são atribuídos da seguinte forma:
# a) Se um cliente comprar 0 livros, ele ganhará 0 pontos.
# b) Se um cliente comprar um livro, ele ganhará 5 pontos.
# c) Se um cliente comprar dois livros, ele ganhará 15 pontos.
# d) Se um cliente comprar 3 livros, ele ganhará 30 pontos.
# e) Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
# Crie um algoritmo que leia o número de livros comprados por um cliente e exiba o número de pontos correspondentes.

comprados = int(input('Insira a quantidade de livros comprados: '))

if(comprados == 0):
    print('Infelizmente você ganhou "0" pontos!')
elif(comprados == 1):
    print('Você ganhou "05" pontos para concorrer ao nosso sorteio!')
elif(comprados == 2):
    print('Você ganhou "15" pontos para concorrer ao nosso sorteio!')
elif(comprados == 3):
    print('Você ganhou "30" pontos para concorrer ao nosso sorteio!')
else:
    print('Você ganhou "60" pontos para concorrer ao nosso sorteio!')
