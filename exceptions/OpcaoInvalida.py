class OpcaoValida(Exception):
    def __init__(self):
        super().__init__(f"Opção inválida")