from controlador.controlador_clientes import ControladorCliente
from controlador_funcionarios import ControladorFuncionarios
from controlador_filme import ControladorFilme
from controlador_sala import ControladorSala
from tela.tela_sistema import TelaSistema
from controlador_sessao import ControladorSessao
from controlador_caixa import ControladorCaixa


class ControladorSistema:
    def __init__(self):
        self.__controlador_clientes = ControladorCliente(self)
        self.__controlador_funcionarios = ControladorFuncionarios(self)
        self.__controlador_filme = ControladorFilme(self)
        self.__controlador_sala = ControladorSala(self)
        self.__controlador_sessao = ControladorSessao(self)
        self.__controlador_caixa = ControladorCaixa(self)
        self.__tela_sistema = TelaSistema()

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
    
    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_cliente(self):
        self.__controlador_clientes.abre_tela()

    def cadastra_funcionario(self):
        self.__controlador_funcionarios.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        while True:
            opcao = self.menu_principal()
            if opcao == 1:
                self.__controlador_clientes.abre_tela()
            elif opcao == 2:
                 self.__controlador_funcionarios.abre_tela()
            elif opcao == 3:
                 self.__controlador_filme.abre_tela_filme()
            elif opcao == 4:
                 self.__controlador_sala.abre_tela_sala()
            elif opcao == 5:
                 self.__controlador_caixa.abre_tela()
            elif opcao == 0:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

                

    
