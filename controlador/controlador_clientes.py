from entidade.EntidadeCliente import EntidadeCliente
from tela.tela_cliente import TelaCliente


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_por_id(self, id_cliente: int):
        for cliente in self.__clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = self.pega_cliente_por_id(dados_cliente["id_cliente"])

        if cliente is None:
            novo_cliente = EntidadeCliente(
                dados_cliente["cpf"], dados_cliente["id_cliente"], dados_cliente["nome"]
            )
            self.__clientes.append(novo_cliente)
            self.__tela_cliente.mostra_mensagem("Cliente incluído com sucesso!")
        else:
            self.__tela_cliente.mostra_mensagem("Cliente já existente.")

    def alterar_cliente(self):
        self.lista_clientes()
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_id(id_cliente)

        if cliente is not None:
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente._EntidadeCliente__cpf = novos_dados_cliente["cpf"]
            cliente._EntidadeCliente__id_cliente = novos_dados_cliente["id_cliente"]
            cliente._EntidadeCliente__nome = novos_dados_cliente["nome"]
            self.__tela_cliente.mostra_mensagem("Cliente alterado com sucesso!")
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado.")

    def listar_filmes_vistos(self):
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_id(id_cliente)
        if cliente:
            self.__tela_cliente.mostra_filmes_vistos(cliente.listar_filmes_vistos())
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado.")

    def listar_sessoes_aguardando(self):
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_id(id_cliente)
        if cliente:
            self.__tela_cliente.mostra_sessoes_aguardando(cliente.listar_sessoes_aguardando())
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado.")

    def lista_clientes(self):
        if not self.__clientes:
            self.__tela_cliente.mostra_mensagem("Nenhum cliente cadastrado.")
        else:
            for cliente in self.__clientes:
                dados_cliente = {
                    "cpf": cliente.cpf,
                    "id_cliente": cliente.id_cliente,
                    "nome": cliente.nome,
                }
                self.__tela_cliente.mostra_cliente(dados_cliente)

    def excluir_cliente(self):
        self.lista_clientes()
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_id(id_cliente)

        if cliente is not None:
            self.__clientes.remove(cliente)
            self.__tela_cliente.mostra_mensagem("Cliente excluído com sucesso.")
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        continua = True
        
        while continua:
            opcao = self.__tela_cliente.tela_opcoes()
            if opcao == 1:
                self.incluir_cliente()
            elif opcao == 2:
                self.alterar_cliente()
            elif opcao == 3:
                self.lista_clientes()
            elif opcao == 4:
                self.excluir_cliente()
            elif opcao == 5:
                self.listar_filmes_vistos()
            elif opcao == 6:
                self.listar_sessoes_aguardando()
            elif opcao == 0:
                self.retornar()
                continua = False
            else:
                self.__tela_cliente.mostra_mensagem("Opção inválida.")

