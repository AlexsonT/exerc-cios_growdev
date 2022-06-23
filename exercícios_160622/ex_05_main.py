from ex_05_Retangulo import Ret
from ex_05_Ponto import Ponto


ret = Ret()

ret.ponto_1 = Ponto(4, 3)
ret.ponto_2 = Ponto(10, 7)

ponto_central = ret.centro()

ponto_central.exibe()