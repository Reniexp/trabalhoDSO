class EntidadeFuncionario:
    def __init__(self, cpf, id_funcionario, nome, cargo, salario, periodo):
        self.__cpf = cpf
        self.__id_funcionario = id_funcionario
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__periodo = periodo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def id_funcionario(self):
        return self.__id_funcionario

    @id_funcionario.setter
    def id_funcionario(self, id_funcionario: int):
        self.__id_funcionario = id_funcionario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario

    @property
    def periodo(self):
        return self.__periodo

    @periodo.setter
    def periodo(self, periodo: str):
        self.__periodo = periodo
