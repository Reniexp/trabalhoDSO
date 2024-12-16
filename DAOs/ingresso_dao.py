from DAOs.dao import DAO
from entidade.ingresso import Ingresso


class ingressoDAO(DAO):
    def __init__(self, data_source):
        super().__init__(data_source) #'ingresso.pkl'

    def add(self, ingresso: Ingresso):
        if((ingresso is not None) and isinstance(ingresso, Ingresso) and isinstance(ingresso.id_ingresso, int)):
            super().add(ingresso.id_ingresso, ingresso)

    def update(self, ingresso: Ingresso):
        if((ingresso is not None) and isinstance(ingresso, Ingresso) and isinstance(ingresso.id_ingresso, int)):
            super().update(ingresso.id_ingresso, ingresso)

    def get(self, ingresso: Ingresso):
        if isinstance(ingresso, Ingresso):
            return super().get(ingresso)

    def remove(selfself, ingresso: Ingresso):
        if(isinstance(ingresso, Ingresso)):
            return super().remove(ingresso)