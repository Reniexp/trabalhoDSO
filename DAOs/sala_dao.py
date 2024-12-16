from DAOs.dao import DAO
from entidade.sala import Sala


class SalaDAO(DAO):
    def __init__(self, data_source: str):
        super().__init__(data_source)

    def add(self, sala: Sala):
        if (sala is not None) and isinstance(sala, Sala) : #and isinstance(sala.id_sala, int))
            super().add(sala)

    def update(self, sala: Sala):
        if((sala is not None) and isinstance(sala, Sala) and isinstance(sala.id_sala, int)):
            super().update(sala)

    def get(self, sala:Sala):
        if isinstance(sala, Sala):
            return super().get(sala)

    def remove(selfself, sala:Sala):
        if(isinstance(sala, Sala)):
            return super().remove(sala)