from filme import Filme
from sala import Sala


class Sessao:
    def __init__(self, idSessao: int, horario: str, filme: Filme, sala: Sala):
        self.__idSessao = idSessao
        self.__horario = horario
        self.__filme = filme
        self.__sala = sala
    
    @property
    def idSessao(self):
        return self.__idSessao
    
    @idSessao.setter
    def idSessao(self, idSessao: int):
        self.__idSessao = idSessao

    @property
    def horario(self):
        return self.__horario
    
    @horario.setter
    def horario(self, horario: str):
        self.__horario = horario

    @property
    def filme(self):
        return self.__filme
    
    @filme.setter
    def filme(self, filme: Filme):
        self.__filme = filme

    @property
    def sala(self):
        return self.__sala
    
    @sala.setter
    def sala(self, sala: Sala):
        self.__sala = sala