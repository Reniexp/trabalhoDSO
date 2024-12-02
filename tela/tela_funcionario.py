import PySimpleGUI as sg


class TelaFuncionario:

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema de gestão de Funcionários!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Cadastrar Novo Funcionário',"RD1", key='1')],
            [sg.Radio('Alterar Funcionário',"RD1", key='2')],
            [sg.Radio('Listar Funcionários',"RD1", key='3')],
            [sg.Radio('Excluir Funcionário',"RD1", key='4')],
            [sg.Radio('Sair da Tela Funcionário',"RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window =  sg.Window('Sistema de Filmes').Layout(layout)

    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self) -> int:

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
    # def tela_opcoes(self) -> int:
    #     opcao_valida = False
    #     while not opcao_valida:
    #         print("-------- FUNCIONARIOS ----------")
    #         print("Escolha a opção:")
    #         print("1 - Incluir Funcionário")
    #         print("2 - Alterar Funcionário")
    #         print("3 - Listar Funcionários")
    #         print("4 - Excluir Funcionário")
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

    def pega_dados_funcionario(self) -> dict:
        print("-------- DADOS FUNCIONARIO ----------")
        
        
        nome = input("Nome: ")
        while nome == "":
            print("O nome não pode ser vazio.")
            nome = input("Nome: ")

        
        cpf = input("CPF (somente números): ")
        while not self.valida_cpf(cpf):
            print("CPF inválido. Digite exatamente 11 dígitos numéricos.")
            cpf = input("CPF (somente números): ")

        id_funcionario = input("ID: ")
        while not self.valida_id_funcionario(id_funcionario):
            print("ID inválido! Deve ser um número inteiro.")
            id_funcionario = input("ID: ")
        id_funcionario = int(id_funcionario)

        
        cargo = input("Cargo: ")
        while cargo == "":
            print("O cargo não pode ser vazio.")
            cargo = input("Cargo: ")

        
        salario = input("Salário: ")
        while not self.valida_salario(salario):
            print("Salário inválido! Deve ser um número.")
            salario = input("Salário: ")
        salario = float(salario)

        
        periodo = input("Período: ")
        while periodo == "":
            print("O período não pode ser vazio.")
            periodo = input("Período: ")

        return {
            "nome": nome,
            "cpf": cpf,
            "id_funcionario": id_funcionario,
            "cargo": cargo,
            "salario": salario,
            "periodo": periodo
        }

    def valida_cpf(self, cpf):
        if len(cpf) != 11:
            return False
        for caractere in cpf:
            if caractere < '0' or caractere > '9':
                return False
        return True

    def valida_id_funcionario(self, id_funcionario):
        try:
            int(id_funcionario)
            return True
        except ValueError:
            return False

    def valida_salario(self, salario):
        try:
            float(salario)
            return True
        except ValueError:
            return False

    def mostra_funcionario(self, dados_funcionario: dict):
        print("-------- DADOS DO FUNCIONARIO ----------")
        print("NOME: ", dados_funcionario["nome"])
        print("CPF: ", dados_funcionario["cpf"])
        print("ID: ", dados_funcionario["id_funcionario"])
        print("CARGO: ", dados_funcionario["cargo"])
        print("SALARIO: ", dados_funcionario["salario"])
        print("PERIODO: ", dados_funcionario["periodo"])
        print("\n")

    def seleciona_funcionario(self) -> str:
        id_funcionario = input("ID do funcionário que deseja selecionar: ")
        while not self.valida_id_funcionario(id_funcionario):
            print("ID inválido. Digite Novamente.")
            id_funcionario = input("id do funcionário que deseja selecionar: ")
        return id_funcionario

    def mostra_mensagem(self, msg: str):
        print(msg)

