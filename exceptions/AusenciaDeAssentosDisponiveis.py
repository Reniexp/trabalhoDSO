class AusenciaDeAssentosDisponiveis(Exception):
    def __init__(self):
        super().__init__("Não há assentos disponíveis nesta sessão.")