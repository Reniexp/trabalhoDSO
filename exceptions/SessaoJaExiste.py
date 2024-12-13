class SessaoJaExiste(Exception):
    def __init__(self):
        super().__init__("Sessão ja existe")