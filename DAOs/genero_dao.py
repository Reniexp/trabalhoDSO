from DAOs.dao import DAO
from entidade.genero import Genero


class generoDAO(DAO):
    def __init__(self,data_source):
        super().__init__(data_source)

    def add(self, genero: Genero):
        if((genero is not None) and isinstance(genero, Genero) and isinstance(genero.nome, str)):
            super().add(genero)

    def update(self, genero: Genero):
        if((genero is not None) and isinstance(genero, Genero) and isinstance(genero.nome, str)):
            super().update(genero)

    def get(self, genero: Genero):
        if isinstance(genero, Genero):
            return super().get(genero)

    def remove(selfself, genero: Genero):
        if(isinstance(genero, Genero)):
            return super().remove(genero)