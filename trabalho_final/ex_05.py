# 5) Qual a média de todas as notas (do 1º e 2º semestre) dos alunos do 2º ano?

import csv  # importando o arquivo csv.

with open('alunos.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)
    
    next(csv_reader)

    notas = []
  
    for line in csv_reader:
        line[1] = int(line[1])
        line[3] = float(line[3]) 
        line[4] = float(line[4])
        
        if line[1] == 2 :
            notas.append((line[3] + line[4]) / 2)
  

mean = (sum(notas) / len(notas))

print('*'*60)
print(f'A média das notas dos alunos do 2º ano ficou em: {mean: .2f}.')
print('*'*60)