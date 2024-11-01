class EntidadeCliente:
    def __init__(self, cpf: int, id_cliente: int, nome: str):
        self.__cpf = cpf
        self.__id_cliente = __id_cliente
        self.__nome = nome
        self.__filmesVistos = []
        self.__sessoesAguardando = []
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def id_cliente(self):
        return self.__idCliente
    
    @property
    def nome(self):
        return self.__nome
    
    def comprarIngresso(self, sessao):
        self.__sessoesAguardando.append(sessao)

    def listarFilmesVistos(self):
        return self.filmesVistos

    def listarSessoesAguardando(self):
        return self.__sessoesAguardando