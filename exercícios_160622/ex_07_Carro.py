# 7) Implemente uma classe chamada Carro com as seguintes propriedades:
#     a) Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
#     b) O consumo é especificado no construtor e o nível de combustível inicial é 0.
#     c) Forneça um método andar() que simula o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
#     d) Forneça um método obter_gasolina(), que retorna o nível atual de combustível e forneça um método adicionar_gasolina(), para abastecer o tanque.
#     Exemplo:
#         meu_fusca = Carro(15)
#         meuFusca.adicionar_gasolina(20)
#         meuFusca.andar(100)
#         meuFusca.obter_gasolina()

class Carro:

    def __init__(self, consumo_litro, tanque):
        self.consumo_litro = consumo_litro
        self.autonomia_atual = tanque

    def andar(self, distancia):
        self.andar = distancia
        tanque = self.autonomia_atual - self.andar
        if distancia <= self.autonomia_atual:
            print(f'O carro percorreu {distancia} km e tem {tanque} km de autonomia')
        else:
            print('Distancia maior que autonomia, necessário abastecer.')    
        

    def obter_gasolina(self):
        tanque = self.autonomia_atual - self.andar
        litros = tanque / self.consumo_litro
        print(f'Você ainda possui{litros: .2f} litros de gasolina.')
        print(f'Você ainda tem {tanque} km de autonomia')
               
    def adicionar_gasolina(self, adicionar_gasolina):
        self.adicionar_gasolina = adicionar_gasolina
        self.autonomia_atual += (adicionar_gasolina * self.consumo_litro)  
        # tanque = adicionar_gasolina * self.consumo_litro
        
        

        