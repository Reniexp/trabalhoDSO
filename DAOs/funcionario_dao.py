from DAOs.dao import DAO
from entidade.funcionario import EntidadeFuncionario


class funcionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionario.pkl')

    def add(self, funcionario: EntidadeFuncionario):
        if((funcionario is not None) and isinstance(funcionario, EntidadeFuncionario) and isinstance(funcionario.cpf, int)):
            super().add(funcionario.cpf, funcionario)

    def update(self, funcionario: EntidadeFuncionario):
        if((funcionario is not None) and isinstance(funcionario, EntidadeFuncionario) and isinstance(funcionario.cpf, int)):
            super().update(funcionario.cpf, funcionario)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)