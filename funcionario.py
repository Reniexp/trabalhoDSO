class EntidadeFuncionario:
    def __init__(self, cpf, id_funcionario, nome, cargo, salario, periodo):
        self.__cpf = cpf
        self.__id_funcionario = id_funcionario
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__periodo = periodo

    @property
    def idFuncionario(self):
        return self.__idFuncionario
    
    @idFuncionario.setter
    def idFuncionario(self,idFuncionario: int):
        self.__idFuncionario = idFuncionario

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome: str):
        self.__nome = nome

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self,cargo: str):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,salario: str):
        self.__salario = salario

    @property
    def periodo(self):
        return self.__periodo
    
    @periodo.setter
    def periodo(self,periodo: str):
        self.__periodo = periodo

    
    
#alguns testes   
#instanciando
funcionario1 = Funcionario(idFuncionario=1, nome="João Silva", cargo="Atendente", salario=2500, periodo="Integral")
funcionario1.cadastrarFuncionario()  #cadastrando o funcionário

#editando
funcionario1.editarFuncionario(novoNome="João Silva Santos", novoCargo="Gerente", novoSalario=3000)

#listando os funcionários para verificar as alterações
funcionarios_listados = Funcionario.listarFuncionarios()
for f in funcionarios_listados:
    #Como os atributos são privados, precisamos implementar um método para visualizá-los.
    print(f"ID: {f._Funcionario__idFuncionario}, Nome: {f._Funcionario__nome}, Cargo: {f._Funcionario__cargo}, Salário: {f._Funcionario__salario}, Período: {f._Funcionario__periodo}")