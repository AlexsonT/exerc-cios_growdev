# 4) De todos os alunos que reprovaram quantos foram por falta e quantos foram por nota, e quantos foram por ambas as causas?


import csv  # importando o arquivo csv.

with open('alunos.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)
    
    next(csv_reader)

    nota = 0
    falta = 0
    ambas = 0

    for line in csv_reader:
        line[5] = int(line[5]) 
        line[6] = float(line[6])
        
        if line[5] > 15:
            falta += 1
        if line[5] <= 15:
            if line[6] > 0 and line[6] <= 5:
                nota += 1 
        if line[5] > 15:
            if line[6] > 0 and line[6] <= 5:
                ambas += 1             
print('*'*50)
print(f'Tivemos {falta} alunos reprovados por falta.')
print(f'Tivemos {nota} alunos reprovados por nota.')
print('.'*50)
print(f'Tivemos {ambas} reprovados em ambos os critérios.')
print('*'*50)