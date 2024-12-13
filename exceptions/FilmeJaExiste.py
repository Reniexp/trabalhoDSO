class FilmeJaExiste(Exception):
    def __init__(self):
        super().__init__("Filme ja existe")