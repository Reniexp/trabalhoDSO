from pessoa_abstrata import Pessoa

class Cliente(Pessoa):
    def __init__(self, cpf: int, id_cliente: int, nome: str):
        super().__init__(cpf, nome)
        
        self.__cpf = cpf
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__filmes_vistos = []
        self.__sessoes_aguardando = []
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def filmes_vistos(self):
        return self.__filmes_vistos
    
    @property
    def sessoes_aguardando(self):
        return self.__sessoes_aguardando
