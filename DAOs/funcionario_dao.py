from DAOs.dao import DAO
from entidade.funcionario import EntidadeFuncionario


class FuncionarioDAO(DAO):
    def __init__(self, data_source: str):
        super().__init__(data_source)

    def add(self, funcionario: EntidadeFuncionario):
        if (funcionario is not None) and isinstance(funcionario, EntidadeFuncionario): # and isinstance(funcionario.cpf, int))
            super().add(funcionario)

    def update(self, funcionario: EntidadeFuncionario):
        if((funcionario is not None) and isinstance(funcionario, EntidadeFuncionario) and isinstance(funcionario.cpf, int)):
            super().update(funcionario)

    def get(self, funcionario: EntidadeFuncionario):
        if isinstance(funcionario, EntidadeFuncionario):
            return super().get(funcionario)

    def remove(self, funcionario:EntidadeFuncionario):
        if(isinstance(funcionario, EntidadeFuncionario)):
            return super().remove(funcionario)
    def get_all(self):
        return super().get_all()