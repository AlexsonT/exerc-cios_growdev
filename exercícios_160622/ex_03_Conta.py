# 3) Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos:
#     a) número da conta
#     b) nome do correntista
#     c) saldo
# Os métodos são os seguintes:
#     a) alterar_nome
#     b) deposito
#     c) saque
# No construtor, o saldo é opcional, com valor padrão zero e os demais atributos são obrigatórios.

class Conta:

    def __init__(self, numero, nome, saldo = 0):
        self.numero_conta = numero
        self.nome_correntista = nome 
        self.saldo = saldo

    def alterar_nome(self, nom):
        self.nome = nome 

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor): 
        if self.saldo - valor >= 0:
            self.saldo -= valor   
        else:
            print(f'Saldo insuficiente para a retirada do valor {valor}')       

    def mostra_saldo(self):
        print(f'R$ {self.saldo}')
            
