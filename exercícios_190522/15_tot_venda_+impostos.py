# 15) Um cliente de uma loja está comprando cinco produtos. Crie um programa que solicite o preço de cada um desses produtos e, em seguida, exiba o subtotal da venda, o valor do imposto e o valor total(subtotal da venda mais o valor do imposto). Suponha que a alíquota do imposto seja de 6 % sobre o subtotal da venda.

prod01 = float(input('Insira o valor do primeiro produto: '))
prod02 = float(input('Insira o valor do segundo produto: '))
prod03 = float(input('Insira o valor do terceiro produto: '))
prod04 = float(input('Insira o valor do quarto produto: '))
prod05 = float(input('Insira o valor do quinto produto: '))


vcompra = prod01 + prod02 + prod03 + prod04 + prod05
impostos = vcompra * .06
vtotal = vcompra + impostos
print(f'O valor total das mercadoria é de {vcompra} R$ e os impostos adicionados correspondem a {impostos} R$, portanto o valor total fica: {vtotal} R$')
