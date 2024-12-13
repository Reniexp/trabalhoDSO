import PySimpleGUI as sg

class TelaCliente:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self) -> int:
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
        elif values.get('0') or button in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem-vindo ao sistema de gestão de Clientes!', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Novo Cliente', "RD1", key='1')],
            [sg.Radio('Alterar Cliente', "RD1", key='2')],
            [sg.Radio('Listar Clientes', "RD1", key='3')],
            [sg.Radio('Excluir Cliente', "RD1", key='4')],
            [sg.Radio('Sair da Tela Cliente', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Clientes').Layout(layout)

    def pega_dados_cliente(self) -> dict:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF (11 dígitos):', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('ID do Cliente (número):', size=(15, 1)), sg.InputText('', key='id_cliente')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Clientes').Layout(layout)

        button, values = self.open()

        if button != 'Confirmar':
            self.close()
            return None

        nome = values['nome'].strip()
        cpf = values['cpf'].strip()
        id_cliente = values['id_cliente'].strip()

        if not nome or not self.valida_cpf(cpf) or not self.valida_id_cliente(id_cliente):
            self.mostra_mensagem("Dados inválidos! Verifique as informações e tente novamente.")
            self.close()
            return self.pega_dados_cliente()

        self.close()
        return {"nome": nome, "cpf": cpf, "id_cliente": int(id_cliente)}

    def mostra_cliente(self, dados_cliente: list):
        string_todos_clientes = ""
        for dado in dados_cliente:
            string_todos_clientes += (
                f"NOME DO CLIENTE: {dado['nome']}\n"
                f"CPF DO CLIENTE: {dado['cpf']}\n"
                f"ID DO CLIENTE: {dado['id_cliente']}\n\n"
            )

        sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes)

    def seleciona_cliente(self) -> str:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do cliente que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id_cliente')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Cliente').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        id_cliente = values['id_cliente'].strip()
        if not self.valida_id_cliente(id_cliente):
            self.mostra_mensagem("ID inválido! Tente novamente.")
            self.close()
            return self.seleciona_cliente()

        self.close()
        return int(id_cliente)

    def mostra_mensagem(self, msg: str):
        sg.Popup('', msg)

    def valida_cpf(self, cpf: str) -> bool:
        return cpf.isdigit() and len(cpf) == 11

    def valida_id_cliente(self, id_cliente: str) -> bool:
        return id_cliente.isdigit()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
