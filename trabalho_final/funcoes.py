def tratamento():

    import csv  # importando o arquivo csv.

    with open('alunos.csv', 'r') as data_file:
        csv_reader = csv.reader(data_file)
        for i, line in enumerate(csv_reader):
            print(line)


