from entidade.ingresso import Ingresso
from entidade.caixa import Caixa
from tela.tela_caixa import TelaCaixa

class ControladorCaixa:
    def __init__(self, controlador_sistema):
        self.__caixa = Caixa()
        self.__tela_caixa = TelaCaixa()
        self.__controlador_sistema = controlador_sistema

    def vender_ingresso(self):
        dados_ingresso = self.__tela_caixa.pegar_dados_ingresso()
        id_sessao = dados_ingresso["sessao"]
        assento = dados_ingresso["assento"]
        id_ingresso = dados_ingresso["id_ingresso"]
        id_cliente = dados_ingresso["id_cliente"]

        sessao = self.__controlador_sistema.obter_sessao_por_id(id_sessao)
        if sessao is None:
            self.__tela_caixa.mostrar_mensagem("Sessão não encontrada ou indisponível.")
            return
        
        cliente = self.__controlador_sistema.obter_cliente_por_id(id_cliente)
        if cliente is None:
            self.__tela_caixa.mostrar_mensagem("Cliente não encontrado ou indisponível")
            return

        if sessao.assentos_disponiveis <= 0:
            self.__tela_caixa.mostrar_mensagem("Não há assentos disponíveis nesta sessão.")
            return

        ingresso = Ingresso(id_ingresso,assento,cliente,sessao)
        
        self.__caixa.registrar_venda(ingresso)
        sessao.assentos_disponiveis -= 1  # Reduzir a quantidade de assentos disponíveis

        self.__tela_caixa.mostrar_mensagem(f"Ingresso para '{sessao.filme.titulo}' vendido com sucesso!")

    def mostrar_total_vendas(self):
        total = self.__caixa.total_vendas
        self.__tela_caixa.mostrar_mensagem(f"Total arrecadado: R$ {total:.2f}")

    def listar_ingressos_vendidos(self):
        if not self.__caixa.ingressos_vendidos:
            self.__tela_caixa.mostrar_mensagem("Nenhum ingresso vendido.")
        else:
            for ingresso in self.__caixa.ingressos_vendidos:
                self.__tela_caixa.mostrar_detalhes_ingresso(ingresso)

    def obter_sessoes_populares(self):
        sessoes_com_vendas = dict()
        
        # Contar ingressos vendidos por sessão
        for venda in self.__caixa.ingressos_vendidos:
            sessao = venda.sessao
            sessoes_com_vendas[sessao] = sessoes_com_vendas.get(sessao, 0) + 1

        # Determinar a sessão mais popular
        maior_num_de_vendas = 0
        sessao_popular = None
        for sessao, num_vendas in sessoes_com_vendas.items():
            if num_vendas > maior_num_de_vendas:
                maior_num_de_vendas = num_vendas
                sessao_popular = sessao
        
        if sessao_popular:
            print(f"A sessão mais popular é: {sessao_popular} com {maior_num_de_vendas} ingressos vendidos.")
        else:
            print("Nenhuma sessão foi vendida.")

    def obter_filmes_populares(self):
        filmes_com_vendas = dict()

        
        for venda in self.__caixa.ingressos_vendidos:
            filme = venda.sessao.filme
            filmes_com_vendas[filme] = filmes_com_vendas.get(filme, 0) + 1

        
        maior_num_de_vendas = 0
        filme_popular = None
        for filme, num_vendas in filmes_com_vendas.items():
            if num_vendas > maior_num_de_vendas:
                maior_num_de_vendas = num_vendas
                filme_popular = filme

        if filme_popular:
            print(f"O filme mais assistido é: '{filme_popular.titulo}' com {maior_num_de_vendas} ingressos vendidos.")
        else:
            print("Nenhum ingresso foi vendido.")

    def abre_tela(self):
        while True:
            opcao = self.__tela_caixa.mostrar_opcoes()
            if opcao == 1:
                self.vender_ingresso()
            elif opcao == 2:
                self.mostrar_total_vendas()
            elif opcao == 3:
                self.listar_ingressos_vendidos()
            elif opcao == 4:
                self.obter_sessoes_populares()
            elif opcao == 5:
                self.obter_filmes_populares()
            elif opcao == 0:
                break
            else:
                self.__tela_caixa.mostrar_mensagem("Opção inválida.")

    def obter_relatorios_salas(self):
        salas_com_vendas = dict()
        for venda in self.__caixa.ingressos_vendidos:
            sala = venda.sala
            salas_com_vendas[sala] = salas_com_vendas.get(sala, 0) + 1

        maior_num_de_vendas = 0
        sala_com_mais_vendas = ""
        for sala, num_vendas in salas_com_vendas.items():
            if num_vendas > maior_num_de_vendas:
                maior_num_de_vendas = num_vendas
                sala_com_mais_vendas = sala
        print(f"Sala {sala_com_mais_vendas} é a que possui mais vendas ({maior_num_de_vendas} assentos vendidos ao todo)")
