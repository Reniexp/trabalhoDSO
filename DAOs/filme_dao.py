from DAOs.dao import DAO
from entidade.filme import Filme


class FilmeDAO(DAO):
    def __init__(self,data_source: str):
        super().__init__(data_source)

    def add(self, filme: Filme):
        if (filme is not None) and isinstance(filme, Filme) : #and isinstance(filme.id_filme, int))
            super().add(filme)

    def update(self, filme: Filme):
        if((filme is not None) and isinstance(filme, Filme) and isinstance(filme.id_filme, int)):
            super().update(filme)

    def get(self, filme:Filme):
        if isinstance(filme, Filme):
            return super().get(filme)

    def remove(selfself, filme:Filme):
        if(isinstance(filme, Filme)):
            return super().remove(filme)