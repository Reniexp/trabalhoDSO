class TipoDeExibicao():
    def __init__(self, codigo_do_tipo_de_exibicao: int):
        if codigo_do_tipo_de_exibicao == 1:
            self.__tipo_de_exibicao = "dublado"
        elif codigo_do_tipo_de_exibicao == 2:
            self.__tipo_de_exibicao = "legendado"
        elif codigo_do_tipo_de_exibicao == 3:
            self.__tipo_de_exibicao = "dublado e legendado"
    
    @property
    def tipo_de_exibicao(self):
        return self.__tipo_de_exibicao

    @tipo_de_exibicao.setter
    def tipo_de_exibicao(self, codigo_do_tipo_de_exibicao: int):
        if codigo_do_tipo_de_exibicao == 1:
            self.__tipo_de_exibicao = "dublado"
        elif codigo_do_tipo_de_exibicao == 2:
            self.__tipo_de_exibicao = "legendado"
        elif codigo_do_tipo_de_exibicao == 3:
            self.__tipo_de_exibicao = "dublado e legendado"



class Filme:
    def __init__(self, idFilme: int, titulo: str, duracaoMinutos: int, genero: str, tipoExibicao: TipoDeExibicao ):
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
    def tipoExibicao(self, tipoExibicao: TipoDeExibicao):
        self.__tipoExibicao = tipoExibicao
