import PySimpleGUI as sg


class TelaCaixa:
    # def mostrar_opcoes(self):
    #     print("\n----- Caixa -----")
    #     print("INGRESSO : R$10.00")
    #     print("1 - Vender Ingresso")
    #     print("2 - Mostrar Total de Vendas")
    #     print("3 - Listar Ingressos Vendidos")
    #     print("4 - Mostrar Sessões Mais Populares")  
    #     print("5 - Mostrar Filmes Mais Assistidos")  
    #     print("0 - Sair")
    #     return int(input("Escolha uma opção: "))
    
    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema de gestão de Caixa!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Vender Ingresso',"RD1", key='1')],
            [sg.Radio('Mostrar Total de Vendas',"RD1", key='2')],
            [sg.Radio('Listar Ingressos Vendidos',"RD1", key='3')],
            [sg.Radio('Mostrar Sessões Mais Populares',"RD1", key='4')],
            [sg.Radio('Mostrar Filmes Mais Assistidos',"RD1", key='5')],
            [sg.Radio('Sair da Tela Caixa',"RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window =  sg.Window('Sistema de Caixa').Layout(layout)

    def __init__(self):
        self.__window = None
        self.init_components()

    def mostrar_opcoes(self) -> int:

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

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_detalhes_ingresso(self, ingresso):
        print("\n--- Ingresso Vendido ---")
        print(f"ID: {ingresso.idIngresso}")
        print(f"Assento : {ingresso.assento}")
        print(f"Filme: {ingresso.sessao.filme.titulo}")
        print(f"Sala: {str(ingresso.sessao.sala.idSala)}")
        print(f"Horário: {ingresso.sessao.horario}")

    def pegar_dados_ingresso(self):
        print("\n--- Dados do Ingresso ---")

        valid_id_ingresso = False
        id_ingresso = input("Id do ingresso: ")

        while not valid_id_ingresso:
            try:
                id_ingresso = int(id_ingresso)
            except:
                print("ID É UM VALOR INTEIRO")
                id_ingresso = input("Id do ingresso: ")
                continue
            else:
                valid_id_ingresso = True

        valid_id_sessao = False
        id_sessao = input("Id da sessão: ")

        while not valid_id_sessao:
            try:
                id_sessao = int(id_sessao)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sessao = input("Id da sessão: ")
                continue
            else:
                valid_id_sessao = True
        
        valid_id_cliente = False
        id_cliente = input("Id do cliente: ")

        while not valid_id_cliente:
            try:
                id_cliente = int(id_cliente)
            except:
                print("ID É UM VALOR INTEIRO")
                id_cliente = input("Id do cliente: ")
                continue
            else:
                valid_id_cliente = True

        assento = input("Qual assento você deseja: ")
        while assento == "":
            print("Não pode ser texto vazio")
            assento = input("Qual assento você deseja: ")

        return {
            "id_ingresso": id_ingresso,
            "id_cliente": id_cliente,
            "sessao": id_sessao,
            "assento": assento
        }
