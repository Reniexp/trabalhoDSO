class Genero:
    def __init__(self, nome):
        self.__nome = nome
        self.__contador_assistidos = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def contador_assistidos(self):
        return self.__contador_assistidos

    def incrementar_assistidos(self):
        self.__contador_assistidos += 1