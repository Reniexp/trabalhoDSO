from tela.tela_sala import TelaSala
from entidade.sala import Sala
import pickle

class ControladorSala():
    def __init__(self, controlador_sistema):
        self.__telaSala = TelaSala()
        self.__salas = []
        self.__controlador_sistema = controlador_sistema

    def load(self):
        arq_salas = open('salas.pkl', "rb")
        salas = pickle.load(arq_salas)
        return salas
    
    def dump(self):
        arq_salas_escrita = open('salas.pkl', "wb")
        pickle.dump(self.__salas,arq_salas_escrita)

    def abre_tela_sala(self):
        opcao_escolhida = 0
        while opcao_escolhida != 6:
            opcao_escolhida = self.__telaSala.tela_opcoes_sala()
            if opcao_escolhida == 1:
                self.lista_salas()
            elif opcao_escolhida == 2:
                self.cadastrar_sala()
            elif opcao_escolhida == 3:
                self.mostrar_dados_sala()
            elif opcao_escolhida == 4:
                self.altera_sala()
            elif opcao_escolhida == 5:
                self.excluir_sala()
    
    def cadastrar_sala(self):
        dados_nova_sala = self.__telaSala.pega_dados_nova_sala()

        idSala = dados_nova_sala["idSala"]
        nomeSala = dados_nova_sala["nomeSala"]
        capacidade = dados_nova_sala["capacidade"]

        salaJaExiste = False
        for sala in self.load():
            if sala.idSala:
                salaJaExiste = True
                break
        print()
        if not salaJaExiste:
            self.__salas.append(
                Sala(
                    idSala,
                    nomeSala,
                    capacidade
                )
            )
            self.dump()

    def excluir_sala(self):
        idSala = self.__telaSala.pega_id_valido_sala()
        
        sala_encontrada = False

        i = 0
        while i < len(self.__salas):
            sala = self.__salas[i]
            if sala.idSala == idSala:
                sala_encontrada = True
                break
            i += 1

        print()       
        if sala_encontrada:
            self.__salas.pop(i)
            self.dump()

    def lista_salas(self):
        if len(self.__salas) == 0:
            print()
            print("Não há sala criada ainda")
            print()
        else:
            for sala in self.__salas:
                print("-----------------------------")
                print("IdSala: ",sala.idSala)
                print("Nome da Sala: ",sala.nomeSala)
                print("Capacidade da sala: ",sala.capacidade)
                print("-----------------------------")
                print()
        
    def mostrar_dados_sala(self):
        print()
        id_sala = self.__telaSala.pega_id_valido_sala()
        
        salaAchada = False
        arq_salas = open('salas.pkl', "rb")
        salas = pickle.load(arq_salas)
        for sala in salas:
            if sala.idSala == id_sala:
                print("IdSala: ", id_sala)
                print("Nome da Sala: ", sala.nomeSala)
                print("Capacidade: ", sala.capacidade)

                salaAchada = True
                break
        if not salaAchada:
            print()
            print("Não existe sala com este id")
        
        print("")

    def altera_sala(self):
        print()
        idSala = self.__telaSala.pega_id_valido_sala()

        for sala in self.load():
            if sala.idSala == idSala:
                sala_encontrada = True
                
                dados_alterados_da_sala = self.__telaSala.pega_dados_atualizar_sala()

                sala.capacidade = dados_alterados_da_sala["capacidade"]
                sala.nomeSala = dados_alterados_da_sala["nomeSala"]

    def pega_sala_pelo_id(self,id_sala:int):
        for sala in self.load():
            if sala.idSala == id_sala:
                return sala
        return -1
    
    def existe_sala(self):
        return len(self.__salas) > 0