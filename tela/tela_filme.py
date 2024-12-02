from exceptions.EntradaInvalidaNoPrompt import EntradaInvalidaNoPrompt
import PySimpleGUI as sg

class TelaFilme():
    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema de gestão de Filmes!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Mostrar Filmes Disponíveis',"RD1", key='1')],
            [sg.Radio('Cadastrar Novo Filme',"RD1", key='2')],
            [sg.Radio('Mostrar dados de Filme',"RD1", key='3')],
            [sg.Radio('Alterar Filme',"RD1", key='4')],
            [sg.Radio('Deletar Filme',"RD1", key='5')],
            [sg.Radio('Sair da Tela Filme',"RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window =  sg.Window('Sistema de Filmes').Layout(layout)

    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes_filme(self) -> int:

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
            
        # invalidInput = True
        # firstTry = True

        # while invalidInput:
        #     if not firstTry:
        #         print()
        #         print("ESCOLHA UM INTEIRO VÁLIDO DE 1 A 6")
        #         print()
                
        #     print("Tela filme")
        #     print("\t(1) Mostrar Filmes Disponíveis")
        #     print("\t(2) Cadastrar Novo Filme")
        #     print("\t(3) Mostrar Dados de Filme")
        #     print("\t(4) Alterar Filme")
        #     print("\t(5) Deletar Filme")
        #     print("\t(6) SAIR da Tela Filme")
        #     print()
            
        #     opcao_escolhida = input("Escolha uma opcao: ")
        #     try:
        #         opcao_escolhida = int(opcao_escolhida)
        #         if opcao_escolhida not in [1,2,3,4,5,6]:
        #             raise EntradaInvalidaNoPrompt(opcao_escolhida)
        #     except:
        #         firstTry = False
        #         continue
        #     else:
        #         invalidInput = False
        # return opcao_escolhida
    
    def pega_id_valido_filme(self) -> int:
        valid_id = False
        id_filme = input("Id do filme: ")

        while not valid_id:
            try:
                id_filme = int(id_filme)
            except:
                print("ID É UM VALOR INTEIRO")
                id_filme = input("Id do filme: ")
                continue
            else:
                valid_id = True
        return id_filme

    def pega_genero_filme(self):
        invalidInput = True
        firstTry = True

        while invalidInput:
            if not firstTry:
                print("ESCOLHA UM INTEIRO VÁLIDO : 1 , 2, 3 OU 4")
            print()
            print("Qual o genero do filme?")
            print("\t1 - Acao")
            print("\t2 - Comedia")
            print("\t3 - Romance")
            print("\t4 - Ficcao Cientifica")

            opcao_escolhida = input("Escolha uma opcao: ")
            try:
                opcao_escolhida = int(opcao_escolhida)
                
                if opcao_escolhida not in [1,2,3,4]:
                    firstTry = False
                    continue
            except:
                firstTry = False
                continue
            else:
                invalidInput = False
        return opcao_escolhida


    def pega_tipo_de_exibicao(self):
        invalidInput = True
        firstTry = True

        while invalidInput:
            if not firstTry:
                print("ESCOLHA UM INTEIRO VÁLIDO : 1 , 2 OU 3")
            print()
            print("Qual o tipo de exibição do filme?")
            print("\t1 - Dublado")
            print("\t2 - Legendado")
            print("\t3 - Dublado e Legendado")

            opcao_escolhida = input("Escolha uma opcao: ")
            try:
                opcao_escolhida = int(opcao_escolhida)
                
                if opcao_escolhida not in [1,2,3]:
                    firstTry = False
                    continue
            except:
                firstTry = False
                continue
            else:
                invalidInput = False
        return opcao_escolhida

    def pega_dados_novo_filme(self):
        valid_id = False
        id_filme = input("Id do filme: ")

        while not valid_id:
            try:
                id_filme = int(id_filme)
            except:
                print("ID É UM VALOR INTEIRO")
                id_filme = input("Id do filme: ")
                continue
            else:
                valid_id = True
  
        titulo = input("Titulo do filme: ")
        while titulo == "":
            print("Não pode ser texto vazio")
            titulo = input("Titulo do filme: ")

        duracao_minutos = input("Duracao em minutos do filme: ")
        valid_duracao = False

        while not valid_duracao:
            try:
                duracao_minutos = int(duracao_minutos)
            except:
                print("DURACAO É UM VALOR INTEIRO")
                duracao_minutos = input("Duracao em minutos do filme: ")
                continue
            else:
                valid_duracao = True

        genero = self.pega_genero_filme()

        tipo_de_exibicao = self.pega_tipo_de_exibicao()

        return {
            "idFilme" : id_filme,
            "titulo" : titulo,
            "duracaoMinutos" : duracao_minutos,
            "genero" : genero,
            "tipoExibicao" : tipo_de_exibicao
        }
    
    def pega_dados_atualizar_filme(self):
        titulo = input("Titulo do filme: ")
        while titulo == "":
            print("Não pode ser texto vazio")
            titulo = input("Titulo do filme: ")

        duracao_minutos = input("Duracao em minutos do filme: ")
        valid_duracao = False

        while not valid_duracao:
            try:
                duracao_minutos = int(duracao_minutos)
            except:
                print("DURACAO É UM VALOR INTEIRO")
                duracao_minutos = input("Duracao em minutos do filme: ")
                continue
            else:
                valid_duracao = True

        genero = self.pega_genero_filme()

        tipo_de_exibicao = self.pega_tipo_de_exibicao()

        return {
            "titulo" : titulo,
            "duracaoMinutos" : duracao_minutos,
            "genero" : genero,
            "tipoExibicao" : tipo_de_exibicao
        }


        

        