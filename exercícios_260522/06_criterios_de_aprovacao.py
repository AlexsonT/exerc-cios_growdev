# 6) Numa determinada escola, os critérios de aprovação são os seguintes:
# a) O aluno deve ter, no máximo, 25% de faltas;
# b) A nota final deve ser igual ou superior a 7,00.
# Construa um algoritmo para ler as notas que um aluno tirou nos 4 bimestres, o número total de aulas e o número de faltas, mostrando ao final a situação do aluno como sendo “Aprovado”, “Reprovado por Faltas” e “Reprovado por média”, considerando que a reprovação por faltas se sobrepõe a reprovação por nota.

print('*'*50)
print('Insira as informações do primeiro bimestre:')
print('*'*50)
print('PRIMEIRO BIMESTRE')
nota11b = float(input('Insira a primeira nota: '))
nota21b = float(input('Insira a segunda nota: '))
aulas1b = int(input('Insira o total de aulas lecionadas: '))
falta1b = int(input('Insira o total de faltas: '))
print('*'*50)
print('Insira as informações do segundo bimestre:')
print('*'*50)
print('SEGUNDO BIMESTRE')
nota12b = float(input('Insira a primeira nota: '))
nota22b = float(input('Insira a segunda nota: '))
aulas2b = int(input('Insira o total de aulas lecionadas: '))
falta2b = int(input('Insira o total de faltas: '))
print('*'*50)
print('Insira as informações do terceiro bimestre:')
print('*'*50)
print('TERCEIRO BIMESTRE')
nota13b = float(input('Insira a primeira nota: '))
nota23b = float(input('Insira a segunda nota: '))
aulas3b = int(input('Insira o total de aulas lecionadas: '))
falta3b = int(input('Insira o total de faltas: '))
print('*'*50)
print('Insira as informações do quarto bimestre:')
print('*'*50)
print('QUARTO BIMESTRE')
nota14b = float(input('Insira a primeira nota: '))
nota24b = float(input('Insira a segunda nota: '))
aulas4b = int(input('Insira o total de aulas lecionadas: '))
falta4b = int(input('Insira o total de faltas: '))
print('*'*50)

media = ((nota11b + nota21b + nota12b + nota22b + nota13b + nota23b + nota14b + nota24b) / 8)
print(f'A sua média ficou em: {media}.')
faltas = (((falta1b + falta2b + falta3b + falta4b) / (aulas1b + aulas2b + aulas3b + aulas4b) * 100))
print(f'Você atingiu um total de {faltas}% de faltas.')
print('*'*10)
if(media >= 7):
    print('O(a) aluno(a) está APROVADO por média.')
else:
    print('O(a) aluno(a) está REPROVADO por média.')
if(faltas < 25):
    print('O(a) aluno(a) está APROVADO por frequência.')
else:
    print('O(a) aluno(a) está REPROVADO por frequência.')
print('*'*10)
if(faltas > 25):
    print('Aluno(a) foi REPROVADO no conceito geral!')
elif(faltas < 25 and media >= 7):
    print('Aluno(a) foi APROVADO no conceito geral!')
else:
    print('O aluno teve presenças suficientes, mas reprovou no conceito geral!')
print('*'*10)
