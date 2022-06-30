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


labels = 'Alunos do\n1º ano.', 'Alunos do\n2º ano.', 'Alunos do\n3º ano.'
sizes = [ment_01, ment_02, ment_03]
explode = (0, 0.1, 0)
figl, axl = plt.subplots(figsize=(8, 8))
c = ['#FFA500', '#FF4500', '#FF8C00']
axl.pie(sizes, explode = explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=75, colors = c)
axl.set_title('Índice de utilização da mentoria', size=14, weight='bold')
axl.axis('equal')
plt.show()  
