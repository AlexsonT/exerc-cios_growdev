# 2) Crie uma classe que modele um retângulo:
#     a) Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#     b) Métodos:
#         i) Mudar valor dos lados
#         ii) Retornar valor dos lados
#         iii) Calcular Área
#         iv) Calcular Perímetro;
# c) Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. Depois, deve-se criar um objeto com as medidas e calcular a quantidade (em m2) de pisos (1 x 1 m2) e de rodapés necessários para o local.

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_lados(self, base, altura):
        self.base = base
        self.altura = altura

    def lados(self):
        return self.base, self.altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2            

