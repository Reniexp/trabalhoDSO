class NenhumIngressoVendido(Exception):
    def __init__(self):
        super().__init__("Nenhum ingresso vendido.")