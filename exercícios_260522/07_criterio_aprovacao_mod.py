#7) Após construir o algoritmo anterior, crie mais duas versões dele para prever as seguintes situações:
#a) Um aluno pode ficar em recuperação se possuir frequência suficiente (superior a 75%) e média superior a 5 mas inferior a 7;
#b) Caso um aluno reprove por média e faltas, sua situação deve ser “Reprovado por Média e Faltas” (ao invés de simplesmente “Reprovado por Faltas” como antes).

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
print(f'A sua média ficou em: {media: .2f}.')
faltas = (((falta1b + falta2b + falta3b + falta4b) / (aulas1b + aulas2b + aulas3b + aulas4b) * 100))
print(f'Você atingiu um total de {faltas: .2f}% de faltas.')
print('*'*50)

if(media >= 7 and faltas <=25):
    print('O(a) aluno(a) está APROVADO por média e frequência.')
elif(media > 5 and faltas <=25):
    print('O(a) aluno(a) está em RECUPERAÇÃO por média.')
    print('Insira a nova media do aluno!')
    nova_media = float(input('A nova média é: '))
    if(nova_media >= 7):
        print('Aluno em recuperação agora está APROVADO!')
    else:
        print('O aluno não atingiu média suficiente para aprovação!')
        print('ALUNO REPROVADO!')    
elif(media <7 and faltas >25): 
    print('O(a) aluno(a) está REPROVADO por média e faltas.')
else:
    print('Aluno REPROVADO por faltas!')   
print('*'*50)     