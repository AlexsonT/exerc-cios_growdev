#3) Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular, utilizando a fórmula.
# VOLUME = COMPRIMENTO * LARGURA * ALTURA

comprimento = float(input('Insira em metros o comprimento do retangulo a calcular a área:'))
largura = float(input('Insira em metros a largura do do retangulo a calcular a área:'))
altura = float(input('Insira em metros a altura do retangulo a calcular a área:'))

area = comprimento*largura*altura
print (f'O comprimento total da área calculada é de: {area} metros')
