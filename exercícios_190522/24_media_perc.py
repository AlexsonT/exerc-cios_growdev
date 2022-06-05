# 24) Escreva um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 20%, 30% e 50%, respectivamente.

n1 = float(input('Sua primeira nota foi: '))
n2 = float(input('Sua segunda nota foi: '))
n3 = float(input('Sua terceira nota foi: '))

media = (n1*.2) + (n2*.3) + (n3*.5)

print(f'Sua média final é: {media: .2f}.')
