from genero import Genero

class Filme:
    def __init__(self, idFilme: int, titulo: str, duracaoMinutos: int, genero: Genero, tipoExibicao: int):
        self.__idFilme = idFilme
        self.__titulo = titulo
        self.__duracaoMinutos = duracaoMinutos
        self.__genero = genero
        self.__tipoExibicao = tipoExibicao
    
    @property
    def idFilme(self):
        return self.__idFilme
    
    @idFilme.setter
    def idFilme(self, idFilme: int):
        self.__idFilme = idFilme

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def duracaoMinutos(self):
        return self.__duracaoMinutos
    
    @duracaoMinutos.setter
    def duracaoMinutos(self, duracaoMinutos: int):
        self.__duracaoMinutos = duracaoMinutos

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero

    @property
    def tipoExibicao(self):
        return self.__tipoExibicao
    
    @tipoExibicao.setter
    def tipoExibicao(self, tipoExibicao: int):
        self.__tipoExibicao = tipoExibicao
