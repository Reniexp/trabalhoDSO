class Caixa:
    def __init__(self):
        self.total_vendas = 0.0
        self.ingressos_vendidos = []

    def registrar_venda(self, ingresso):
        self.total_vendas += ingresso.preco
        self.ingressos_vendidos.append(ingresso)

    @property
    def ingressos_vendidos(self):
        return self.__ingressos_vendidos

    def adicionar_ingresso(self, ingresso):
        self.__ingressos_vendidos.append(ingresso)

