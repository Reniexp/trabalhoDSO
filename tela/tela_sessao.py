from exceptions.EntradaInvalidaNoPrompt import EntradaInvalidaNoPrompt

class TelaSessao:
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
                if opcao_escolhida not in [1,2,3,4,5,6]:
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
                id_sessao = input("Id do filme: ")
                continue
            else:
                valid_id = True
        return id_sessao
    
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