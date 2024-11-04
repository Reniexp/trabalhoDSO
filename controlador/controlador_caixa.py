from entidade.ingresso import Ingresso
from entidade.caixa import Caixa
from tela.tela_caixa import TelaCaixa

class ControladorCaixa:
    def __init__(self, controlador_sistema):
        self.__caixa = Caixa()
        self.__tela_caixa = TelaCaixa()
        self.__controlador_sistema = controlador_sistema

    def vender_ingresso(self):
        # Obter o ID da sessão a partir da entrada do usuário
        id_sessao = int(input("Digite o ID da sessão: "))

        # Verificar se a sessão correspondente ao ID está disponível
        sessao = self.__controlador_sistema.obter_sessao_por_id(id_sessao)
        if sessao is None:
            self.__tela_caixa.mostrar_mensagem("Sessão não encontrada ou indisponível.")
            return

        # Verificar a disponibilidade de assentos
        if sessao.sala.assentos_disponiveis <= 0:
            self.__tela_caixa.mostrar_mensagem("Não há assentos disponíveis nesta sessão.")
            return

        # Criar o ingresso e registrar a venda
        id_ingresso = len(self.__caixa.ingressos_vendidos) + 1  # Geração simples de ID
        ingresso = Ingresso(id_ingresso, sessao.filme, sessao.sala, sessao.horario, sessao.filme.preco)
        
        # Registrar a venda e atualizar os assentos disponíveis
        self.__caixa.registrar_venda(ingresso)
        sessao.sala.assentos_disponiveis -= 1  # Reduzir a quantidade de assentos disponíveis

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
            sala = venda.sala
            salas_com_vendas[sala] = salas_com_vendas.get(sala, 0) + 1

        maior_num_de_vendas = 0
        sala_com_mais_vendas = ""
        for sala, num_vendas in salas_com_vendas.items():
            if num_vendas > maior_num_de_vendas:
                maior_num_de_vendas = num_vendas
                sala_com_mais_vendas = sala
        print(f"Sala {sala_com_mais_vendas} é a que possui mais vendas ({maior_num_de_vendas} assentos vendidos ao todo)")
