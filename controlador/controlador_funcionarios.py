from entidade.funcionario import EntidadeFuncionario
from tela.tela_funcionario import TelaFuncionario
from exceptions.NaoFoiPossivelPersistirOsDados import NaoFoiPossivelPersistirOsDados
from DAOs.funcionario_dao import FuncionarioDAO
import pickle
import os

class ControladorFuncionarios:
    def __init__(self, controlador_sistema):
        self.__funcionarios_DAO = FuncionarioDAO(os.getcwd().replace("\\","/")+"/controlador/funcionarios.pkl")
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema

    def pega_funcionario_por_id(self, id_funcionario: int):
        for funcionario in self.__funcionarios_DAO.get_all():
            if funcionario.id_funcionario == id_funcionario:
                return funcionario
        return None

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        if not dados_funcionario:
            return

        id_funcionario = dados_funcionario["id_funcionario"]
        funcionario = self.pega_funcionario_por_id(id_funcionario)

        if funcionario is None:
            funcionario = EntidadeFuncionario(
                dados_funcionario["cpf"],
                dados_funcionario["id_funcionario"],
                dados_funcionario["nome"],
                dados_funcionario["cargo"],
                dados_funcionario["salario"],
                dados_funcionario["periodo"]
            )
            self.__funcionarios_DAO.add(funcionario)
            self.__tela_funcionario.mostra_mensagem("Funcionário incluído com sucesso.")
        else:
            self.__tela_funcionario.mostra_mensagem(f"Funcionário com ID {id_funcionario} já existe.")

    def alterar_funcionario(self):
        if  len(self.__funcionarios_DAO.get_all()) == 0:
            self.__tela_funcionario.mostra_mensagem("Nenhum funcionário cadastrado para alterar.")
            return

        self.lista_funcionarios()
        id_funcionario = self.__tela_funcionario.seleciona_funcionario()
        if id_funcionario is None:
            return

        funcionario = self.pega_funcionario_por_id(id_funcionario)

        if funcionario is not None:
            novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            if novos_dados_funcionario is None:
                return

            funcionario.nome = novos_dados_funcionario["nome"]
            funcionario.cpf = novos_dados_funcionario["cpf"]
            funcionario.id_funcionario = novos_dados_funcionario["id_funcionario"]
            funcionario.cargo = novos_dados_funcionario["cargo"]
            funcionario.salario = novos_dados_funcionario["salario"]
            funcionario.periodo = novos_dados_funcionario["periodo"]

            self.__tela_funcionario.mostra_mensagem("Funcionário atualizado com sucesso.")
        else:
            self.__tela_funcionario.mostra_mensagem("Funcionário não encontrado.")

    def lista_funcionarios(self):
        if  len(self.__funcionarios_DAO.get_all()) == 0:
            self.__tela_funcionario.mostra_mensagem("Nenhum funcionário cadastrado.")
        else:
            dados_funcionarios = [
                {
                    "nome": func.nome,
                    "cpf": func.cpf,
                    "id_funcionario": func.id_funcionario,
                    "cargo": func.cargo,
                    "salario": func.salario,
                    "periodo": func.periodo
                } for func in self.__funcionarios_DAO.get_all()
            ]
            self.__tela_funcionario.mostra_funcionarios(dados_funcionarios)

    def excluir_funcionario(self):
        if len(self.__funcionarios_DAO.get_all()) == 0:
            self.__tela_funcionario.mostra_mensagem("Nenhum funcionário cadastrado para excluir.")
            return

        self.lista_funcionarios()
        id_funcionario = self.__tela_funcionario.seleciona_funcionario()
        if id_funcionario is None:
            return

        funcionario = self.pega_funcionario_por_id(id_funcionario)

        if funcionario is not None:
            self.__funcionarios_DAO.remove(funcionario)
            self.__tela_funcionario.mostra_mensagem("Funcionário excluído com sucesso.")
        else:
            self.__tela_funcionario.mostra_mensagem("Funcionário não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela_sistema()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_funcionario,
            2: self.alterar_funcionario,
            3: self.lista_funcionarios,
            4: self.excluir_funcionario,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_funcionario.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
                if opcao == 0:
                    break
            else:
                self.__tela_funcionario.mostra_mensagem("Opção inválida.")

    def existe_funcionario(self):
        return bool(self.lista_funcionarios)
