# 9) Qual o sobrenome que mais aparece na base de dados?

import csv

with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    sobrenomes = []
    repeticoes = []
    
    for line in csv_reader:
        if line[1] not in sobrenomes:
            repeticoes.append([1, line[1]])
            sobrenomes.append(line[1])
        else:
            for i in repeticoes:
                if i[1] == line[1]:
                    i[0] += 1    
           

print(max(repeticoes))            

