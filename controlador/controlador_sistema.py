from controlador.controlador_clientes import ControladorCliente
from controlador.controlador_funcionarios import ControladorFuncionarios
from controlador.controlador_filme import ControladorFilme
from controlador.controlador_sala import ControladorSala
from tela.tela_sistema import TelaSistema
from controlador.controlador_sessao import ControladorSessao
from controlador.controlador_caixa import ControladorCaixa
from controlador.controlador_sessao import ControladorSessao


class ControladorSistema:
    __instance = None
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_clientes = ControladorCliente(self)
        self.__controlador_funcionarios = ControladorFuncionarios(self)
        self.__controlador_filme = ControladorFilme(self)
        self.__controlador_sala = ControladorSala(self)
        self.__controlador_sessao = ControladorSessao(self)
        self.__controlador_caixa = ControladorCaixa(self)
        self.sessoes = self.__controlador_sessao.sessoes
        self.clientes = self.__controlador_clientes.clientes


    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente
    
    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario
    
    @property
    def controlador_filme(self):
        return self.__controlador_filme
    
    @property
    def controlador_sala(self):
        return self.__controlador_sala
    
    @property
    def controlador_sessao(self):
        return self.__controlador_sessao
    
    @property
    def controlador_caixa(self):
        return self.__controlador_caixa
    
    def obter_sessao_por_id(self, id_sessao):
        self.sessoes = self.__controlador_sessao.sessoes
        for sessao in self.sessoes:
            if sessao.idSessao == id_sessao:
                return sessao
        return None 

    def obter_cliente_por_id(self, id_cliente):
        self.clientes = self.__controlador_clientes.clientes
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None 

    
    def requisitos_para_sessao(self):
        if not self.__controlador_sala.existe_sala() or not self.__controlador_filme.existe_filme() or not self.__controlador_funcionarios.existe_funcionario():
            self.__tela_sistema.mostra_mensagem("Erro: Certifique-se de que pelo menos uma sala, um filme e um funcionário estejam cadastrados antes de criar uma sessão.")
            return False
        return True

    def abre_tela_sistema(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes_sistema()
            if opcao == 1:
                self.__controlador_clientes.abre_tela()
            elif opcao == 2:
                self.__controlador_funcionarios.abre_tela()
            elif opcao == 3:
                self.__controlador_filme.abre_tela_filme()
            elif opcao == 4:
                self.__controlador_sala.abre_tela_sala()
            elif opcao == 5:
                self.__controlador_caixa.abre_tela_caixa()
            elif opcao == 6:
                if self.requisitos_para_sessao():
                    self.__controlador_sessao.abre_tela_sessao()
            elif opcao == 0:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")
        
    
    def inicializa_sistema(self):
        self.abre_tela_sistema()

    def cadastra_cliente(self):
        self.__controlador_clientes.abre_tela()

    def cadastra_funcionario(self):
        self.__controlador_funcionarios.abre_tela()

    def encerra_sistema(self):
        exit(0)
    
    def pega_filme(self,id_filme):
        return self.__controlador_filme.pega_filme_por_id(id_filme)
    
    def pega_sala(self,id_sala):
        return self.__controlador_sala.pega_sala_pelo_id(id_sala)
    
    def pega_funcionario(self,id_funcionario):
        return self.__controlador_funcionarios.pega_funcionario_por_id(id_funcionario)


