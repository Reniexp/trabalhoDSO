class TelaFilme():
    def tela_opcoes_filme(self) -> int:
        invalidInput = True
        firstTry = True

        while invalidInput:
            if not firstTry:
                print("ESCOLHA UM INTEIRO VÁLIDO")
            print("Tela filme")
            print("\t(1) Mostrar Filmes Disponíveis")
            print("\t(2) Cadastrar Novo Filme")
            print("\t(3) Mostrar Dados de Filme")
            print("\t(4) Alterar Filme")
            print("\t(5) Deletar Filme")
            print("\t(6) SAIR da Tela Filme")
            print()
            
            opcao_escolhida = input("Escolha uma opcao: ")
            try:
                opcao_escolhida = int(opcao_escolhida)
            except:
                firstTry = False
                continue
            else:
                invalidInput = False
        return opcao_escolhida
    
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


        

        