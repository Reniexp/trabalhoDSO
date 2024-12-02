from exceptions.EntradaInvalidaNoPrompt import EntradaInvalidaNoPrompt
import PySimpleGUI as sg

class TelaSessao:
    def pega_dados_nova_sessao(self):
        valid_id = False
        id_sessao = input("Id da sessao: ")

        while not valid_id:
            try:
                id_sessao = int(id_sessao)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sessao = input("Id da sessao: ")
                continue
            else:
                valid_id = True

        horario = input("Horario da sessao: ")
        while horario == "":
            print("Não pode ser texto vazio")
            horario = input("Horario da sessao: ")

        valid_id_filme = False
        id_filme = input("Id do filme: ")
        while not valid_id_filme:
            try:
                id_filme = int(id_filme)
            except:
                print("ID É UM VALOR INTEIRO")
                id_filme = input("Id do filme: ")
                continue
            else:
                valid_id_filme = True

        valid_id_sala = False
        id_sala = input("Id da sala: ")
        while not valid_id_sala:
            try:
                id_sala = int(id_sala)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sala = input("Id da sala: ")
                continue
            else:
                valid_id_sala = True

        valid_id_funcionario = False
        id_funcionario = input("Id do funcionario responsavel: ")
        while not valid_id_funcionario:
            try:
                id_funcionario = int(id_funcionario)
            except:
                print("ID É UM VALOR INTEIRO")
                id_funcionario = input("Id do funcionario responsavel: ")
                continue
            else:
                valid_id_funcionario = True

        return {
            "idSessao": id_sessao,
            "idFilme": id_filme,
            "idSala": id_sala,
            "idFuncionario": id_funcionario,
            "horario": horario
        }

    # def tela_opcoes_sessao(self) -> int:
    #     invalidInput = True
    #     firstTry = True

    #     while invalidInput:
    #         if not firstTry:
    #             print()
    #             print("ESCOLHA UM INTEIRO VÁLIDO DE 1 A 6")
    #             print()

    #         print("Tela Sessao")
    #         print("\t(1) Mostrar Sessoes Disponíveis")
    #         print("\t(2) Cadastrar Nova Sessao")
    #         print("\t(3) Mostrar Dados de Sessao")
    #         print("\t(4) Alterar Sessao")
    #         print("\t(5) Deletar Sessao")
    #         print("\t(6) SAIR da Tela Sessao")
    #         print()

    #         opcao_escolhida = input("Escolha uma opcao: ")
    #         try:
    #             opcao_escolhida = int(opcao_escolhida)
    #             if opcao_escolhida not in [1, 2, 3, 4, 5, 6]:
    #                 raise EntradaInvalidaNoPrompt(opcao_escolhida)
    #         except:
    #             firstTry = False
    #             continue
    #         else:
    #             invalidInput = False
    #     return opcao_escolhida

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema de gestão de Sessão!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Mostrar Sessões Disponíveis',"RD1", key='1')],
            [sg.Radio('Cadastrar Nova Sessão',"RD1", key='2')],
            [sg.Radio('Mostrar Dados de Sessão',"RD1", key='3')],
            [sg.Radio('Alterar Sessão',"RD1", key='4')],
            [sg.Radio('Deletar Sessão',"RD1", key='5')],
            [sg.Radio('Sair da Tela Sessão',"RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window =  sg.Window('Sistema de Sessões').Layout(layout)

    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes_sessao(self) -> int:

        self.init_components()
        button, values = self.__window.Read()
        invalid_input = True
        first_try = True
        opcao = 0

        while invalid_input:
            if not first_try:
                if values['1']:
                    opcao = 1
                
                if values['2']:
                    opcao = 2

                if values['3']:
                    opcao = 3

                if values['4']:
                    opcao = 4

                if values['5']:
                    opcao = 5

                if values['6']:
                    opcao = 6

                if values['0'] or button in (None, 'Cancelar'):
                    opcao = 0

                self.close()
                return opcao

    def pega_id_valido_sessao(self) -> int:
        valid_id = False
        id_sessao = input("Id da sessao: ")

        while not valid_id:
            try:
                id_sessao = int(id_sessao)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sessao = input("Id da sessao: ")
                continue
            else:
                valid_id = True
        return id_sessao

    def pega_dados_atualizar_sessao(self):
        horario = input("Horario da sessao: ")
        while horario == "":
            print("Não pode ser texto vazio")
            horario = input("Horario da sessao: ")

        valid_id_filme = False
        id_filme = input("Id do filme: ")
        while not valid_id_filme:
            try:
                id_filme = int(id_filme)
            except:
                print("ID É UM VALOR INTEIRO")
                id_filme = input("Id do filme: ")
                continue
            else:
                valid_id_filme = True

        valid_id_sala = False
        id_sala = input("Id da sala: ")
        while not valid_id_sala:
            try:
                id_sala = int(id_sala)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sala = input("Id da sala: ")
                continue
            else:
                valid_id_sala = True

        valid_id_funcionario = False
        id_funcionario = input("Id do funcionario responsavel: ")
        while not valid_id_funcionario:
            try:
                id_funcionario = int(id_funcionario)
            except:
                print("ID É UM VALOR INTEIRO")
                id_funcionario = input("Id do funcionario responsavel: ")
                continue
            else:
                valid_id_funcionario = True

        return {
            "horario": horario,
            "idFilme": id_filme,
            "idSala": id_sala,
            "idFuncionario": id_funcionario,
        }
