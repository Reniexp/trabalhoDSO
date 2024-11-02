from entidade.cliente import EntidadeCliente
from tela.tela_cliente import TelaCliente

class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_por_id(self, cpf: int):
        for client in self.__clientes:
            if client.id_cliente == cpf:
                return client
        return None
    
    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        id_cliente = dados_cliente["id_cliente"]
        cliente = self.pega_cliente_por_id(id_cliente)
        try:
          if cliente == None:
            cliente = EntidadeCliente(dados_cliente["cpf"], dados_cliente["id_cliente"], dados_cliente["nome"], dados_cliente["filmesVistos", dados_cliente["sessoesAguardando"]])
            self.__clientes.append(cliente)
          else:
            pass
            #raise KeyError
            #raise AmigoRepetidoException(cpf)
        
        #alternativa com exceção já existente
        #except KeyError:
          #self.__tela_cliente.mostra_mensagem("Cliente já existente!")
        except ClienteRepetidoException as e:
          self.__tela_cliente.mostra_mensagem(e)
          
          
          
          
    def alterar_cliente(self):
        self.lista_clientes()
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_id(id_cliente)

        if(cliente is not None):
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.id_funcionario = novos_dados_cliente["id_funcionario"]
            cliente.nome = novos_dados_cliente["nome"]
            cliente.filmesVistos = novos_dados_cliente["filmesVistos"]
            cliente.sessoesAguardando = novos_dados_cliente["sessoesAguardando"]
            
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Cliente não existente")


    #sugestao: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_clientes(self):
        for client in self.__clientes:
            self.__tela_cliente.mostra_cliente({"cpf": client.cpf, "id_cliente": client.id_cliente, "nome": client.nome, "filmesVistos": client.filmesVistos, "sessoesAguardando": client.sessoesAguardando})

    def excluir_cliente(self):
        self.lista_clientes()
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_id_cliente(id_cliente)

        if(cliente is not None):
            self.__cliente.remove(cliente)
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Cliente não existente")
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.lista_clientes, 4: self.excluir_cliente, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_funcionario.tela_opcoes()]()
