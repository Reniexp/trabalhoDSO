import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()


    def tela_opcoes_sistema(self) -> int:
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0

    
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
            


    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema de gestão de Cinema!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Gerenciar Clientes',"RD1", key='1')],
            [sg.Radio('Gerenciar Funcionários',"RD1", key='2')],
            [sg.Radio('Gerenciar Filmes',"RD1", key='3')],
            [sg.Radio('Gerenciar Salas',"RD1", key='4')],
            [sg.Radio('Gerenciar Caixa',"RD1", key='5')],
            [sg.Radio('Gerenciar Sessões',"RD1", key='6')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window =  sg.Window('Sistema de Cinema').Layout(layout)

    def mostra_mensagem(self, mensagem: str):
        """Exibe uma mensagem informativa ao usuário."""
        print(mensagem)
