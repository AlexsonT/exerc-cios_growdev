# 1) Crie uma classe que modele uma bola:
# a) Atributos
#     i) Cor
#     ii) Circunferência
#     iii) Material
# b) Métodos
#     i) troca_cor
#     ii) mostra_cor

from ex_01_Bola import Bola

bola = Bola('vermelho', 0.7, 'couro')

bola.mostra_cor()

bola.troca_cor('branco')

bola.mostra_cor()
