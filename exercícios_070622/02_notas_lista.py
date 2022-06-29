# 2) Faça um programa que peça o nome e as duas notas de 5 alunos, calcule a média das notas e armazene nome e média cada uma em uma lista, ao final imprima o nome e o número de alunos com média maior ou igual a 7.0.

nomes = []
medias = []

for i in range(5):
    nome = str(input('Insira o nome do aluno: '))
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))

    media = (nota1 + nota2) / 2

    nomes.append(nome)
    medias.append(media)

for i in range(5):
    if medias[i] >= 7:
        print(f'Nome: {nomes[i]}\nMedia:{medias[i]}')  
        
print(nomes)
print(medias)