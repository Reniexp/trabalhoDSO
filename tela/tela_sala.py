from exceptions.EntradaInvalidaNoPrompt import EntradaInvalidaNoPrompt
import PySimpleGUI as sg

class TelaSala:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes_sala(self) -> int:
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
        elif values.get('6'):
            opcao = 6
        elif values.get('0') or button in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem-vindo ao sistema de gestão de Salas!', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Mostrar Salas Disponíveis', "RD1", key='1')],
            [sg.Radio('Cadastrar Nova Sala', "RD1", key='2')],
            [sg.Radio('Mostrar dados de Sala', "RD1", key='3')],
            [sg.Radio('Alterar Sala', "RD1", key='4')],
            [sg.Radio('Deletar Sala', "RD1", key='5')],
            [sg.Radio('Sair da Tela Sala', "RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Sala').Layout(layout)

    def pega_dados_nova_sala(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS SALA ----------', font=("Helvica", 25))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id_sala')],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome_sala')],
            [sg.Text('Capacidade:', size=(15, 1)), sg.InputText('', key='capacidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Cadastro de Sala').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        nome_sala = values['nome_sala'].strip()
        capacidade = values['capacidade'].strip()
        id_sala = values['id_sala'].strip()

        
        try:
            if not id_sala.isdigit():
                raise EntradaInvalidaNoPrompt("ID inválido! Deve ser um número.")
            id_sala = int(id_sala)
            
            if not nome_sala:
                raise EntradaInvalidaNoPrompt("Nome da sala não pode estar vazio.")
            if not capacidade.isdigit() or int(capacidade) <= 0:
                raise EntradaInvalidaNoPrompt("Capacidade inválida! Deve ser um número maior que 0.")
            capacidade = int(capacidade)

        except EntradaInvalidaNoPrompt as e:
            self.mostra_mensagem(str(e))
            return self.pega_dados_nova_sala()

        self.close()
        return {
            "id_sala": id_sala,
            "nome_sala": nome_sala,
            "capacidade": capacidade
        }

    def pega_dados_atualizar_sala(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- ALTERAR SALA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome_sala')],
            [sg.Text('Capacidade:', size=(15, 1)), sg.InputText('', key='capacidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de Sala').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        nome_sala = values['nome_sala'].strip()
        capacidade = values['capacidade'].strip()

        
        try:
            if not nome_sala:
                raise EntradaInvalidaNoPrompt("Nome da sala não pode estar vazio.")
            if not capacidade.isdigit() or int(capacidade) <= 0:
                raise EntradaInvalidaNoPrompt("Capacidade inválida! Deve ser um número maior que 0.")
            capacidade = int(capacidade)

        except EntradaInvalidaNoPrompt as e:
            self.mostra_mensagem(str(e))
            return self.pega_dados_atualizar_sala()

        self.close()

        return {
            "nome_sala": nome_sala,
            "capacidade": capacidade
        }
    
    def mostra_sala(self, dados_salas: list):
        string_todas_salas = ""
        for dado in dados_salas:
            string_todas_salas += (
                f"ID: {dado['id_sala']}\n"
                f"NOME DA SALA: {dado['nome_sala']}\n"
                f"CAPACIDADE: {dado['capacidade']} pessoas\n\n"
            )

        sg.Popup('-------- LISTA DE SALAS ----------', string_todas_salas)

    def seleciona_sala(self) -> int:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR SALA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID da sala que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id_sala')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Sala').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        id_sala = values['id_sala'].strip()

        
        if not id_sala.isdigit():
            self.mostra_mensagem("ID inválido! Tente novamente.")
            self.close()
            return self.seleciona_sala()

        self.close()
        return int(id_sala)

    
    def mostra_mensagem(self, msg: str):
        sg.Popup('', msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
