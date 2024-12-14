from entidade.ingresso import Ingresso
from entidade.caixa import Caixa
from tela.tela_caixa import TelaCaixa
from exceptions.ClienteNaoEncontrado import ClienteNaoEncontrado
from exceptions.SessaoNaoEncontrada import SessaoNaoEncontrada
from exceptions.AusenciaDeAssentosDisponiveis import AusenciaDeAssentosDisponiveis
from exceptions.NenhumIngressoVendido import NenhumIngressoVendido
from exceptions.NenhumaSessaoVendida import NenhumaSessaoVendida
import pickle
import os

class ControladorCaixa:
    def __init__(self, controlador_sistema):
        self.__caixa = Caixa()
        self.__tela_caixa = TelaCaixa()
        self.__controlador_sistema = controlador_sistema

    def load(self):
        try:
            with open(os.getcwd().replace("\\", "/") + "/controlador/caixa.pkl", "rb") as arq_caixa:
                return pickle.load(arq_caixa)
        except EOFError:
            return []

    def dump(self):
        try:
            with open(os.getcwd().replace("\\", "/") + "/controlador/caixa.pkl", "wb") as arq_caixa:
                return pickle.dump(self.__caixa.ingressos_vendidos, arq_caixa)
        except EOFError:
            raise NenhumIngressoVendido()

    @property
    def ingressos_vendidos(self):
        return self.load()

    def pegar_ingresso_por_id(self, id_ingresso: int):
        for ingresso in self.load():
            if ingresso.id_ingresso == id_ingresso:
                return ingresso
        return None

    def vender_ingresso(self):
        dados_ingresso = self.__tela_caixa.pegar_dados_ingresso()
        id_sessao = dados_ingresso["sessao"]
        assento = dados_ingresso["assento"]
        id_ingresso = dados_ingresso["id_ingresso"]
        id_cliente = dados_ingresso["id_cliente"]

        sessao = self.__controlador_sistema.obter_sessao_por_id(id_sessao)
        if sessao is None:
            try:
                raise SessaoNaoEncontrada()
            except SessaoNaoEncontrada:
                return

        cliente = self.__controlador_sistema.obter_cliente_por_id(id_cliente)
        if cliente is None:
            try:
                raise ClienteNaoEncontrado()
            except ClienteNaoEncontrado:
                return

        if sessao.assentos_disponiveis <= 0:
            try:
                raise AusenciaDeAssentosDisponiveis
            except AusenciaDeAssentosDisponiveis:
                return

        ingresso = Ingresso(id_ingresso, assento, cliente, sessao)
        self.__caixa.registrar_venda(ingresso)
        sessao.assentos_disponiveis -= 1

        self.__tela_caixa.mostra_mensagem(f"Ingresso para '{sessao.filme.titulo}' vendido com sucesso!")

    def mostrar_total_vendas(self):
        total = self.__caixa.total_vendas
        self.__tela_caixa.mostra_mensagem(f"Total arrecadado: R$ {total:.2f}")

    def listar_ingressos_vendidos(self):
        if not self.__caixa.ingressos_vendidos:
            try:
                raise NenhumIngressoVendido()
            except NenhumIngressoVendido:
                return
        else:
            dados_ingressos = [
                {"id_ingresso": ingresso.id_ingresso, "assento": ingresso.assento, "cliente": ingresso.cliente.nome, "sessao": ingresso.sessao.id_sessao}
                for ingresso in self.__caixa.ingressos_vendidos
            ]
            self.__tela_caixa.mostrar_detalhes_ingresso(dados_ingressos)

    def obter_sessoes_populares(self):
        sessoes_com_vendas = dict()

        for venda in self.__caixa.ingressos_vendidos:
            sessao = venda.sessao
            sessoes_com_vendas[sessao] = sessoes_com_vendas.get(sessao, 0) + 1

        maior_num_de_vendas = 0
        sessao_popular = None
        for sessao, num_vendas in sessoes_com_vendas.items():
            if num_vendas > maior_num_de_vendas:
                maior_num_de_vendas = num_vendas
                sessao_popular = sessao

        if sessao_popular:
            self.__tela_caixa.mostra_mensagem(f"A sessão mais popular tem como id: {sessao_popular.id_sessao} com {maior_num_de_vendas} ingressos vendidos.")
        else:
            try:
                raise NenhumaSessaoVendida()
            except NenhumaSessaoVendida:
                return

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
            self.__tela_caixa.mostra_mensagem(f"O filme mais assistido é: '{filme_popular.titulo}' com {maior_num_de_vendas} ingressos vendidos.")
        else:
            try:
                raise NenhumIngressoVendido()
            except NenhumIngressoVendido:
                return

    def abre_tela_caixa(self):
        while True:
            opcao = self.__tela_caixa.tela_opcoes_caixa()
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
                self.__tela_caixa.mostra_mensagem("Opção inválida.")

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
        self.__tela_caixa.mostra_mensagem(f"Sala {sala_com_mais_vendas} é a que possui mais vendas ({maior_num_de_vendas} assentos vendidos ao todo)")
