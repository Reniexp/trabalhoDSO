class Sala:
    def __init__(self,id_sala: int, nome_sala: str, capacidade: int):
        self.__id_sala = id_sala
        self.__nome_sala = nome_sala
        self.__capacidade = capacidade
    def __eq__(self, value):
        return self.__id_sala == value.id_sala
    @property
    def id_sala(self):
        return self.__id_sala
    
    @id_sala.setter
    def id_sala(self, id_sala: int):
        self.__id_sala = id_sala

    @property
    def nome_sala(self):
        return self.__nome_sala
    
    @nome_sala.setter
    def nome_sala(self, nome_sala: str):
        self.__nome_sala = nome_sala

    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade
        