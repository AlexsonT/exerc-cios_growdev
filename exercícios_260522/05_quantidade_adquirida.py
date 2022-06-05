#5) Faça um algoritmo para ler a quantidade adquirida e o preço unitário de um produto.
#a) Calcular e escrever o total (total = quantidade adquirida * preço unitário);
#b) Leia o desconto sobre a compra e calcule (total a pagar = total - desconto);
#Sabendo-se que:
#(1) Se quantidade <= 5 o desconto será de 2%.
#(2) Se quantidade > 5 e quantidade <=10 o desconto será de 3%.
#(3) Se quantidade > 10 o desconto será de 5%.


qtd = int(input('Insira a quantidade adquirida: '))
punit = float(input('Insira o valor unitário do produto: '))

ptotal = qtd * punit
print(f'O valor total da sua compra foi de ${ptotal: .2f}')

print('-'*50)

if(qtd <= 5):
    print(f'Você comprou {qtd} unidade(s) e recebeu "2%" de desconto.')
    print(f'O valor do seu desconto é de $: {ptotal*.02: .2f}')
    print(f'Valor total a pagar é $: {ptotal*.98: .2f}')
elif(qtd > 5 and qtd <= 10):
    print(f'Você comprou {qtd} unidade(s) e recebeu "3%" de desconto.')
    print(f'O valor do seu desconto é de $: {ptotal*.03: .2f}')
    print(f'O valor total a pagar é $: {ptotal*.97: .2f}')
else:
    print(f'Você comprou {qtd} unidade(s) e recebeu "5%" de desconto.')
    print(f'O valor do seu desconto é de $: {ptotal*.05: .2f}')
    print(f'O valor total a pagar é $: {ptotal*.95: .2f}')
print('-'*50)