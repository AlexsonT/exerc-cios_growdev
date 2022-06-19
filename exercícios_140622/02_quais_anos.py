#2) Busque qual são os anos da base de dados?

import csv

with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    datas = []
 
    for line in csv_reader:
        if line[5] not in datas:
            datas.append(line[5])
            datas.sort()
           
print(datas)       