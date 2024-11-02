class EntidadeSala():
    def __init__(self, idSala: int, nomeSala: str, capacidade: int):
        self.__idSala = idSala
        self.__nomeSala = nomeSala
        self.__capacidade = capacidade

    @property
    def idSala(self):
        return self.__idSala
    
    @property
    def nomeSala(self):
        return self.__nomeSala

    @nomeSala.setter
    def nomeSala(self, nomeSala: str):
        self.__nomeSala = nomeSala
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade: str):
        self.__capacidade = capacidade