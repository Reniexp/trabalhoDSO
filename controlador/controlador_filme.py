from tela.tela_filme import TelaFilme
from entidade.filme import Filme
from exceptions.FilmeNaoEncontrado import FilmeNaoEncontrado
from exceptions.FilmeJaExiste import FilmeJaExiste
from exceptions.OpcaoValida import OpcaoValida

class ControladorFilme:
    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema

    @property
    def filmes(self):
        return self.__filmes

    def pega_filme_por_id(self, id_filme: int):
        for filme in self.__filmes:
            if filme.id_filme == id_filme:
                return filme
        return None
    
    def mostrar_dados_filme(self):
        if not self.__filmes:
            self.__tela_filme.mostra_mensagem("Nenhum filme cadastrado.")
            return

        
        self.listar_filmes()
        id_filme = self.__tela_filme.seleciona_filme()
        if id_filme is None:
            return

        filme = self.pega_filme_por_id(id_filme)

        if filme is not None:
            dados_filme = {
                "id_filme": filme.id_filme,
                "titulo": filme.titulo,
                "duracao": filme.duracaoMinutos,
                "genero": filme.genero,
                "tipo_exibicao": filme.tipoExibicao
            }
            
            self.__tela_filme.mostra_dados_filme(dados_filme)
        else:
            try:
                raise FilmeNaoEncontrado()
            except FilmeNaoEncontrado:
                return

    def incluir_filme(self):
        dados_filme = self.__tela_filme.pega_dados_novo_filme()
        if not dados_filme:
            return

        id_filme = dados_filme["id_filme"]
        filme = self.pega_filme_por_id(id_filme)

        if filme is None:
            novo_filme = Filme(
                dados_filme["id_filme"],
                dados_filme["titulo"],
                dados_filme["duracao"],
                dados_filme["genero"],
                dados_filme["tipo_exibicao"]
            )
            self.__filmes.append(novo_filme)
            self.__tela_filme.mostra_mensagem("Filme incluído com sucesso!")
        else:
            try:
                raise FilmeJaExiste()
            except FilmeJaExiste:
                return

    def alterar_filme(self):
        if not self.__filmes:
            self.__tela_filme.mostra_mensagem("Nenhum filme cadastrado para alterar.")
            return

        self.listar_filmes()
        id_filme = self.__tela_filme.seleciona_filme()
        if id_filme is None:
            return

        filme = self.pega_filme_por_id(id_filme)

        if filme is not None:
            novos_dados_filme = self.__tela_filme.pega_dados_novo_filme()
            if novos_dados_filme is None:
                return

            filme.titulo = novos_dados_filme["titulo"]
            filme.duracaoMinutos = novos_dados_filme["duracao"]
            filme.genero = novos_dados_filme["genero"]
            filme.tipoExibicao = novos_dados_filme["tipo_exibicao"]
            self.__tela_filme.mostra_mensagem("Filme alterado com sucesso!")
        else:
            try:
                raise FilmeNaoEncontrado()
            except FilmeNaoEncontrado:
                return

    def listar_filmes(self):
        if not self.__filmes:
            self.__tela_filme.mostra_mensagem("Nenhum filme cadastrado.")
            try:
                raise FilmeNaoEncontrado()
            except FilmeNaoEncontrado:
                return
        else:
            dados_filmes = [
                {"id_filme": filme.id_filme, "titulo": filme.titulo, "duracao": filme.duracaoMinutos, "genero": filme.genero, "tipo_exibicao": filme.tipoExibicao}
                for filme in self.__filmes
            ]
            self.__tela_filme.mostra_filme(dados_filmes)

    def excluir_filme(self):
        if not self.__filmes:
            self.__tela_filme.mostra_mensagem("Nenhum filme cadastrado para excluir.")
            return

        self.listar_filmes()
        id_filme = self.__tela_filme.seleciona_filme()
        if id_filme is None:
            return

        filme = self.pega_filme_por_id(id_filme)

        if filme is not None:
            self.__filmes.remove(filme)
            self.__tela_filme.mostra_mensagem("Filme excluído com sucesso.")
        else:
            try:
                raise FilmeNaoEncontrado()
            except FilmeNaoEncontrado:
                return

    def retornar(self):
        self.__controlador_sistema.abre_tela_sistema()

    def abre_tela_filme(self):
        while True:
            opcao = self.__tela_filme.tela_opcoes_filme()
            if opcao == 1:
                self.listar_filmes()
            elif opcao == 2:
                self.incluir_filme()
            elif opcao == 3:
                self.mostrar_dados_filme()
            elif opcao == 4:
                self.alterar_filme()
            elif opcao == 5:
                self.excluir_filme()
            elif opcao == 0:
                self.retornar()
                break
            else:
                self.__tela_filme.mostra_mensagem("Opção inválida.")
                try:
                    raise OpcaoValida()
                except OpcaoValida:
                    return
