from tela.tela_sessao import TelaSessao
from entidade.sessao import Sessao
from exceptions.SessaoNaoEncontrada import SessaoNaoEncontrada
from exceptions.SessaoJaExiste import SessaoJaExiste
from exceptions.OpcaoValida import OpcaoValida
from exceptions.NaoFoiPossivelPersistirOsDados import NaoFoiPossivelPersistirOsDados
import pickle
import os

class ControladorSessao:
    def __init__(self, controlador_sistema):
        self.__sessoes = self.load()
        self.__controlador_sistema = controlador_sistema
        self.__tela_sessao = TelaSessao()

    def load(self):
        try:
            with open(os.getcwd().replace("\\","/")+"/controlador/sessoes.pkl", "rb") as arq_sessoes:
                return pickle.load(arq_sessoes)
        except EOFError:
            return []

    def dump(self):
        try:
            with open(os.getcwd().replace("\\","/")+"/controlador/sessoes.pkl", "wb") as arq_sessoes_escrita:
                pickle.dump(self.__sessoes,arq_sessoes_escrita)
        except EOFError:
            raise NaoFoiPossivelPersistirOsDados()

    @property
    def sessoes(self):
        return self.load()

    def pega_sessao_por_id(self, id_sessao: int):
        for sessao in self.load():
            if sessao.id_sessao == id_sessao:
                return sessao
        return None

    def mostrar_dados_sessao(self):
        if not self.load():
            self.__tela_sessao.mostra_mensagem("Nenhuma sessão cadastrada.")
            return

        self.listar_sessoes()
        id_sessao = self.__tela_sessao.seleciona_sessao()
        if id_sessao is None:
            return

        sessao = self.pega_sessao_por_id(id_sessao)

        if sessao is not None:
            dados_sessao = {
                "id_sessao": sessao.id_sessao,
                "horario": sessao.horario,
                "filme": sessao.filme.titulo,
                "sala": sessao.sala.numero,
                "funcionario": sessao.funcionario.nome
            }
            self.__tela_sessao.mostra_dados_sessao(dados_sessao)
        else:
            try:
                raise SessaoNaoEncontrada()
            except SessaoNaoEncontrada:
                return

    def incluir_sessao(self):
        dados_sessao = self.__tela_sessao.pega_dados_nova_sessao()
        if not dados_sessao:
            return

        id_sessao = dados_sessao["id_sessao"]
        sessao = self.pega_sessao_por_id(id_sessao)

        if sessao is None:
            filme = self.__controlador_sistema.pega_filme(dados_sessao["id_filme"])
            sala = self.__controlador_sistema.pega_sala(dados_sessao["id_sala"])
            funcionario = self.__controlador_sistema.pega_funcionario(dados_sessao["id_funcionario"])

            if filme and sala and funcionario:
                nova_sessao = Sessao(
                    dados_sessao["id_sessao"],
                    dados_sessao["horario"],
                    filme,
                    sala,
                    funcionario
                )
                self.__sessoes.append(nova_sessao)
                self.dump()
                self.__tela_sessao.mostra_mensagem("Sessão incluída com sucesso!")
            else:
                self.__tela_sessao.mostra_mensagem("Dados inválidos. Verifique as IDs informadas.")
        else:
            try:
                raise SessaoJaExiste()
            except SessaoJaExiste:
                return

    def alterar_sessao(self):
        if not self.__sessoes:
            self.__tela_sessao.mostra_mensagem("Nenhuma sessão cadastrada para alterar.")
            return

        self.listar_sessoes()
        id_sessao = self.__tela_sessao.seleciona_sessao()
        if id_sessao is None:
            return

        sessao = self.pega_sessao_por_id(id_sessao)

        if sessao is not None:
            novos_dados_sessao = self.__tela_sessao.pega_dados_nova_sessao()
            if novos_dados_sessao is None:
                return

            sessao.horario = novos_dados_sessao["horario"]
            sessao.filme = self.__controlador_sistema.pega_filme(novos_dados_sessao["id_filme"])
            sessao.sala = self.__controlador_sistema.pega_sala(novos_dados_sessao["id_sala"])
            sessao.funcionario = self.__controlador_sistema.pega_funcionario(novos_dados_sessao["id_funcionario"])
            self.__tela_sessao.mostra_mensagem("Sessão alterada com sucesso!")
        else:
            try:
                raise SessaoNaoEncontrada()
            except SessaoNaoEncontrada:
                return

    def listar_sessoes(self):
        if not self.load():
            self.__tela_sessao.mostra_mensagem("Nenhuma sessão cadastrada.")
            try:
                raise SessaoNaoEncontrada()
            except SessaoNaoEncontrada:
                return
        else:
            dados_sessoes = [
                {
                    "id_sessao": sessao.id_sessao,
                    "horario": sessao.horario,
                    "filme": sessao.filme.titulo,
                    "sala": sessao.sala.numero,
                    "funcionario": sessao.funcionario.nome
                }
                for sessao in self.__sessoes
            ]
            self.__tela_sessao.mostra_sessoes(dados_sessoes)

    def excluir_sessao(self):
        if not self.load():
            self.__tela_sessao.mostra_mensagem("Nenhuma sessão cadastrada para excluir.")
            return

        self.listar_sessoes()
        id_sessao = self.__tela_sessao.seleciona_sessao()
        if id_sessao is None:
            return

        sessao = self.pega_sessao_por_id(id_sessao)

        if sessao is not None:
            self.__sessoes.remove(sessao)
            self.dump()
            self.__tela_sessao.mostra_mensagem("Sessão excluída com sucesso.")
        else:
            try:
                raise SessaoNaoEncontrada()
            except SessaoNaoEncontrada:
                return

    def retornar(self):
        self.__controlador_sistema.abre_tela_sistema()

    def abre_tela_sessao(self):
        while True:
            opcao = self.__tela_sessao.tela_opcoes_sessao()
            if opcao == 1:
                self.listar_sessoes()
            elif opcao == 2:
                self.incluir_sessao()
            elif opcao == 3:
                self.mostrar_dados_sessao()
            elif opcao == 4:
                self.alterar_sessao()
            elif opcao == 5:
                self.excluir_sessao()
            elif opcao == 0:
                self.retornar()
                break
            else:
                self.__tela_sessao.mostra_mensagem("Opção inválida.")
                try:
                    raise OpcaoValida()
                except OpcaoValida:
                    return
