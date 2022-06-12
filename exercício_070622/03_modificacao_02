#3) Modifique o programa anterior para que utilize apenas uma lista e em cada posição da lista armazene um dicionário com o nome e a média.

alunos = []

for i in range(10):
    nome = str(input('Insira o nome do aluno: '))
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))

    media = (nota1 + nota2) / 2

    aluno = {'nome': nome, 'media': media}

    alunos.append(aluno)

for i in range(2):
    aluno = alunos[i]
    if aluno['media'] >= 7:
        print(f'Nome: {aluno["nome"]}\nMedia:{aluno["media"]}')  
