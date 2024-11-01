class ControladorFuncionarios():
    def __init__(self, controlador_funcionario):
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema
        
    def pega_funcionario_por_id(self, id_funcionario: int):
        for funcion in self.__funcionarios:
          if(funcion.id_funcionario == id_funcionario):
            return funcion
        return None
    
    #testagem com lançamento de exceção para funcionarios já existentes
    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        id_funcionario = dados_funcionario["id_funcionario"]
        funcionario = self.pega_funcionario_por_id(id_funcionario)
        try:
          if funcionario == None:
            funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["id_funcionario"], dados_funcionario["cargo"], dados_funcionario["salario"], dados_funcionario["periodo"])
            self.__funcionarios.append(funcionario)
          else:
            #raise KeyError
            raise FuncionarioRepetidoException(id)
        
        #alternativa com exceção já existente
        #except KeyError:
          #self.__tela_funcionario.mostra_mensagem("Funcionario já existente!")
        except FuncionarioRepetidoException as e:
          self.__tela_funcionario.mostra_mensagem(e)
          

    def alterar_funcionario(self):
        self.lista_funcionarios()
        id_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_id(id_funcionario)

        if(funcionario is not None):
            novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            funcionario.nome = novos_dados_funcionario["nome"]
            funcionario.cpf = novos_dados_funcionario["cpf"]
            funcionario.id_funcionario = novos_dados_funcionario["id_funcionario"]
            funcionario.cargo = novos_dados_funcionario["cargo"]
            funcionario.salario = novos_dados_funcionario["salario"]
            funcionario.periodo = novos_dados_funcionario["periodo"]
          
            self.lista_funcionarios()
        else:
            self.__tela_funcionario.mostra_mensagem("ATENCAO: Funcionario não existente")


    #sugestao: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_funcionarios(self):
        for funcion in self.__funcionarios:
            self.__tela_funcionario.mostra_funcionario({"nome": funcion.nome, "cpf": funcion.cpf, "id_funcionario": funcion.id_funcionario, "cargo": funcion.cargo, "salario": funcion.salario, "periodo": funcion.periodo})

    def excluir_funcionario(self):
        self.lista_funcionarios()
        id_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_id_funcionario(id_funcionario)

        if(funcionario is not None):
            self.__funcionarios.remove(funcionario)
            self.lista_funcionarios()
        else:
            self.__tela_funcionario.mostra_mensagem("ATENCAO: Funcionario não existente")
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_funcionario, 2: self.alterar_funcionario, 3: self.lista_funcionarios, 4: self.excluir_funcionario, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_funcionario.tela_opcoes()]()
    
