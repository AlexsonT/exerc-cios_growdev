# 10) Qual foi o ano em que os homens mais usaram o crédito?

import csv

with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    repeticoes = []
    ano = []
    
    for line in csv_reader:
        if line[3] == 'M' and line[6] == 'credito':    
            if line[5] not in ano:
                repeticoes.append([1, line[5]])
                ano.append(line[5])
            else:
                for i in repeticoes:
                    if i[1] == line[5]:
                        i[0] += 1    
           

print(max(repeticoes))   