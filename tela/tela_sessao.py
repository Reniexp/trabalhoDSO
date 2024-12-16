import PySimpleGUI as sg

class TelaSessao:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes_sessao(self) -> int:
        self.init_opcoes()
        button, values = self.open()
        opcao = 0

        if values.get('1'):
            opcao = 1
        elif values.get('2'):
            opcao = 2
        elif values.get('3'):
            opcao = 3
        elif values.get('4'):
            opcao = 4
        elif values.get('5'):
            opcao = 5
        # elif values.get('6'):
        #     opcao = 6
        elif values.get('0') or button in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem-vindo ao sistema de gestão de Sessões!', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Mostrar Sessões Disponíveis', "RD1", key='1')],
            [sg.Radio('Cadastrar Nova Sessão', "RD1", key='2')],
            [sg.Radio('Mostrar dados de Sessão', "RD1", key='3')],
            [sg.Radio('Alterar Sessão', "RD1", key='4')],
            [sg.Radio('Deletar Sessão', "RD1", key='5')],
            [sg.Radio('Sair da Tela Sessão', "RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Sessões').Layout(layout)

    def pega_dados_nova_sessao(self) -> dict:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS SESSÃO ----------', font=("Helvica", 25))],
            [sg.Text('ID da Sessão:', size=(15, 1)), sg.InputText('', key='id_sessao')],
            [sg.Text('Horário (HH:MM):', size=(15, 1)), sg.InputText('', key='horario')],
            [sg.Text('ID do Filme:', size=(15, 1)), sg.InputText('', key='id_filme')],
            [sg.Text('ID da Sala:', size=(15, 1)), sg.InputText('', key='id_sala')],
            [sg.Text('ID do Funcionário:', size=(15, 1)), sg.InputText('', key='id_funcionario')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Sessão').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        id_sessao = values['id_sessao'].strip()
        horario = values['horario'].strip()
        id_filme = values['id_filme'].strip()
        id_sala = values['id_sala'].strip()
        id_funcionario = values['id_funcionario'].strip()

        if not id_sessao or not horario or not id_filme or not id_sala or not id_funcionario:
            self.mostra_mensagem("Dados inválidos! Verifique as informações e tente novamente.")
            self.close()
            return self.pega_dados_nova_sessao()

        self.close()
        return {
            "id_sessao": int(id_sessao),
            "horario": horario,
            "id_filme": int(id_filme),
            "id_sala": int(id_sala),
            "id_funcionario": int(id_funcionario)
        }

    def mostra_sessao(self, dados_sessoes: list):
        string_todas_sessoes = ""
        for dado in dados_sessoes:
            string_todas_sessoes += (
                f"ID: {dado['id_sessao']}\n"
                f"HORÁRIO: {dado['horario']}\n"
                f"ID FILME: {dado['id_filme']}\n"
                f"ID SALA: {dado['id_sala']}\n"
                f"ID FUNCIONÁRIO: {dado['id_funcionario']}\n\n"
            )

        sg.Popup('-------- LISTA DE SESSÕES ----------', string_todas_sessoes)

    def seleciona_sessao(self) -> int:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR SESSÃO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID da sessão que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id_sessao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Sessão').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        id_sessao = values['id_sessao'].strip()
        if not id_sessao.isdigit():
            self.mostra_mensagem("ID inválido! Tente novamente.")
            self.close()
            return self.seleciona_sessao()

        self.close()
        return int(id_sessao)

    def mostra_mensagem(self, msg: str):
        sg.Popup('', msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
