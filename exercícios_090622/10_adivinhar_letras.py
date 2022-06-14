 # 10)Implemente um programa onde o usuário deve adivinhar as letras de uma palavra por meio de palpites. A palavra deve ser mostrada inicialmente com as letras substituídas por underlines, conforme exemplo abaixo.
# dados => _ _ _ _ _
# O usuário deve então palpitar sobre as letras que ele julga estarem na frase.
# A cada letra que errar, ele perde 1 ponto. A cada letra que ele acertar a mesma deve ser exibida na tela, exemplo:
# Palpite: d
# Saída: d _ d _ _
# Se completar a frase o usuário ganha o jogo, se sua pontuação zerar ele perde o jogo. Ao iniciar o jogo, a pontuação é de 4 pontos.

palavra = 'python'.upper()

acertos = erros = 0
letras_acertadas = ''
letras_erradas = ''
chances = 4   

print('*' * 50)

while acertos != len(palavra) and erros != 4:
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += f'{letra}'
        else:
            mensagem += '_ '  
    print(mensagem)    
    print(f'Você já errou: {letras_erradas}')
    print(f'Você ainda tem {chances} chance(s).')
    print()

    letra = input('Insira uma letra: ').upper()
    
    if letra in palavra:
        print('Você acertou uma letra!')
        letras_acertadas += letra
        acertos += 1
    else:
        print('Infelizmente você errou!')
        letras_erradas += letra
        erros += 1 
        chances -= 1   

if acertos == len(palavra):
    print('*' * 50)
    print('PARABÉNS, VOCÊ ACERTOU A PALAVRA!')
    print('*' * 50)
else: 
    print('*' * 50)
    print(':( Infelizmente você perdeu!')
    print('TENTE NOVAMENTE!')
    print('*' * 50)

