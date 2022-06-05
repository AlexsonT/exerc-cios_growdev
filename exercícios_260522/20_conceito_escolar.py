#20) Faça um programa que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento
#Entre 9.0 e 10.0  A
#Entre 7.5 e 8.9 B
#Entre 6.0 e 7.4 C
#Entre 4.0 e 5.9 D
#Entre 0 e 3.9 E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem:
#a) APROVADO se o conceito for A, B ou C.
#b) REPROVADO se o conceito for D ou E.

n1 = float(input('Insira a primeira nota do aluno:'))
n2 = float(input('Insira a segunda nota do aluno:'))
media = ((n1 + n2) / 2)

if media >= 0 and media < 4:
    print(f'Sua média ficou em: {media}')
    print('Seu conceito é: "E"')
if media >= 4 and media < 6:    
    print(f'Sua média ficou em: {media}')
    print('Seu conceito é: "D"')
    print('Você está REPROVADO!')
if media >= 6 and media < 7.5:
    print(f'Sua média ficou em: {media}')
    print('Seu conceito é: "C"')
    print('Você está APROVADO!')
if media >= 7.5 and media < 9:
    print(f'Sua média ficou em: {media}')
    print('Seu conceito é: "B"')
    print('Você está APROVADO!')
if media >= 9:
    print(f'Sua média ficou em: {media}')
    print('Seu conceito é: "A"')
    print('Você está APROVADO!')