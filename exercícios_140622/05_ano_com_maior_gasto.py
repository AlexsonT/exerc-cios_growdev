# 5) Qual foi o ano com maior gasto?

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
            soma.append([line[4], line[5]])
        else:
            for i in soma:
                if i[1] == line[5]:
                    i[0] += line[4]

print(max(soma))