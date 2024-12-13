class SessaoNaoEncontrada(Exception):
    def __init__(self):
        super().__init__("Sessão não encontrada ou indisponível.")