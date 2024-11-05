class Caixa:
    def __init__(self):
        self.__total_vendas = 0.0
        self.__ingressos_vendidos = []

    @property
    def total_vendas(self):
        return self.__total_vendas
    
    @property
    def ingressos_vendidos(self):
        return self.__ingressos_vendidos
    
    def registrar_venda(self, ingresso):
        self.__total_vendas += 10
        self.ingressos_vendidos.append(ingresso)

