# 7) Escreva um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias. Considere ano = 365 dias, mês = 31 dias.
import datetime

tempo = datetime.date.today()
dia = int(input('Dia de Nascimento: '))
mes = int(input('Mês de Nascimento: '))
ano = int(input('Ano de nascimento: '))
tempo2 = datetime.date(day=dia, month=mes, year=ano)
dias = tempo - tempo2
print(dias)



#Forma02
print("Você deverá informar sua idade expressa em anos, meses e dias")

print("Anos: ")
anos = int(input())

print("Mêses: ")
meses = int(input())

print("Dias: ")
dias = int(input())

total_dias = anos * 365 + meses * 31 + dias

print("Sua idade em dias: {}".format(total_dias))