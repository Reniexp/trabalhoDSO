import PySimpleGUI as sg

class TelaCaixa:
    def _init_(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes_caixa(self) -> int:
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
            [sg.Text('Bem-vindo ao sistema de gestão de Caixa!', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Vender Ingresso (INGRESSO : R$10.00)', "RD1", key='1')],
            [sg.Radio('Mostrar Total de Vendas', "RD1", key='2')],
            [sg.Radio('Listar Ingressos Vendidos', "RD1", key='3')],
            [sg.Radio('Mostrar Sessões Mais Populares', "RD1", key='4')],
            [sg.Radio('Mostrar Filmes Mais Assistidos', "RD1", key='5')],
            [sg.Radio('Sair da Tela Caixa', "RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Caixa').Layout(layout)

    def pegar_dados_ingresso(self) -> dict:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS INGRESSO ----------', font=("Helvica", 25))],
            [sg.Text('ID do Ingresso:', size=(15, 1)), sg.InputText('', key='id_ingresso')],
            [sg.Text('ID da Sessão:', size=(15, 1)), sg.InputText('', key='id_sessao')],
            [sg.Text('ID do Cliente:', size=(15, 1)), sg.InputText('', key='id_cliente')],
            [sg.Text('Assento:', size=(15, 1)), sg.InputText('', key='assento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Ingresso').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        id_ingresso = values['id_ingresso'].strip()
        id_sessao = values['id_sessao'].strip()
        id_cliente = values['id_cliente'].strip()
        assento = values['assento'].strip()

        if not id_ingresso or not id_sessao or not id_cliente or not assento:
            self.mostra_mensagem("Dados inválidos! Verifique as informações e tente novamente.")
            self.close()
            return self.pegar_dados_ingresso()

        self.close()
        return {
            "id_ingresso": int(id_ingresso),
            "id_sessao": int(id_sessao),
            "id_cliente": int(id_cliente),
            "assento": assento
        }

    def mostra_mensagem(self, msg: str):
        sg.Popup('', msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
