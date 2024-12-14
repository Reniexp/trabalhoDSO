from .filme import Filme
from .sala import Sala
from .funcionario import EntidadeFuncionario

class Sessao:
    def __init__(self, idSessao: int, horario: str, filme: Filme, sala: Sala, funcionario: EntidadeFuncionario):
        self.__idSessao = idSessao
        self.__horario = horario
        self.__filme = filme
        self.__sala = sala
        self.__funcionario = funcionario
        self.__assentos_disponiveis = sala.capacidade
    
    def __eq__(self, value):
        return self.__idSessao == value.idSessao
    
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

    @property
    def funcionario(self):
        return self.__funcionario
    
    @funcionario.setter
    def funcionario(self, funcionario: EntidadeFuncionario):
        self.__funcionario = funcionario

    @property
    def assentos_disponiveis(self):
        return self.__assentos_disponiveis
    
    @assentos_disponiveis.setter
    def assentos_disponiveis(self, assentos_disponiveis: int):
        self.__assentos_disponiveis = assentos_disponiveis