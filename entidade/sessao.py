from .filme import Filme
from .sala import Sala
from .funcionario import EntidadeFuncionario

class Sessao:
    def __init__(self, id_sessao: int, horario: str, filme: Filme, sala: Sala, funcionario: EntidadeFuncionario):
        self.__id_sessao = id_sessao
        self.__horario = horario
        self.__filme = filme
        self.__sala = sala
        self.__funcionario = funcionario
        self.__assentos_disponiveis = sala.capacidade
    
    @property
    def id_sessao(self):
        return self.__id_sessao
    
    @id_sessao.setter
    def id_sessao(self, id_sessao: int):
        self.__id_sessao = id_sessao

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