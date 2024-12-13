class SalaJaExiste(Exception):
    def __init__(self):
        super().__init__("Sala ja existe")