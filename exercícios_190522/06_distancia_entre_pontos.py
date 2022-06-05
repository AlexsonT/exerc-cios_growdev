# 6) Escreva um programa que receba a posição de dois pontos em um espaço 2D, ou seja, cada ponto tem coordenadas x e y, e calcule a distância entre esses dois pontos, exibindo-a na tela.
x1 = float(input('Informe o eixo x do primeiro ponto! '))
y1 = float(input('Informe o eixo y do primeiro ponto! '))
x2 = float(input('Informe o eixo x do segundo ponto! '))
y2 = float(input('Informe o eixo y do segundo ponto! '))


distancia = ((x2-x1)**2 + (y2-y1)**2)
print(f'A distância entre os dois pontos é: {distancia}')