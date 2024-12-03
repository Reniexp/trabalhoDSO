import PySimpleGUI as sg


class TelaCliente:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self) -> int:
        self.init_opcoes()
        button, values = self.__window.open()
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

                if values['0'] or button in (None, 'Cancelar'):
                    opcao = 0

                self.close()
                return opcao

    
    # def tela_opcoes(self) -> int:
    #     opcao_valida = False
    #     while not opcao_valida:
    #         print("-------- CLIENTES ----------")
    #         print("Escolha a opção:")
    #         print("1 - Incluir Cliente")
    #         print("2 - Alterar Cliente")
    #         print("3 - Listar Clientes")
    #         print("4 - Excluir Cliente")
    #         print("0 - Retornar")

    #         opcao = input("Escolha a opção: ")
    #         try:
    #             opcao = int(opcao)
    #             if opcao in [0, 1, 2, 3, 4]:
    #                 opcao_valida = True
    #             else:
    #                 print("Opção inválida! Escolha um número entre 0 e 4.")
    #         except ValueError:
    #             print("Entrada inválida! Digite um número inteiro.")
    #     return opcao


    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema de gestão de Clientes!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Cadastrar Novo Cliente',"RD1", key='1')],
            [sg.Radio('Alterar Cliente',"RD1", key='2')],
            [sg.Radio('Listar Clientes',"RD1", key='3')],
            [sg.Radio('Excluir Cliente',"RD1", key='4')],
            [sg.Radio('Sair da Tela Cliente',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window =  sg.Window('Sistema de Clientes').Layout(layout)

    def close(self):
        self.__window.Close()
                
    def pega_dados_cliente(self) -> dict:
        
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Text('ID do Cliente:', size=(15, 1)), sg.InputText('', key='id_cliente')],
        [sg.Text('Filmes vistos:', size=(15, 1)), sg.InputText('', key='filmes_vistos')],
        [sg.Text('Sessões aguardando:', size=(15, 1)), sg.InputText('', key='sessoes_aguardando')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        cpf = values['cpf']

        self.close()
        return {"nome": nome, "telefone": telefone, "cpf": cpf}

        #print("-------- DADOS CLIENTE ----------")
        #
        #
        #nome = input("Nome: ")
        #while nome == "":
        #    print("O nome não pode ser vazio.")
        #    nome = input("Nome: ")

        
        #cpf = input("CPF (somente números): ")
        #while not self.valida_cpf(cpf):
        #    print("CPF inválido. Digite exatamente 11 dígitos numéricos.")
        #    cpf = input("CPF (somente números): ")
        
        
        #id_cliente = input("ID: ")
        #while not self.valida_id_cliente(id_cliente):
        #    print("ID inválido! Deve ser um número inteiro.")
        #    id_cliente = input("ID: ")
        #id_cliente = int(id_cliente)

        
        #filmes_vistos = input("Filmes vistos (separe por vírgula ou digite '0' se não houver): ")
        #filmes_vistos_lista = [] if filmes_vistos.strip() == "0" else [f.strip() for f in filmes_vistos.split(",")]

        
        #sessoes_aguardando = input("Sessões aguardando (separe por vírgula ou digite '0' se não houver): ")
        #sessoes_aguardando_lista = [] if sessoes_aguardando.strip() == "0" else [s.strip() for s in sessoes_aguardando.split(",")]

        #return {
        #    "nome": nome,
        #    "cpf": cpf,
        #    "id_cliente": id_cliente,
        #    "filmes_vistos": filmes_vistos_lista,
        #    "sessoes_aguardando": sessoes_aguardando_lista,
        #}

    def mostra_cliente(self, dados_cliente: dict):
        string_todos_clientes = ""
        for dado in dados_amigo:
            string_todos_clientes = string_todos_clientes + "NOME DO CLIENTE: " + dado["nome"] + '\n'
            string_todos_clientes = string_todos_clientes + "CPF DO CLIENTE: " + str(dado["cpf"]) + '\n'
            string_todos_clientes = string_todos_clientes + "ID DO CLIENTE: " + str(dado["id_cliente"]) + '\n\n'
            string_todos_clientes = string_todos_clientes + "FILMES VISTOS DO CLIENTE: " + str(dado["filmes_vistos"]) + '\n\n'
            string_todos_clientes = string_todos_clientes + "SESSÕES AGUARDANDO DO CLIENTE: " + str(dado["sessoes_aguardando"]) + '\n\n'


        sg.Popup('-------- LISTA DE AMIGOS ----------', string_todos_clientes)
        
        
        #filmes_vistos = dados_cliente.get("filmes_vistos", [])
        #sessoes_aguardando = dados_cliente.get("sessoes_aguardando", [])

        #print("NOME DO CLIENTE:", dados_cliente["nome"])
        #print("CPF DO CLIENTE:", dados_cliente["cpf"])
        #print("ID DO CLIENTE:", dados_cliente["id_cliente"])
        #print("FILMES VISTOS DO CLIENTE:", ", ".join(filmes_vistos) if filmes_vistos else "Nenhum")
        #print("SESSOES AGUARDANDO DO CLIENTE:", ", ".join(sessoes_aguardando) if sessoes_aguardando else "Nenhuma")
        #print("\n")

    def seleciona_cliente(self) -> int:
        id_cliente = input("ID do cliente que deseja selecionar: ")
        while not self.valida_id_cliente(id_cliente):
            print("ID inválido. Digite novamente.")
            id_cliente = input("ID do cliente que deseja selecionar: ")
        return int(id_cliente)

    def mostra_mensagem(self, msg: str):
        print(msg)

    def valida_cpf(self, cpf: str) -> bool:
        if len(cpf) != 11:
            return False
        for caractere in cpf:
            if caractere < '0' or caractere > '9':
                return False
        return True

    def valida_id_cliente(self, id_cliente: str) -> bool:
        try:
            int(id_cliente)
            return True
        except ValueError:
            return False
