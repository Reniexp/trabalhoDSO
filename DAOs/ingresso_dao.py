from DAOs.dao import DAO
from entidade.ingresso import Ingresso


class ingressoDAO(DAO):
    def __init__(self):
        super().__init__('ingresso.pkl')

    def add(self, ingresso: Ingresso):
        if((ingresso is not None) and isinstance(ingresso, Ingresso) and isinstance(ingresso.id_ingresso, int)):
            super().add(ingresso.id_ingresso, ingresso)

    def update(self, ingresso: Ingresso):
        if((ingresso is not None) and isinstance(ingresso, Ingresso) and isinstance(ingresso.id_ingresso, int)):
            super().update(ingresso.id_ingresso, ingresso)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)