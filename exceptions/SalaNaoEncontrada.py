class SalaNaoEncontrada(Exception):
    def __init__(self):
        super().__init__(f"Sala não encontrada ou indisponível")