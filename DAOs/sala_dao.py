from DAOs.dao import DAO
from entidade.sala import Sala


class salaDAO(DAO):
    def __init__(self):
        super().__init__('sala.pkl')

    def add(self, sala: Sala):
        if((sala is not None) and isinstance(sala, Sala) and isinstance(sala.id_sala, int)):
            super().add(sala.id_sala, sala)

    def update(self, sala: Sala):
        if((sala is not None) and isinstance(sala, Sala) and isinstance(sala.id_sala, int)):
            super().update(sala.id_sala, sala)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)