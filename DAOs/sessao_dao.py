from DAOs.dao import DAO
from entidade.sessao import Sessao


class SessaoDAO(DAO):
    def __init__(self,data_source):
        super().__init__(data_source)

    def add(self, sessao: Sessao):
        if((sessao is not None) and isinstance(sessao, Sessao) and isinstance(sessao.id_sessao, int)):
            super().add(sessao)

    def update(self, sessao: Sessao):
        if((sessao is not None) and isinstance(sessao, Sessao) and isinstance(sessao.id_sessao, int)):
            super().update(sessao)

    def get(self, sessao:Sessao):
        if isinstance(sessao, Sessao):
            return super().get(sessao)

    def remove(selfself, sessao: Sessao):
        if(isinstance(sessao, Sessao)):
            return super().remove(sessao)