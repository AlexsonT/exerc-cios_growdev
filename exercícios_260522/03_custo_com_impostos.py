# 3) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

produto = float(input("Insira o custo de produção do veículo: "))

print(f'O valor de venda do seu veículo é ${produto*1.73: ,.2f}, destes sendo: ${produto*.28: ,.2f}(28%) de impostos e ${produto*.45: ,.2f}(45%) de margem.')
