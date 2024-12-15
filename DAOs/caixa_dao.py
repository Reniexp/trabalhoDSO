from DAOs.dao import DAO
from entidade.caixa import Caixa


class caixaDAO(DAO):
    def __init__(self):
        super().__init__('caixa.pkl')

    def add(self, caixa: Caixa):
        if((caixa is not None) and isinstance(caixa, Caixa) and isinstance(caixa.cpf, int)):
            super().add(caixa.cpf, caixa)

    def update(self, caixa: Caixa):
        if((caixa is not None) and isinstance(caixa, Caixa) and isinstance(caixa.cpf, int)):
            super().update(caixa.cpf, caixa)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)