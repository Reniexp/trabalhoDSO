from DAOs.dao import DAO
from entidade.sala import Sala


class salaDAO(DAO):
    def __init__(self):
        super().__init__('sala.pkl')

    def add(self, sala: Sala):
        if((sala is not None) and isinstance(sala, Sala) and isinstance(sala.cpf, int)):
            super().add(sala.cpf, sala)

    def update(self, sala: Sala):
        if((sala is not None) and isinstance(sala, Sala) and isinstance(sala.cpf, int)):
            super().update(sala.cpf, sala)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)