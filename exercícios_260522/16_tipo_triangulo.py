# 16) Construa um algoritmo que, a partir do valor do comprimento dos três lados de um triângulo, classifique-o em equilátero, isósceles ou escaleno. Lembre, um triângulo é equilátero quando o comprimento de todos os seus lados for igual, é isósceles quando apenas um dos lados tiver comprimento diferente e é escaleno quando todos os lados tiverem comprimentos diferentes dos demais lados.
print('*'*50)
ladoa = float(input('Insira a medida do lado "A" do triângulo: '))
ladob = float(input('Insira a medida do lado "B" do triângulo: '))
ladoc = float(input('Insira a medida do lado "C" do triângulo: '))
print('*'*50)

if ladoa == ladob and ladoa == ladoc:
    print('TRIÂNGULO DO TIPO EQUILÁTERO')
elif ladoa == ladob and ladoa != ladoc:
    print('TRIÂNGULO DO TIPO ISÓCELES')
    if ladoa == ladoc and ladoa != ladob:
        print('TRIÂNGULO DO TIPO ISÓCELES')
        if ladob == ladoc and ladob != ladoa:
            print('TRIÂNGULO DO TIPO ISÓCELES')
else:
    print('TRIÂNGULO DO TIPO ESCALENO')
print('*'*50)