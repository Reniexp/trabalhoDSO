import PySimpleGUI as sg

class TelaFilme:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes_filme(self) -> int:
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
            [sg.Text('Bem-vindo ao sistema de gestão de Filmes!', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Mostrar Filmes Disponíveis', "RD1", key='1')],
            [sg.Radio('Cadastrar Novo Filme', "RD1", key='2')],
            [sg.Radio('Mostrar dados de Filme', "RD1", key='3')],
            [sg.Radio('Alterar Filme', "RD1", key='4')],
            [sg.Radio('Deletar Filme', "RD1", key='5')],
            [sg.Radio('Sair da Tela Filme', "RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Filmes').Layout(layout)

    def pega_dados_novo_filme(self) -> dict:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS FILME ----------', font=("Helvica", 25))],
            [sg.Text('ID do Filme:', size=(15, 1)), sg.InputText('', key='id_filme')],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Text('Duração (em minutos):', size=(15, 1)), sg.InputText('', key='duracao')],
            [sg.Text('Gênero:', size=(15, 1))],
            [sg.Radio('Ação', "GENERO", key='genero_acao'), sg.Radio('Comédia', "GENERO", key='genero_comedia'),
             sg.Radio('Romance', "GENERO", key='genero_romance'), sg.Radio('Ficção Científica', "GENERO", key='genero_ficcao')],
            [sg.Text('Tipo de Exibição:', size=(15, 1))],
            [sg.Radio('Dublado', "TIPO_EXIBICAO", key='dublado'), sg.Radio('Legendado', "TIPO_EXIBICAO", key='legendado'),
             sg.Radio('Dublado e Legendado', "TIPO_EXIBICAO", key='dublado_legendado')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Filme').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        id_filme = values['id_filme'].strip()
        titulo = values['titulo'].strip()
        duracao = values['duracao'].strip()
        genero = None
        tipo_exibicao = None

        if values.get('genero_acao'):
            genero = 'Ação'
        elif values.get('genero_comedia'):
            genero = 'Comédia'
        elif values.get('genero_romance'):
            genero = 'Romance'
        elif values.get('genero_ficcao'):
            genero = 'Ficção Científica'

        if values.get('dublado'):
            tipo_exibicao = 'Dublado'
        elif values.get('legendado'):
            tipo_exibicao = 'Legendado'
        elif values.get('dublado_legendado'):
            tipo_exibicao = 'Dublado e Legendado'

        if not id_filme or not titulo or not duracao or not genero or not tipo_exibicao:
            self.mostra_mensagem("Dados inválidos! Verifique as informações e tente novamente.")
            self.close()
            return self.pega_dados_novo_filme()

        self.close()
        return {"id_filme": int(id_filme), "titulo": titulo, "duracao": int(duracao), "genero": genero, "tipo_exibicao": tipo_exibicao}

    def mostra_filme(self, dados_filmes: list):
        string_todos_filmes = ""
        for dado in dados_filmes:
            string_todos_filmes += (
                f"ID: {dado['id_filme']}\n"
                f"TÍTULO: {dado['titulo']}\n"
                f"DURAÇÃO: {dado['duracao']} minutos\n"
                f"GÊNERO: {dado['genero']}\n"
                f"TIPO DE EXIBIÇÃO: {dado['tipo_exibicao']}\n\n"
            )

        sg.Popup('-------- LISTA DE FILMES ----------', string_todos_filmes)

    def seleciona_filme(self) -> int:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR FILME ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do filme que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id_filme')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Filme').Layout(layout)

        button, values = self.open()
        if button != 'Confirmar':
            self.close()
            return None

        id_filme = values['id_filme'].strip()
        if not id_filme.isdigit():
            self.mostra_mensagem("ID inválido! Tente novamente.")
            self.close()
            return self.seleciona_filme()

        self.close()
        return int(id_filme)

    def mostra_mensagem(self, msg: str):
        sg.Popup('', msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
