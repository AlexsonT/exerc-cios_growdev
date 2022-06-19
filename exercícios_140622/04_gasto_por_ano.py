#4) Qual foi o gasto por ano?

import csv

with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    datas = []
    soma = []

    for line in csv_reader:
        line[5] = int(line[5])
        line[4] = int(line[4])
        
        if line[5] not in datas:
            datas.append(line[5])
            soma.append([line[5], line[4]])
        else:
            for i in soma:
                if i[0] == line[5]:
                    i[1] += line[4]
soma.sort()
           
for i in soma:
    print(f'No ano {i[0]} foi gasto o total de {i[1]} ') 