from DAOs.dao import DAO
from entidade.filme import Filme


class filmeDAO(DAO):
    def __init__(self):
        super().__init__('filme.pkl')

    def add(self, filme: Filme):
        if((filme is not None) and isinstance(filme, Filme) and isinstance(filme.id_filme, int)):
            super().add(filme.id_filme, filme)

    def update(self, filme: Filme):
        if((filme is not None) and isinstance(filme, Filme) and isinstance(filme.id_filme, int)):
            super().update(filme.id_filme, filme)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)