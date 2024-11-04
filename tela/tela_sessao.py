from exceptions.EntradaInvalidaNoPrompt import EntradaInvalidaNoPrompt

class TelaSessao:
    def pega_dados_nova_sessao(self):
        valid_id = False
        id_sessao = input("Id da sessao: ")

        while not valid_id:
            try:
                id_sessao = int(id_sessao)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sessao = input("Id da sessao: ")
                continue
            else:
                valid_id = True

        horario = input("Horario da sessao: ")
        while horario == "":
            print("Não pode ser texto vazio")
            horario = input("Horario da sessao: ")

        valid_id_filme = False
        id_filme = input("Id do filme: ")
        while not valid_id_filme:
            try:
                id_filme = int(id_filme)
            except:
                print("ID É UM VALOR INTEIRO")
                id_filme = input("Id do filme: ")
                continue
            else:
                valid_id_filme = True

        valid_id_sala = False
        id_sala = input("Id da sala: ")
        while not valid_id_sala:
            try:
                id_sala = int(id_sala)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sala = input("Id da sala: ")
                continue
            else:
                valid_id_sala = True

        valid_id_funcionario = False
        id_funcionario = input("Id do funcionario responsavel: ")
        while not valid_id_funcionario:
            try:
                id_funcionario = int(id_funcionario)
            except:
                print("ID É UM VALOR INTEIRO")
                id_funcionario = input("Id do funcionario responsavel: ")
                continue
            else:
                valid_id_funcionario = True

        return {
            "idSessao": id_sessao,
            "idFilme": id_filme,
            "idSala": id_sala,
            "idFuncionario": id_funcionario,
            "horario": horario
        }

    def tela_opcoes_sessao(self) -> int:
        invalidInput = True
        firstTry = True

        while invalidInput:
            if not firstTry:
                print()
                print("ESCOLHA UM INTEIRO VÁLIDO DE 1 A 6")
                print()

            print("Tela Sessao")
            print("\t(1) Mostrar Sessoes Disponíveis")
            print("\t(2) Cadastrar Nova Sessao")
            print("\t(3) Mostrar Dados de Sessao")
            print("\t(4) Alterar Sessao")
            print("\t(5) Deletar Sessao")
            print("\t(6) SAIR da Tela Sessao")
            print()

            opcao_escolhida = input("Escolha uma opcao: ")
            try:
                opcao_escolhida = int(opcao_escolhida)
                if opcao_escolhida not in [1, 2, 3, 4, 5, 6]:
                    raise EntradaInvalidaNoPrompt(opcao_escolhida)
            except:
                firstTry = False
                continue
            else:
                invalidInput = False
        return opcao_escolhida

    def pega_id_valido_sessao(self) -> int:
        valid_id = False
        id_sessao = input("Id da sessao: ")

        while not valid_id:
            try:
                id_sessao = int(id_sessao)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sessao = input("Id da sessao: ")
                continue
            else:
                valid_id = True
        return id_sessao

    def pega_dados_atualizar_sessao(self):
        horario = input("Horario da sessao: ")
        while horario == "":
            print("Não pode ser texto vazio")
            horario = input("Horario da sessao: ")

        valid_id_filme = False
        id_filme = input("Id do filme: ")
        while not valid_id_filme:
            try:
                id_filme = int(id_filme)
            except:
                print("ID É UM VALOR INTEIRO")
                id_filme = input("Id do filme: ")
                continue
            else:
                valid_id_filme = True

        valid_id_sala = False
        id_sala = input("Id da sala: ")
        while not valid_id_sala:
            try:
                id_sala = int(id_sala)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sala = input("Id da sala: ")
                continue
            else:
                valid_id_sala = True

        valid_id_funcionario = False
        id_funcionario = input("Id do funcionario responsavel: ")
        while not valid_id_funcionario:
            try:
                id_funcionario = int(id_funcionario)
            except:
                print("ID É UM VALOR INTEIRO")
                id_funcionario = input("Id do funcionario responsavel: ")
                continue
            else:
                valid_id_funcionario = True

        return {
            "horario": horario,
            "idFilme": id_filme,
            "idSala": id_sala,
            "idFuncionario": id_funcionario,
        }
