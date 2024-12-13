class NaoFoiPossivelPersistirOsDados(Exception):
    def __init__(self):
        super().__init__(f"Não foi possível persistir os dados")