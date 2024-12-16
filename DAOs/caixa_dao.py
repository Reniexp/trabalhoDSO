from DAOs.dao import DAO
from entidade.caixa import Caixa


class CaixaDAO(DAO):
    def __init__(self,data_source: str):
        super().__init__(data_source)

    def add(self, caixa: Caixa):
        if((caixa is not None) and isinstance(caixa, Caixa) and isinstance(caixa.cpf, int)):
            super().add(caixa)

    def update(self, caixa: Caixa):
        if((caixa is not None) and isinstance(caixa, Caixa) and isinstance(caixa.cpf, int)):
            super().update(caixa)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)