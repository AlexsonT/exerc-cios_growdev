#12) Qual o valor gasto em compras por jovens do ano de 2010 até 2015?

import csv

with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    # Jovens = 18 a 25 anos

    soma = []

    for line in csv_reader:
        line[2] = int(line[2])
        line[4] = int(line[4])
        line[5] = int(line[5])
        
        if line[2] >= 18 and line[2] < 26:
            if line[5] >= 2010 and line[5] <= 2015:
                soma.append(line[4])
               

print('*'*55)
print(f'O valor gasto por jovens no período foi de ${sum(soma): .2f}.')
print('*'*55)