# 11) Qual opção de pagamento é mais utilizada em cada faixa etária?

import csv


with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    # Jovens = 18 a 25 anos
    # Adultos, 26 a 59 anos
    # Idosos, igual ou maior que 60 anos

    debito1 = credito1 = dinheiro1 = 0
    debito2 = credito2 = dinheiro2 = 0
    debito3 = credito3 = dinheiro3 = 0
        
    for line in csv_reader:
        line[2] = int(line[2])
        if line[2] >= 18 and line[2] < 26:
            if line[6] == 'debito':
                debito1 += 1
            elif line[6] == 'credito':
                credito1 +=1            
            else:
                dinheiro1 += 1

        elif line[2] >= 26 and line[2] < 60:
            if line[6] == 'debito':
                debito2 += 1
            elif line[6] == 'credito':
                credito2 +=1            
            else:
                dinheiro2 += 1

        else:       
            if line[6] == 'debito':
                debito3 += 1
            elif line[6] == 'credito':
                credito3 +=1            
            else:
                dinheiro3 += 1

print('*'*50)
if debito1 > credito1 and debito1 > dinheiro1:
    print('A opção de pagamento mais utilizada pelos jovens é o Débito.')
elif credito1 > debito1 and credito1 > dinheiro1: 
    print('A opção de pagamento mais utilizada pelos jovens é o Crédito.')
else:
    print('A opção de pagamento mais utilizada pelos jovens é o Dinheiro.')

if debito2 > credito2 and debito2 > dinheiro2:
    print('A opção de pagamento mais utilizada pelos adultos é o Débito.')
elif credito2 > debito2 and credito2 > dinheiro2: 
    print('A opção de pagamento mais utilizada pelos adultos é o Crédito.')
else:
    print('A opção de pagamento mais utilizada pelos adultos é o Dinheiro.')  

if debito3 > credito3 and debito3 > dinheiro3:
    print('A opção de pagamento mais utilizada pelos idosos é o Débito.')
elif credito3 > debito3 and credito3 > dinheiro3: 
    print('A opção de pagamento mais utilizada pelos idosos é o Crédito.')
else:
    print('A opção de pagamento mais utilizada pelos idosos é o Dinheiro.')                 

print('*'*50)