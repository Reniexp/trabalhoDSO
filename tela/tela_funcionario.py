import PySimpleGUI as sg

class TelaFuncionario:
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
            [sg.Text('Bem-vindo ao Sistema de Gestão de Funcionários!', font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvetica", 15))],
            [sg.Radio('Cadastrar Novo Funcionário', "RD1", key='1')],
            [sg.Radio('Alterar Funcionário', "RD1", key='2')],
            [sg.Radio('Listar Funcionários', "RD1", key='3')],
            [sg.Radio('Excluir Funcionário', "RD1", key='4')],
            [sg.Radio('Sair da Tela Funcionário', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Funcionários').Layout(layout)

    def pega_dados_funcionario(self) -> dict:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS FUNCIONÁRIO ----------', font=("Helvetica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF (11 dígitos):', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('ID do Funcionário (número):', size=(15, 1)), sg.InputText('', key='id_funcionario')],
            [sg.Text('Cargo:', size=(15, 1)), sg.InputText('', key='cargo')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
            [sg.Text('Período (Manhã/Tarde/Noite):', size=(15, 1)), sg.InputText('', key='periodo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Funcionários').Layout(layout)

        button, values = self.open()

        if button != 'Confirmar':
            self.close()
            return None

        nome = values['nome'].strip()
        cpf = values['cpf'].strip()
        id_funcionario = values['id_funcionario'].strip()
        cargo = values['cargo'].strip()
        salario = values['salario'].strip()
        periodo = values['periodo'].strip()

        if (not nome or not self.valida_cpf(cpf) or not self.valida_id_funcionario(id_funcionario) or 
                not cargo or not self.valida_salario(salario) or not periodo):
            self.mostra_mensagem("Dados inválidos! Verifique as informações e tente novamente.")
            self.close()
            return self.pega_dados_funcionario()

        self.close()
        return {
            "nome": nome,
            "cpf": cpf,
            "id_funcionario": int(id_funcionario),
            "cargo": cargo,
            "salario": float(salario),
            "periodo": periodo
        }

    def mostra_funcionarios(self, dados_funcionarios: list):
        string_todos_funcionarios = ""
        for dado in dados_funcionarios:
            string_todos_funcionarios += (
                f"NOME: {dado['nome']}\n"
                f"CPF: {dado['cpf']}\n"
                f"ID: {dado['id_funcionario']}\n"
                f"CARGO: {dado['cargo']}\n"
                f"SALÁRIO: {dado['salario']}\n"
                f"PERÍODO: {dado['periodo']}\n\n"
            )

        sg.Popup('-------- LISTA DE FUNCIONÁRIOS ----------', string_todos_funcionarios)

    def seleciona_funcionario(self) -> int:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR FUNCIONÁRIO ----------', font=("Helvetica", 25))],
            [sg.Text('Digite o ID do funcionário que deseja selecionar:', font=("Helvetica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id_funcionario')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Funcionário').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        id_funcionario = values['id_funcionario'].strip()
        if not self.valida_id_funcionario(id_funcionario):
            self.mostra_mensagem("ID inválido! Tente novamente.")
            self.close()
            return self.seleciona_funcionario()

        self.close()
        return int(id_funcionario)

    def mostra_mensagem(self, msg: str):
        sg.Popup('', msg)

    def valida_cpf(self, cpf: str) -> bool:
        return cpf.isdigit() and len(cpf) == 11

    def valida_id_funcionario(self, id_funcionario: str) -> bool:
        return id_funcionario.isdigit()

    def valida_salario(self, salario: str) -> bool:
        try:
            float(salario)
            return True
        except ValueError:
            return False

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
