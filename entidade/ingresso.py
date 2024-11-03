from entidade.cliente import Cliente
from entidade.sessao import Sessao

class Ingresso:
    def __init__(self, idIngresso: int, assento: str, cliente:Cliente, sessao : Sessao):
        self.__idIngresso = idIngresso
        self.__assento = assento
        self.__cliente = cliente
        self.__sessao = sessao
       
    @property
    def idIngresso(self):
        return self.__idIngresso
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def assento(self):
        return self.__assento
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def sessao(self):
        return self.__sessao 
