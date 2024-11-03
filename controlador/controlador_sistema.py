from controlador_clientes import ControladorCliente
from controlador_funcionarios import ControladorFuncionarios
from controlador_filme import ControladorFilme
from controlador_sala import ControladorSala
from tela.tela_sistema import TelaSistema
from controlador_sessao import ControladorSessao

class ControladorSistema:
    def __init__(self):
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionarios(self)
        self.__controlador_filme = ControladorFilme(self)
        self.__controlador_sala = ControladorSala(self)
        self.__controlador_sessao = ControladorSessao(self)
        self.__tela_sistema = TelaSistema()

    def abre_tela(self):
        while True:
            opcao = self.menu_principal()
            if opcao == 1:
                self.__controlador_cliente.abre_tela()
            elif opcao == 2:
                 self.__controlador_funcionario.abre_tela()
            elif opcao == 3:
                 self.__controlador_filme.abre_tela_filme()
            elif opcao == 4:
                 self.__controlador_sala.abre_tela()
            elif opcao == 5:
                 self.__controlador_sessao.abre_tela()
            elif opcao == 0:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

    def menu_principal(self):
        print("\nMenu Principal:")
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Funcionários")
        print("3 - Gerenciar Filmes")
        print("4 - Gerenciar Salas")
        print("5 - Gerenciar Sessões")
        print("0 - Sair")
        return int(input("Selecione uma opção: "))
