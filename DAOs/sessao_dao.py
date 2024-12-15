from DAOs.dao import DAO
from entidade.sessao import Sessao


class sessaoDAO(DAO):
    def __init__(self):
        super().__init__('sessao.pkl')

    def add(self, sessao: Sessao):
        if((sessao is not None) and isinstance(sessao, Sessao) and isinstance(sessao.cpf, int)):
            super().add(sessao.cpf, sessao)

    def update(self, sessao: Sessao):
        if((sessao is not None) and isinstance(sessao, Sessao) and isinstance(sessao.cpf, int)):
            super().update(sessao.cpf, sessao)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)