# 8) A padaria do Paulo vende pão francês a R$0.75, pão doce a R$0.85 e quindim a R$1.50. Crie um algoritmo que pergunte quantas unidades de cada produto foram vendidas pelo Paulo num dia e calcule o total faturado.

frances = 0.75
doce = 0.85
quindim = 1.50

fat1 = int(input('Quantas unidade foram vendidas de Pão Francês hoje? '))
fat2 = int(input('Quantas unidade foram vendidas de Pão Doce hoje? '))
fat3 = int(input('Quantas unidade foram vendidas de Quindim hoje? '))

faturamento = (fat1*frances)+(fat2*doce)+(fat3*quindim)
print(
    f'O faturamento total dos itens mencionados no dia de hoje foi de: R$ {faturamento}')


# Modificação 1 – Modifique o algoritmo para que, ao invés de considerar o preço dos produtos como fixos, o usuário possa informar o preço deles.
p1 = float(input('Qual é o valor unitário do Pão Francês? '))
fat1 = int(input('Quantas unidade foram vendidas de Pão Francês hoje? '))
p2 = float(input('Qual é o valor unitário do Pão Doce? '))
fat2 = int(input('Quantas unidade foram vendidas de Pão Doce hoje? '))
p3 = float(input('Qual é o valor unitário do Quindim? '))
fat3 = int(input('Quantas unidade foram vendidas de Quindim hoje? '))

faturamento = (fat1*p1)+(fat2*p2)+(fat3*p3)
print(
    f'O faturamento total dos itens mencionados no dia de hoje foi de: R$ {faturamento}')

# Modificação 2 – Paulo tem o hábito de guardar 10% de tudo que fatura numa caderneta de poupança, para eventuais necessidades no futuro. Sabendo disso, modifique o algoritmo que você criou para que ele informe quanto do total faturado deve ser poupado.
p1 = float(input('Qual é o valor unitário do Pão Francês? '))
fat1 = int(input('Quantas unidade foram vendidas de Pão Francês hoje? '))
p2 = float(input('Qual é o valor unitário do Pão Doce? '))
fat2 = int(input('Quantas unidade foram vendidas de Pão Doce hoje? '))
p3 = float(input('Qual é o valor unitário do Quindim? '))
fat3 = int(input('Quantas unidade foram vendidas de Quindim hoje? '))

faturamento = (fat1*p1)+(fat2*p2)+(fat3*p3)
print(
    f'O faturamento total dos itens mencionados no dia de hoje foi de: R$ {faturamento}')

reserva = faturamento * 0.1
print(f'O valor a ser guardado é de: {reserva}')

# Modificação 3 – Modifique o algoritmo para que, antes de calcular quanto deve ser guardado na poupança, ele desconte o valor do imposto devido, que é de 5%.
p1 = float(input('Qual é o valor unitário do Pão Francês? '))
fat1 = int(input('Quantas unidade foram vendidas de Pão Francês hoje? '))
p2 = float(input('Qual é o valor unitário do Pão Doce? '))
fat2 = int(input('Quantas unidade foram vendidas de Pão Doce hoje? '))
p3 = float(input('Qual é o valor unitário do Quindim? '))
fat3 = int(input('Quantas unidade foram vendidas de Quindim hoje? '))

faturamento = (fat1*p1)+(fat2*p2)+(fat3*p3)
print(
    f'O faturamento total dos itens mencionados no dia de hoje foi de: R$ {faturamento}')

reserva = (faturamento * .95) * 0.1
print(f'O valor a ser guardado é de: {reserva}')
