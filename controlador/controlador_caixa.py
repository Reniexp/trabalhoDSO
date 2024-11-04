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

        id_ingresso = dados_ingresso["id_ingresso"]
        filme = dados_ingresso["filme"]
        sala = dados_ingresso["sala"]
        horario = dados_ingresso["horario"]
        preco = dados_ingresso["preco"]

        ingresso = Ingresso(id_ingresso, filme, sala, horario, preco)

        self.__caixa.registrar_venda(ingresso)

        self.__tela_caixa.mostrar_mensagem(f"Ingresso para '{filme}' vendido com sucesso!")

    def mostrar_total_vendas(self):
        total = self.__caixa.total_vendas
        self.__tela_caixa.mostrar_mensagem(f"Total arrecadado: R$ {total:.2f}")

    def listar_ingressos_vendidos(self):
        if not self.__caixa.ingressos_vendidos:
            self.__tela_caixa.mostrar_mensagem("Nenhum ingresso vendido.")
        else:
            for ingresso in self.__caixa.ingressos_vendidos:
                self.__tela_caixa.mostrar_detalhes_ingresso(ingresso)

    def abre_tela(self):
        while True:
            opcao = self.__tela_caixa.mostrar_opcoes()
            if opcao == 1:
                self.vender_ingresso()
            elif opcao == 2:
                self.mostrar_total_vendas()
            elif opcao == 3:
                self.listar_ingressos_vendidos()
            elif opcao == 0:
                break
            else:
                self.__tela_caixa.mostrar_mensagem("Opção inválida.")

    def obter_relatorios_salas(self):
        salas_com_vendas = dict()
        for venda in self.__caixa.ingressos_vendidos:
            sala = venda.sessao.sala
            salas_com_vendas[sala] = salas_com_vendas.get(sala, 0) + 1

        maior_num_de_vendas = 0
        sala_com_mais_vendas = ""
        for sala,num_vendas in salas_com_vendas.items():
            if num_vendas > maior_num_de_vendas:
                maior_num_de_vendas = num_vendas
                sala_com_mais_vendas = sala
        print(f"Sala {sala_com_mais_vendas} é a que possui mais vendas ({maior_num_de_vendas} assentos vendidos ao todo)")
            