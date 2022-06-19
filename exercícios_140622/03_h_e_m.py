#3) Qual a porcentagem de homens e mulheres na base de dados?

import csv

with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    m = f = 0
    for line in csv_reader:
        if line[3] == 'M':
            m += 1
            
        elif line[3] == 'F':
            f += 1
             
total = m + f
print('*'*50)
print(f'Total de cadastros masculinos: {m} equivalente a {(m / total) * 100}%')
print(f'Total de cadastros femininos: {f} equivalente a {(f / total) * 100}%')
print('*'*50)