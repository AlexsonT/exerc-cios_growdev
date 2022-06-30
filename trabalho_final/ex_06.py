# 6) As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?. Crie um gráfico para mostrar isso.

import csv
import matplotlib.pyplot as plt

with open('alunos.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)

    next(csv_reader)
    
    rep01 = rep02 = rep03 = 0
   
    for line in csv_reader:
        line[1] = int(line[1])
        line[5] = int(line[5])
        line[6] = float(line[6])

        if line[5] > 15 or line[6] > 0 and line[6] <= 5:
            if line[1] == 1:
                rep01 += 1
            if line[1] == 2: 
                rep02 += 1
            if line[1] == 3: 
                rep03 += 1      

labels = 'Alunos do\n1º ano.', 'Alunos do\n2º ano.', 'Alunos do\n3º ano.'
sizes = [rep01, rep02, rep03]
explode = (0, 0.1, 0)
figl, axl = plt.subplots(figsize=(8, 8))
c = ['#4169E1', '#00BFFF', '#1E90FF']
axl.pie(sizes, explode = explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=75, colors = c)
axl.set_title('% DE REPROVAÇÕES NO PERÍODO', size=14, weight='bold')
axl.axis('equal')
plt.show()  