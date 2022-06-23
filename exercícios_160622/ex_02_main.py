from ex_02_Retangulo import Retangulo

base = int(input('Informe o valor da base do retangulo: '))
altura = int(input('Informe o valor da altura do retangulo: '))

ret = Retangulo(base, altura)

pisos = ret.area()

rodapes = ret.perimetro()

print(f'Pisos (1 x 1 m²): {pisos}')
print(f'Rodapes(m): {rodapes}')