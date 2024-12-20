from entidade.cliente import Cliente
from tela.tela_cliente import TelaCliente
from exceptions.ClienteJaExiste import ClienteJaExiste
from exceptions.ClienteNaoEncontrado import ClienteNaoEncontrado
from exceptions.ClienteNaoCadastrado import ClienteNaoCadastrado
from exceptions.OpcaoInvalida import OpcaoValida
from exceptions.NaoFoiPossivelPersistirOsDados import NaoFoiPossivelPersistirOsDados
from DAOs.cliente_dao import ClienteDAO
import pickle
import os

class ControladorCliente:
    def __init__(self, controlador_sistema):
        #self.__clientes = []
        #cliente_directory = os.getcwd().replace("\\","/")+"/controlador/clientes.pkl"
        self.__cliente_DAO = ClienteDAO("clientes.pkl")
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    @property
    def clientes(self):
        return self.__cliente_DAO.get_all()

    def pega_cliente_por_id(self, id_cliente: int):
        #for cliente in self.load():
        #    if cliente.id_cliente == id_cliente:
        #        return cliente
        #return None
        for cliente in self.__cliente_DAO.get_all():
            #print(cliente.id_cliente)
            if(cliente.id_cliente == id_cliente):
                return cliente
        return None


    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        if dados_cliente is None:
            return

        cliente = self.pega_cliente_por_id(dados_cliente["id_cliente"])

        if cliente is None:
            novo_cliente = Cliente(
                dados_cliente["cpf"], dados_cliente["id_cliente"], dados_cliente["nome"]
            )
            self.__cliente_DAO.add(novo_cliente)
            self.__tela_cliente.mostra_mensagem("Cliente incluído com sucesso!")
        else:
            try:
                raise ClienteJaExiste()
            except:
                return

    def alterar_cliente(self):
        if  len(self.__cliente_DAO.get_all()) == 0:
            self.__tela_cliente.mostra_mensagem("Nenhum cliente cadastrado para alterar.")
            return

        self.lista_clientes()
        id_cliente = self.__tela_cliente.seleciona_cliente()
        if id_cliente is None:
            return

        cliente = self.pega_cliente_por_id(id_cliente)

        if cliente is not None:
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            if novos_dados_cliente is None:
                return

            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.id_cliente = novos_dados_cliente["id_cliente"]
            cliente.nome = novos_dados_cliente["nome"]
            self.__tela_cliente.mostra_mensagem("Cliente alterado com sucesso!")
        else:
            try:
                raise ClienteNaoEncontrado()
            except ClienteNaoEncontrado:
                return

    def listar_filmes_vistos(self):
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_id(id_cliente)
        if cliente:
            self.__tela_cliente.mostra_filmes_vistos(cliente.listar_filmes_vistos())
        else:
            try:
                raise ClienteNaoEncontrado()
            except ClienteNaoEncontrado:
                return

    def listar_sessoes_aguardando(self):
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_id(id_cliente)
        if cliente:
            self.__tela_cliente.mostra_sessoes_aguardando(cliente.listar_sessoes_aguardando())
        else:
            try:
                raise ClienteNaoEncontrado()
            except ClienteNaoEncontrado:
                return

    def lista_clientes(self):
        if len(self.__cliente_DAO.get_all()) == 0:
            self.__tela_cliente.mostra_mensagem("Nenhum cliente cadastrado.")
            try:
                raise ClienteNaoCadastrado()
            except ClienteNaoCadastrado:
                return
        else:
            dados_clientes = [
                {"cpf": cliente.cpf, "id_cliente": cliente.id_cliente, "nome": cliente.nome}
                for cliente in self.__cliente_DAO.get_all()
            ]
            self.__tela_cliente.mostra_cliente(dados_clientes)

    def excluir_cliente(self):
        if  len(self.__cliente_DAO.get_all()) == 0:
            self.__tela_cliente.mostra_mensagem("Nenhum cliente cadastrado para excluir.")
            return

        self.lista_clientes()
        id_cliente = self.__tela_cliente.seleciona_cliente()
        if id_cliente is None:
            return

        cliente = self.pega_cliente_por_id(id_cliente)

        if cliente is not None:
            self.__cliente_DAO.remove(cliente)
            self.__tela_cliente.mostra_mensagem("Cliente excluído com sucesso.")
        else:
            try:
                raise ClienteNaoEncontrado()
            except ClienteNaoEncontrado:
                return

    def retornar(self):
        self.__controlador_sistema.abre_tela_sistema()

    def abre_tela(self):
        while True:
            opcao = self.__tela_cliente.tela_opcoes()
            if opcao == 1:
                self.incluir_cliente()
            elif opcao == 2:
                self.alterar_cliente()
            elif opcao == 3:
                self.lista_clientes()
            elif opcao == 4:
                self.excluir_cliente()
            elif opcao == 0:
                self.retornar()
                break
            else:
                self.__tela_cliente.mostra_mensagem("Opção inválida.")
                try:
                    raise OpcaoValida()
                except OpcaoValida:
                    return

