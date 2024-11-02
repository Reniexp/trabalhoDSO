class EntidadeCaixa:
    def __init__(self):
        self.total_vendas = 0.0
        self.ingressos_vendidos = []

    def registrar_venda(self, ingresso):
        self.total_vendas += ingresso.preco
        self.ingressos_vendidos.append(ingresso)
