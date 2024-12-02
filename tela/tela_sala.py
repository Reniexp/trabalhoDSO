from exceptions.EntradaInvalidaNoPrompt import EntradaInvalidaNoPrompt
import PySimpleGUI as sg

class TelaSala(): 
    def pega_dados_nova_sala(self):
        valid_id = False
        id_sala = input("Id da sala: ")

        while not valid_id:
            try:
                id_sala = int(id_sala)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sala = input("Id da sala: ")
                continue
            else:
                valid_id = True
        
        nomeSala = input("Nome da sala: ")
        while nomeSala == "":
            print("Não pode ser texto vazio")
            nomeSala = input("Nome da sala: ")
        
        valid_capacidade = False
        capacidade = input("Capacidade da sala: ")

        while not valid_capacidade:
            try:
                capacidade = int(capacidade)
            except:
                print("CAPACIDADE É UM VALOR INTEIRO")
                capacidade = input("Capacidade da sala: ")
                continue
            else:
                valid_capacidade = True
        
        return {
            "idSala" : id_sala,
            "nomeSala" : nomeSala,
            "capacidade" : capacidade
        }
    
    def pega_id_valido_sala(self) -> int:
        valid_id = False
        id_sala = input("Id da sala: ")

        while not valid_id:
            try:
                id_sala = int(id_sala)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sala = input("Id da sala: ")
                continue
            else:
                valid_id = True
        return id_sala
    
    # def tela_opcoes_sala(self) -> int:
    #     invalidInput = True
    #     firstTry = True
 

    #     while invalidInput:
    #         if not firstTry:
    #             print()
    #             print("ESCOLHA UM INTEIRO VÁLIDO DE 1 A 6")
    #             print()

    #         print("Tela Sala")
    #         print("\t(1) Mostrar Salas Disponíveis")
    #         print("\t(2) Cadastrar Nova Sala")
    #         print("\t(3) Mostrar Dados de Sala")
    #         print("\t(4) Alterar Sala")
    #         print("\t(5) Deletar Sala")
    #         print("\t(6) SAIR da Tela da Sala")
    #         print()
            
    #         opcao_escolhida = input("Escolha uma opcao: ")
    #         try:
    #             opcao_escolhida = int(opcao_escolhida)
    #             if opcao_escolhida not in [1,2,3,4,5,6]:
    #                 raise EntradaInvalidaNoPrompt()
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
            [sg.Text('Bem vindo ao sistema de gestão de Salas!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Mostrar Salas Disponíveis',"RD1", key='1')],
            [sg.Radio('Cadastrar Nova Sala',"RD1", key='2')],
            [sg.Radio('Mostrar dados de Sala',"RD1", key='3')],
            [sg.Radio('Alterar Sala',"RD1", key='4')],
            [sg.Radio('Deletar Sala',"RD1", key='5')],
            [sg.Radio('Sair da Tela Sala',"RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window =  sg.Window('Sistema de Sala').Layout(layout)

    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes_sala(self) -> int:

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
    
    def pega_dados_atualizar_sala(self):
        nomeSala = input("Nome da sala: ")
        while nomeSala == "":
            print("Não pode ser texto vazio")
            nomeSala = input("Nome da sala: ")
        
        valid_capacidade = False
        capacidade = input("Capacidade da sala: ")

        while not valid_capacidade:
            try:
                capacidade = int(capacidade)
            except:
                print("CAPACIDADE É UM VALOR INTEIRO")
                capacidade = input("Capacidade da sala: ")
                continue
            else:
                valid_capacidade = True
        
        return {
            "nomeSala" : nomeSala,
            "capacidade" : capacidade
        }
    