from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, cpf:int, nome:str):
        pass
    
    @property
    def cpf(self):
        pass
    
    @cpf.setter
    def cpf(self, cpf: int):
        pass

    @property
    def nome(self):
        pass
    
    @nome.setter
    def nome(self, nome: int):
        pass

