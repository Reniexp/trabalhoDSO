class EntidadeIngresso:
    def __init__(self, idIngresso: int, assento: str, valor: float, cliente: Cliente, sessao: Sessao):
        self.__idIngresso = idIngresso
        self.__assento = assento
        self.__valor = valor
        self.__cliente = cliente
        self.__sessao = sessao
    
    @property
    def idIngresso(self):
        return self.__idIngresso
    @idIngresso.setter
    def idIngresso(self, idIngresso: int):
        self.__idIngresso = idIngresso

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor: int):
        self.__valor = valor

    @property
    def assento(self):
        return self.__assento
    @assento.setter
    def assento(self, assento: str):
        self.__assento = assento

    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente
    
    @property
    def sessao(self):
        return self.__sessao
    @sessao.setter
    def sessao(self, sessao: Sessao):
        self.__sessao = sessao