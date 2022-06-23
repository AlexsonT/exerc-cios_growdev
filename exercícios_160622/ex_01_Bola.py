# 1) Crie uma classe que modele uma bola:
# a) Atributos
#     i) Cor
#     ii) Circunferência
#     iii) Material
# b) Métodos
#     i) troca_cor
#     ii) mostra_cor

class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        print(self.cor)        