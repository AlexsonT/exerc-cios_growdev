# 2) Quantos alunos do 1º ano foram aprovados sem exame?

import csv  # importando o arquivo csv.

with open('alunos.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)
    
    next(csv_reader)

    repeticoes = 0

    for line in csv_reader:
        line[1] = int(line[1]) 
        line[6] = float(line[6]) 
        if line[1] == 1 and line[6] == 0.0:
            repeticoes += 1    
print('*'*50)           
print(f'Tivemos {repeticoes} alunos do 1º ano aprovados sem exame.')
print('*'*50)  