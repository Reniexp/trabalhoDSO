class Cliente:
    def __init__(self, cpf: int, id_cliente: int, nome: str):
        self.__cpf = cpf
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__filmes_vistos = []
        self.__sessoes_aguardando = []
        
    def __eq__(self, value):
        return self.id_cliente == value.id_cliente
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente: int):
        self.__id_cliente = id_cliente

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def filmes_vistos(self):
        return self.__filmes_vistos

    @property
    def sessoes_aguardando(self):
        return self.__sessoes_aguardando
