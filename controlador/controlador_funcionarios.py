from entidade.funcionario import EntidadeFuncionario
from tela.tela_funcionario import TelaFuncionario

# Definição da exceção personalizada para funcionários repetidos
class FuncionarioRepetidoException(Exception):
    def __init__(self, id_funcionario):
        super().__init__(f"Funcionário com ID {id_funcionario} já existe.")

class ControladorFuncionarios:
    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema

    def pega_funcionario_por_id(self, id_funcionario: int):
        for funcionario in self.__funcionarios:
            if funcionario.id_funcionario == id_funcionario:
                return funcionario
        return None

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        id_funcionario = dados_funcionario["id_funcionario"]
        funcionario = self.pega_funcionario_por_id(id_funcionario)
        try:
            if funcionario is None:
                funcionario = EntidadeFuncionario(
                    dados_funcionario["cpf"],
                    dados_funcionario["id_funcionario"],
                    dados_funcionario["nome"],
                    dados_funcionario["cargo"],
                    dados_funcionario["salario"],
                    dados_funcionario["periodo"]
                )
                self.__funcionarios.append(funcionario)
                self.__tela_funcionario.mostra_mensagem("Funcionário incluído com sucesso.")
            else:
                raise FuncionarioRepetidoException(id_funcionario)
        except FuncionarioRepetidoException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))

    def alterar_funcionario(self):
        self.lista_funcionarios()
        id_funcionario = self.__tela_funcionario.seleciona_funcionario()
        try:
            id_funcionario = int(id_funcionario)
        except ValueError:
            self.__tela_funcionario.mostra_mensagem("ID inválido! Deve ser um número inteiro.")
            return

        funcionario = self.pega_funcionario_por_id(id_funcionario)

        if funcionario is not None:
            novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            funcionario.nome = novos_dados_funcionario["nome"]
            funcionario.cpf = novos_dados_funcionario["cpf"]
            funcionario.id_funcionario = novos_dados_funcionario["id_funcionario"]
            funcionario.cargo = novos_dados_funcionario["cargo"]
            funcionario.salario = novos_dados_funcionario["salario"]
            funcionario.periodo = novos_dados_funcionario["periodo"]

            self.lista_funcionarios()
            self.__tela_funcionario.mostra_mensagem("Funcionário atualizado com sucesso.")
        else:
            self.__tela_funcionario.mostra_mensagem("ATENÇÃO: Funcionário não existente")

    def lista_funcionarios(self):
        if not self.__funcionarios:
            self.__tela_funcionario.mostra_mensagem("Lista de funcionários está vazia.")
        else:
            for funcionario in self.__funcionarios:
                self.__tela_funcionario.mostra_funcionario({
                    "nome": funcionario.nome,
                    "cpf": funcionario.cpf,
                    "id_funcionario": funcionario.id_funcionario,
                    "cargo": funcionario.cargo,
                    "salario": funcionario.salario,
                    "periodo": funcionario.periodo
                })

    def excluir_funcionario(self):
        self.lista_funcionarios()
        id_funcionario = self.__tela_funcionario.seleciona_funcionario()
        try:
            id_funcionario = int(id_funcionario)
        except ValueError:
            self.__tela_funcionario.mostra_mensagem("ID inválido! Deve ser um número inteiro.")
            return

        funcionario = self.pega_funcionario_por_id(id_funcionario)

        if funcionario is not None:
            self.__funcionarios.remove(funcionario)
            self.lista_funcionarios()
            self.__tela_funcionario.mostra_mensagem("Funcionário excluído com sucesso.")
        else:
            self.__tela_funcionario.mostra_mensagem("ATENÇÃO: Funcionário não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_funcionario,
            2: self.alterar_funcionario,
            3: self.lista_funcionarios,
            4: self.excluir_funcionario,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__tela_funcionario.tela_opcoes()
            funcao = lista_opcoes.get(opcao, None)
            if funcao:
                funcao()
                if opcao == 0:
                    continua = False
            else:
                self.__tela_funcionario.mostra_mensagem("Opção inválida.")

