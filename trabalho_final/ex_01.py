# 1) Quantos alunos estudam em cada escola, e qual a escola com mais alunos?

import csv  # importando o arquivo csv.

with open('alunos.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)
    
    next(csv_reader)

    repeticoes = []
    escola = []

    for line in csv_reader:    
        if line[2] not in escola:
            repeticoes.append([1, line[2]])
            escola.append(line[2])
        else:    
            for i in repeticoes:
                if i[1] == line[2]:
                    i[0] += 1 
print('*'*76)
for e in repeticoes:
    repeticoes.sort()
    print(f'A escola {e[1]} tem {e[0]} alunos.')    
print('*'*76)

print(f'A escola {e[1]} tem o maior número de alunos com {e[0]} matrículados.')             
print('*'*76) 

