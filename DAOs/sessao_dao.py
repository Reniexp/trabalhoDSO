from DAOs.dao import DAO
from entidade.sessao import Sessao


class sessaoDAO(DAO):
    def __init__(self):
        super().__init__('sessao.pkl')

    def add(self, sessao: Sessao):
        if((sessao is not None) and isinstance(sessao, Sessao) and isinstance(sessao.id_sessao, int)):
            super().add(sessao.id_sessao, sessao)

    def update(self, sessao: Sessao):
        if((sessao is not None) and isinstance(sessao, Sessao) and isinstance(sessao.id_sessao, int)):
            super().update(sessao.id_sessao, sessao)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)