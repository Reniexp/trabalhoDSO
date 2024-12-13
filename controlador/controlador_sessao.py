from entidade.sessao import Sessao
from entidade.filme import Filme
from entidade.sala import Sala
from entidade.funcionario import EntidadeFuncionario
from exceptions.NaoFoiPossivelPersistirOsDados import NaoFoiPossivelPersistirOsDados
from tela.tela_sessao import TelaSessao
import pickle
import os
class ControladorSessao:
    def __init__(self, controlador_sistema):
        self.__sessoes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_sessao = TelaSessao()

    def load(self):
        #arq_sessoes = open(os.getcwd()+"\controlador\sessoes.pkl", "rb")
        #sessoes = pickle.load(arq_sessoes)
        #return sessoes
        try:
            with open(os.getcwd()+"\controlador\sessoes.pkl", "rb") as arq_sessoes:
                return pickle.load(arq_sessoes)
        except EOFError:
            return [] 
    
    def dump(self):
        try:
            with open(os.getcwd()+"\controlador\sessoes.pkl", "wb") as arq_sessoes_escrita:
                pickle.dump(self.__sessoes,arq_sessoes_escrita)
        except EOFError:
            raise NaoFoiPossivelPersistirOsDados()

    @property
    def sessoes(self):
        return self.load()

    def abre_tela_sessao(self):
        while True:
            opcao_escolhida = self.__tela_sessao.tela_opcoes_sessao()
            if opcao_escolhida == 1:
                self.lista_sessoes()
            elif opcao_escolhida == 2:
                self.criar_sessao()
            elif opcao_escolhida == 3:
                self.mostrar_dados_sessao()
            elif opcao_escolhida == 4:
                self.editar_sessao()
            elif opcao_escolhida == 5:
                self.excluir_sessao()
            elif opcao_escolhida == 6:
                print("Saindo da Tela de Sessão...")
                break

    def criar_sessao(self):
        print("\n")
        dados = self.__tela_sessao.pega_dados_nova_sessao()
        
        filme = self.__controlador_sistema.pega_filme(dados["idFilme"])
        if filme == -1:
            print("NÃO EXISTE FILME COM ESTE ID, VALOR INVÁLIDO")
            return

        sala = self.__controlador_sistema.pega_sala(dados["idSala"])
        if sala == -1:
            print("NÃO EXISTE SALA COM ESTE ID, VALOR INVÁLIDO")
            return

        funcionario = self.__controlador_sistema.pega_funcionario(dados["idFuncionario"])
        if funcionario is None:
            print("NÃO EXISTE FUNCIONARIO COM ESTE ID, VALOR INVÁLIDO")
            return

        sessaoJaExiste = any(sessao.idSessao == dados["idSessao"] for sessao in self.__sessoes)
        if not sessaoJaExiste:
            nova_sessao = Sessao(
                dados["idSessao"],
                dados["horario"],
                filme,
                sala,
                funcionario
            )
            self.__sessoes.append(nova_sessao)
            self.dump()
    def editar_sessao(self):
        print()
        idSessao = self.__tela_sessao.pega_id_valido_sessao()

        sessao_encontrada = False
        for sessao in self.load():
            if sessao.idSessao == idSessao:
                sessao_encontrada = True
                dados_atualizados = self.__tela_sessao.pega_dados_nova_sessao()
                
                sessao.horario = dados_atualizados["horario"]
                sessao.filme = self.__controlador_sistema.pega_filme(dados_atualizados["idFilme"])
                sessao.sala = self.__controlador_sistema.pega_sala(dados_atualizados["idSala"])
                sessao.funcionario = self.__controlador_sistema.pega_funcionario(dados_atualizados["idFuncionario"])
                print("Sessão atualizada com sucesso!")
                break

        if not sessao_encontrada:
            print("Id inválido, não há sessão com este id")

    def excluir_sessao(self):
        idSessao = self.__tela_sessao.pega_id_valido_sessao()
        
        sessao_encontrada = False
        i = 0
        while i < len(self.__sessoes):
            if self.__sessoes[i].idSessao == idSessao:
                sessao_encontrada = True
                break
            i += 1

        if sessao_encontrada:
            self.__sessoes.pop(i)
            self.dump()
    def lista_sessoes(self):
        if not self.load():
            print("Não há sessão criada ainda")
        else:
            for sessao in self.load():
                print("-----------------------------")
                print(f"IdSessão: {sessao.idSessao}")
                print(f"Horário: {sessao.horario}")
                print(f"Filme: {sessao.filme.titulo}")
                print(f"Sala: {sessao.sala.nomeSala}")
                print(f"Funcionário: {sessao.funcionario.nome}")
                print("-----------------------------")

    def mostrar_dados_sessao(self):
        idSessao = self.__tela_sessao.pega_id_valido_sessao()
        sessoes = self.load()
        sessao_encontrada = next((sessao for sessao in sessoes if sessao.idSessao == idSessao), None)

        if sessao_encontrada:
            print(f"IdSessão: {sessao_encontrada.idSessao}")
            print(f"Horário: {sessao_encontrada.horario}")
            print(f"Filme: {sessao_encontrada.filme.titulo}")
            print(f"Sala: {sessao_encontrada.sala.nomeSala}")
            print(f"Funcionário: {sessao_encontrada.funcionario.nome}")
        else:
            print("Não existe sessão com este id")
