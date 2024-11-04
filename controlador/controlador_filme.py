from tela.tela_filme import TelaFilme
from entidade.filme import Filme

class ControladorFilme():
    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__telaFilme = TelaFilme()
        self.__controlador_sistema = controlador_sistema


    def abre_tela_filme(self):
        opcao_escolhida = 0
        while opcao_escolhida != 6:
            opcao_escolhida = self.__telaFilme.tela_opcoes_filme()
            if opcao_escolhida == 1:
                self.lista_filmes()
            elif opcao_escolhida == 2:
                self.incluir_filme()
            elif opcao_escolhida == 3:
                self.mostrar_dados_filme()
            elif opcao_escolhida == 4:
                self.altera_filme()
            elif opcao_escolhida == 5:
                self.excluir_filme()

    def incluir_filme(self):
        dados_do_novo_filme = self.__telaFilme.pega_dados_novo_filme()

        print("\n")

        idFilme = dados_do_novo_filme["idFilme"]
        titulo = dados_do_novo_filme["titulo"]
        duracaoMinutos = dados_do_novo_filme["duracaoMinutos"]
        genero = dados_do_novo_filme["genero"]
        tipoExibicao = dados_do_novo_filme["tipoExibicao"]
        
        filmeJaExiste = False
        for filme in self.__filmes:
            if filme.idFilme == idFilme and filme.titulo == titulo and filme.duracaoMinutos == duracaoMinutos and filme.genero == genero and filme.tipoExibicao == tipoExibicao:
                filmeJaExiste = True
        
        if not filmeJaExiste:
            self.__filmes.append(
            Filme(
                    idFilme,
                    titulo,
                    duracaoMinutos,
                    genero,
                    tipoExibicao
                )
            )
        print("Filme criado com sucesso!")
        print(self.__filmes[0].titulo)

    def mostrar_dados_filme(self):
        print()
        id_filme = self.__telaFilme.pega_id_valido_filme()
        
        filmeAchado = False
        for filme in self.__filmes:
            if filme.idFilme == id_filme:
                print("Titulo: ", filme.titulo)
                print("Duracao Em Minutos: ", filme.duracaoMinutos)

                genero = ""
                if filme.genero == 1:
                    genero = "acao"
                elif filme.genero == 2:
                    genero = "comedia"
                elif filme.genero == 3:
                    genero = "romance"
                elif filme.genero == 4:
                    genero = "ficcao cientifica"

                print("Genero: ", genero)
                
                tipo_de_exibicao = ""
                if filme.tipoExibicao == 1:
                    tipo_de_exibicao = "dublado"
                elif filme.tipoExibicao == 2:
                    tipo_de_exibicao = "legendado"
                elif filme.tipoExibicao == 3:
                    tipo_de_exibicao = "dublado e legendado"

                print("Tipo de Exibicao: ", tipo_de_exibicao)

                filmeAchado = True
                break
        if not filmeAchado:
            print()
            print("Não existe filme com este id")
        
        print("")

    def altera_filme(self):
        print()
        idFilme = self.__telaFilme.pega_id_valido_filme()

        filme_encontrado = False

        for filme in self.__filmes:
            if filme.idFilme == idFilme:
                filme_encontrado = True
                
                dados_alterados_do_filme = self.__telaFilme.pega_dados_atualizar_filme()

                filme.titulo = dados_alterados_do_filme["titulo"]
                filme.duracaoMinutos = dados_alterados_do_filme["duracaoMinutos"]
                filme.genero = dados_alterados_do_filme["genero"]
                filme.tipoExibicao = dados_alterados_do_filme["tipoExibicao"]
        print()
        if not filme_encontrado:
            print("Id inválido, não há filme com este id")
        else:
            print("Filme altualizado! com sucesso!")
        print()

    def excluir_filme(self):
        idFilme = self.__telaFilme.pega_id_valido_filme()
        
        filme_encontrado = False

        i = 0
        while i < len(self.__filmes):
            filme = self.__filmes[i]
            if filme.idFilme == idFilme:
                filme_encontrado = True
                break
            i += 1

        print()       
        if filme_encontrado:
            self.__filmes.pop(i)
            print("Filme deletado com sucesso!")
        else:
            print("Id inválido, não há filme com este id")
        print()
    
    def lista_filmes(self):
        if len(self.__filmes) == 0:
            print()
            print("Não há filme criado ainda")
            print()
        else:
            for filme in self.__filmes:
                print("-----------------------------")
                print("IdFilme: ",filme.idFilme)
                print("Titulo: ",filme.titulo)
                print("Duracao Em Minutos: ",filme.duracaoMinutos)
                tipo_de_exibicao = ""
                if filme.tipoExibicao == 1:
                    tipo_de_exibicao = "dublado"
                elif filme.tipoExibicao == 2:
                    tipo_de_exibicao = "legendado"
                elif filme.tipoExibicao == 3:
                    tipo_de_exibicao = "dublado e legendado"

                print("Tipo de Exibicao: ", tipo_de_exibicao)

                genero = ""
                if filme.genero == 1:
                    genero = "acao"
                elif filme.genero == 2:
                    genero = "comedia"
                elif filme.genero == 3:
                    genero = "romance"
                elif filme.genero == 4:
                    genero = "ficcao cientifica"
                    
                print("Genero: ", genero)
                print("-----------------------------")
                print()
