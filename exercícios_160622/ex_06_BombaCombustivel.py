# 6) Faça um programa completo utilizando classes e métodos que:
#     a) Possua uma classe chamada BombaCombustivel, com no mínimo esses atributos:
#         i) tipo_combustivel.
#         ii) valor_litro
#         iii) quantidade_combustivel
#     b) Possua no mínimo esses métodos:
#         i) abastecer_por_valor() – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo;
#         ii) abastecer_por_litro() – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#         iii) alterar_valor() – altera o valor do litro do combustível.
#         iv) alterar_combustivel() – altera o tipo do combustível.
#         v) alterar_quantidade_combustivel() – altera a quantidade de combustível restante na bomba.

# OBS: Sempre que acontecer um abastecimento é necessárioatualizar a quantidade de combustível total na bomba.

class BombaCombustivel:

    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        print(f'Você abasteceu {litros: .2f} de um total de R${valor}')
        self.alterar_quantidade_combustivel(litros)
        pass

    def abastecer_por_litro(self, litros):
        print('Você abasteceu {litros} litros')
        valor = litros * self.valor_litro
        print(f'Você abasteceu {litros} de um total de R${valor}')
        self.alterar_quantidade_combustivel(litros)

    def alterar_valor(self, valor_litro):
        self.valor_litro = valor_litro

    def alterar_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel

    def alterar_quantidade_combustivel(self, litros):
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
        else:
            print('Quantidade de litros insuficientes!')    


