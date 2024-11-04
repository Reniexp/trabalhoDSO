from entidade.sessao import Sessao
from entidade.filme import Filme
from entidade.sala import Sala
from entidade.funcionario import EntidadeFuncionario


class ControladorSessao:
    def __init__(self, controlador_sistema):
        self.__sessoes = []
        self.__controlador_sistema = controlador_sistema


    def criar_sessao(self, idSessao: int, horario: str, id_filme: int, id_sala: int, id_funcionario_responsavel: int):
        print("\n")

        filme = self.__controlador_sistema.pega_filme(id_filme)
        if filme == -1 :
            print()
            print("NÃO EXISTE FILME COM ESTE ID, VALOR INVÁLIDO")
            print()
            return

        sala = self.__controlador_sistema.pega_sala(id_sala)
        if filme == -1 :
            print()
            print("NÃO EXISTE SALA COM ESTE ID, VALOR INVÁLIDO")
            print()
            return
        
        funcionario = self.__controlador_sistema.pega_funcionario(id_funcionario_responsavel)
        if filme == None :
            print()
            print("NÃO EXISTE FUNCIONARIO COM ESTE ID, VALOR INVÁLIDO")
            print()
            return
        
        sessaoJaExiste = False
        for sessao in self.__sessoes:
            if sessao.idSessao == idSessao:
                sessaoJaExiste = True
        
        if not sessaoJaExiste:
            self.__sessoes.append(
            Sessao(
                    idSessao,
                    horario,
                    filme,
                    sala,
                    funcionario,
                )
            )
        print("Sessão criada com sucesso!")
        print(self.__sessoes[0].idSessao)
    
    def editar_sessao(self,idSessao:int, horario: str, filme: Filme, sala: Sala, funcionario_responsavel: EntidadeFuncionario):
        print()

        sessao_encontrada = False

        for sessao in self.__sessoes:
            if sessao.idSessao == idSessao:
                sessao_encontrada = True
                
                sessao.horario = horario
                sessao.filme = filme
                sessao.sala = sala
                sessao.funcionario = funcionario_responsavel
        print()
        if not sessao_encontrada:
            print("Id inválido, não há sessão com este id")
        else:
            print("Sessão altualizada com sucesso!")
        print()

    def excluir_sessao(self, idSessao: int):
        sessao_encontrada = False

        i = 0
        while i < len(self.__sessoes):
            sessao = self.__sessoes[i]
            if sessao.idSessao == idSessao:
                sessao_encontrada = True
                break
            i += 1

        print()       
        if sessao_encontrada:
            self.__sessoes.pop(i)
            print("Sessão deletado com sucesso!")
        else:
            print("Id inválido, não há sessão com este id")
        print()
    
    def lista_sessoes(self):
        if len(self.__sessoes) == 0:
            print()
            print("Não há sessão criada ainda")
            print()
        else:
            for sessao in self.__sessoes:
                print("-----------------------------")
                print("IdSessão: ",sessao.idSessao)
                print("Horário: ",sessao.horario)
                print("Filme: ",sessao.filme.titulo)
                print("Sala: ",sessao.sala.nomeSala)
                print("-----------------------------")
                print()

