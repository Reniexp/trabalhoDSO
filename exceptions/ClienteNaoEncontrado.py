class ClienteNaoEncontrado(Exception):
    def __init__(self):
        super().__init__(f"Cliente não encontrado ou indisponível")