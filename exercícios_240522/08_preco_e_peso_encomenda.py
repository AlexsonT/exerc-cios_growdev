#8) Crie um algoritmo para uma empresa de transportes que, a partir do peso de uma encomenda fornecida pelo usuário, calcule o preço da remessa conforme a seguinte tabela:
#Peso da encomenda >> Valor
#500 gramas ou menos >> R$ 1,10
#Mais de 500 gramas, mas não maisque 2 quilos >> R$ 2,20
#Mais de 2 quilos, mas não mais de 10 quilos >> R$ 3,70
#Mais de 10 quilos R$ 5,00 mais R$ 3,80/kg pelo peso que ultrapassar 10 Kg

peso = float(input('Insira o peso da mercadoria em kg: '))
excesso = peso - 10


if(peso <= 0.5):
    print('O valor para transporte de sua encomenda é de R$ 1,10')
elif(peso <= 2):
    print('O valor para transporte de sua encomenda é de R$ 2,20')
elif(peso<=10):
    print('O valor para transporte de sua encomenda é de R$ 3,70')
else:
    frete = excesso * 3.8 + 5
    print(f'O valor para transporte de sua encomenda é de R$ {frete: .2f}')