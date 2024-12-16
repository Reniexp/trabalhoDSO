from DAOs.dao import DAO
from entidade.cliente import Cliente


class ClienteDAO(DAO):
    def __init__(self,data_source: str):
        super().__init__(data_source)

    def add(self, cliente: Cliente):
        if (cliente is not None) and isinstance(cliente, Cliente) : #and isinstance(cliente.cpf, int))
            super().add(cliente)

    def update(self, cliente: Cliente):
        if((cliente is not None) and isinstance(cliente, Cliente) and isinstance(cliente.cpf, int)):
            super().update(cliente)

    def get(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            return super().get(cliente)

    def remove(selfself, cliente:Cliente):
        if(isinstance(cliente, Cliente)):
            return super().remove(cliente)