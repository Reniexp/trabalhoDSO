class NenhumaSessaoVendida(Exception):
    def __init__(self):
        super().__init__("Nenhuma sessão vendida")