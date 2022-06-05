# 20) Dado que uma empresa possui valores variáveis de suas ações ao longo do tempo, e que existe sempre uma taxa (que também é variável) a ser paga para realizar transações de compra e venda, escreva um programa que peça a quantidade de ações compradas, o valor da ação naquele período e qual a taxa que foi paga, peça também as mesmas informações em relação a venda de ações. O programa deve exibir:
# a) O valor total gasto na compra de ações
# b) O valor pago em taxa durante a compra
# c) O valor total ganho na venda das ações
# d) O valor pago na venda
# e) O valor de diferença total entre a compra e a venda

qtd = int(input('Qual a quantia de ações compradas? '))
vlunit = float(input('Qual o valor unitário das ações compradas? '))
tx = float(input('Qual a taxa das ações compradas? '))

total = (qtd*vlunit)
tx2 = total * (tx/100)


print(
    f'O valor total da compra das ações foi de R$ {total+tx2} destes sendo R$ {total*(tx/100)} de taxas')


qtdv = int(input('Qual a quantia de ações vendidas? '))
vlunitv = float(input('Qual o valor unitário das ações vendidas? '))
txv = float(input('Qual a taxa das ações vendidas? '))


totalv = (qtdv*vlunitv)
tx2v = totalv * (txv/100)

print(
    f'O valor total da venda das ações foi de R$ {totalv+tx2v} destes sendo R$ {totalv*(txv/100)} de taxas')


print(f'O lucro na venda das ações foi de R$ {(totalv+tx2v)-(total+tx2)} ')