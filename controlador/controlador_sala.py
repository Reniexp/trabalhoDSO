from tela.tela_sala import TelaSala
from entidade.sala import Sala
from exceptions.OpcaoValida import OpcaoValida
from exceptions.SalaNaoEncontrada import SalaNaoEncontrada
from exceptions.SalaJaExiste import SalaJaExiste
from exceptions.NaoFoiPossivelPersistirOsDados import NaoFoiPossivelPersistirOsDados
from DAOs.sala_dao import SalaDAO
import pickle
import os

class ControladorSala:
    def __init__(self, controlador_sistema):
        self.__tela_sala = TelaSala()
        self.__salas_DAO = SalaDAO(os.getcwd().replace("\\","/")+"/controlador/salas.pkl")
        self.__controlador_sistema = controlador_sistema

    @property
    def salas(self):
        return self.__salas_DAO.get_all()

    def pega_sala_pelo_id(self, id_sala: int):
        for sala in self.__salas_DAO.get_all():
            if sala.id_sala == id_sala:
                return sala
        return None

    def mostrar_dados_sala(self):
        if len(self.__salas_DAO.get_all()) == 0:
            self.__tela_sala.mostra_mensagem("Nenhuma sala cadastrada.")
            return

        self.lista_salas()
        id_sala = self.__tela_sala.seleciona_sala()
        if id_sala is None:
            return

        sala = self.pega_sala_pelo_id(id_sala)

        if sala is not None:
            dados_sala = {
                "id_sala": sala.id_sala,
                "nome_sala": sala.nome_sala,
                "capacidade": sala.capacidade
            }
            self.__tela_sala.mostra_dados_sala(dados_sala)
        else:
            try:
                raise SalaNaoEncontrada()
            except SalaNaoEncontrada:
                return
            
    def cadastrar_sala(self):
        dados_sala = self.__tela_sala.pega_dados_nova_sala()
        if not dados_sala:
            return
        
        id_sala = dados_sala["id_sala"]
        sala = self.pega_sala_pelo_id(id_sala)

        if sala is None:
            nova_sala = Sala(
                dados_sala["id_sala"],
                dados_sala["nome_sala"],
                dados_sala["capacidade"]
            )
            self.__salas_DAO.add(nova_sala)
            self.__tela_sala.mostra_mensagem("Sala criada com sucesso!")
        else:
            try:
                raise SalaJaExiste()
            except SalaJaExiste:
                return


    def alterar_sala(self):
        if len(self.__salas_DAO.get_all()) == 0:
            self.__tela_sala.mostra_mensagem("Nenhuma sala cadastrada para alterar.")
            return

        self.lista_salas()
        id_sala = self.__tela_sala.seleciona_sala()
        if id_sala is None:
            return

        sala = self.pega_sala_pelo_id(id_sala)

        if sala is not None:
            dados_alterados_sala = self.__tela_sala.pega_dados_atualizar_sala()

            sala.capacidade = dados_alterados_sala["capacidade"]
            sala.nome_sala = dados_alterados_sala["nome_sala"]

            self.__tela_sala.mostra_mensagem("Sala atualizada com sucesso.")
        else:
            try:
                raise SalaNaoEncontrada()
            except SalaNaoEncontrada:
                return
            
    def lista_salas(self):
        if len(self.__salas_DAO.get_all()) == 0:
            self.__tela_sala.mostra_mensagem("Nenhuma sala cadastrada.")
            try:
                raise SalaNaoEncontrada()
            except SalaNaoEncontrada:
                return    
        
        else:
            dados_salas = [
                {
                    "id_sala": sala.id_sala,
                    "nome_sala": sala.nome_sala,
                    "capacidade": sala.capacidade
                } for sala in self.__salas_DAO.get_all()
            ]
            self.__tela_sala.mostra_sala(dados_salas)

    def excluir_sala(self):
        if len(self.__salas_DAO.get_all()) == 0:
            self.__tela_sala.mostra_mensagem("Nenhuma sala cadastrada para excluir.")
            return

        self.lista_salas()
        id_sala = self.__tela_sala.seleciona_sala()
        if id_sala is None:
            return

        sala = self.pega_sala_pelo_id(id_sala)

        if sala is not None:
            self.__salas_DAO.remove(sala)
            self.__tela_sala.mostra_mensagem("Sala excluída com sucesso.")
        else:
            try:
                self.__tela_sala.mostra_mensagem("Sala kkkk com sucesso.")
                raise SalaNaoEncontrada()
            except SalaNaoEncontrada:
                return
            
    def retornar(self):
        self.__controlador_sistema.abre_tela_sistema()

    def abre_tela_sala(self):
        while True:
            opcao = self.__tela_sala.tela_opcoes_sala()
            if opcao == 1:
                self.lista_salas()
            elif opcao == 2:
                self.cadastrar_sala()
            elif opcao == 3:
                self.mostrar_dados_sala()
            elif opcao == 4:
                self.alterar_sala()
            elif opcao == 5:
                self.excluir_sala()
            elif opcao == 0:
                self.retornar()
                break
            else:
                self.__tela_sala.mostra_mensagem("Opção inválida.")
                try:
                    raise OpcaoValida()
                except OpcaoValida:
                    return

                
    def existe_sala(self):
        return bool(self.lista_salas)