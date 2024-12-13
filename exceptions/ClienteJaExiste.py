class ClienteJaExiste(Exception):
    def __init__(self):
        super().__init__("Cliente ja existe")