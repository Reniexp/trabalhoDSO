from DAOs.dao import DAO
from entidade.genero import Genero


class generoDAO(DAO):
    def __init__(self):
        super().__init__('genero.pkl')

    def add(self, genero: Genero):
        if((genero is not None) and isinstance(genero, Genero) and isinstance(genero.cpf, int)):
            super().add(genero.cpf, genero)

    def update(self, genero: Genero):
        if((genero is not None) and isinstance(genero, Genero) and isinstance(genero.cpf, int)):
            super().update(genero.cpf, genero)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)