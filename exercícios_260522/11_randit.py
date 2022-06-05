#11) Crie um algoritmo para um jogo de adivinhação, onde o usuário tenta adivinhar um número aleatório gerado pelo computador. Esse número aleatório é inteiro e não negativo, e deve ser escolhido dentro de uma faixa estabelecida pelo usuário (por exemplo, o usuário pode estipular que esse número varie entre 0 e 10 ou entre 22 e 48, por exemplo). Após o usuário tentar adivinhar qual foi o número gerado, o algoritmo deve escrever esse número e dizer se indicar se o palpite do jogador estava correto, muito alto ou muito baixo. Dica: Para gerar um número aleatório utilize a função randint do módulo random.

from random import randint
print('='*50)
n1 = int(input('Insira o primeiro número do intervalo a adivinhar: '))
n2 = int(input('Insira o segundo número do intervalo a adivinhar: '))
print('='*50)
computador = randint(n1,n2)
print('Adivinhe o número entre o intervalo informado! Boa sorte!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Tente adivinhar! Diga um número!'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('.'*50)
            print('Chutou baixo! Tente mais uma vez!')
            print('='*50)
        elif jogador >computador:
            print('.'*50)
            print('Chutou alto! Tente mais uma vez!') 
            print('='*50)
print('-*'*25)            
print(f'ACERTOU!!! Parabéns! Utilizou {palpites} tentativa(s)!')
print('-*'*25)               

