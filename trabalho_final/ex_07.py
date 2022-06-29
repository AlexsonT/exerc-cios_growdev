# 7) Qual dos anos (1º, 2º ou 3º) mais procura a monitoria?. Crie um gráfico para mostrar esses dados.

import csv
import matplotlib.pyplot as plt

with open('alunos.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)

    next(csv_reader)

    ment_01 = ment_02 = ment_03 = 0

    for line in csv_reader:
        line[1] = int(line[1])

        if line[1] == 1 and line[7] == 'True':
            ment_01 += 1
        if line[1] == 2 and line[7] == 'True':
            ment_02 += 1
        if line[1] == 3 and line[7] == 'True':
            ment_03 += 1

print(ment_01, ment_02, ment_03)
