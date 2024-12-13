class FilmeNaoEncontrado(Exception):
    def __init__(self):
        super().__init__(f"Filme não encontrado ou indisponível")