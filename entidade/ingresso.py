from entidade.cliente import Cliente
from entidade.sessao import Sessao

class Ingresso:
    def __init__(self, id_ingresso: int, assento: str, cliente:Cliente, sessao : Sessao):
        self.__id_ingresso = id_ingresso
        self.__assento = assento
        self.__cliente = cliente
        self.__sessao = sessao
       
    @property
    def idIngresso(self):
        return self.__id_ingresso
    
    @property
    def assento(self):
        return self.__assento
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def sessao(self):
        return self.__sessao 
