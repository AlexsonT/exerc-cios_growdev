# 3) Quantos alunos do 3º ano reprovaram? e desses quantos procuraram monitoria?


import csv  # importando o arquivo csv.

with open('alunos.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)
    
    next(csv_reader)

    reprovaram = 0
    mentoria = 0

    for line in csv_reader:
        line[1] = int(line[1]) 
        line[6] = float(line[6])
        # line[7] = bool(line[7]) 
        if line[1] == 3:
            if line[6] > 0.0 and line[6] <= 5.0:
                reprovaram += 1 
                if line[7] == 'True':
                    mentoria += 1       
               
print(reprovaram)  
print(mentoria)