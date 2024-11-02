class Sessao:
    def __init__(self, idSessao, horario, filme, sala, assentosDisponiveis, valorIngresso):
        self.__idSessao = idSessao
        self.__horario = horario
        self.__assentosDisponiveis = assentosDisponiveis
        self.__valorIngresso = valorIngresso
        self.__filme = filme
        self.__sala = sala
    
    @property
    def idSessao(self):
        return self.__idSessao
    
    @property
    def horario(self):
        return self.__horario
    
    @property
    def assentosDisponiveis(self):
        return self.__assentosDisponiveis
    
    @property
    def valorIngresso(self):
        return self.__valorIngresso
    
    @property
    def filme(self):
        return self.__filme

    @property
    def sala(self):
        return self.__sala
    
    def criarSessao(self):
        Sessao.sessoes.append(self)

    def editarSessao(self, novoHorario=None, novaSala=None, novosAssentos=None, novoValorIngresso=None):
        if novoHorario: self.horario = novoHorario
        if novaSala: self.sala = novaSala
        if novosAssentos: self.assentosDisponiveis = novosAssentos
        if novoValorIngresso: self.valorIngresso = novoValorIngresso

    def excluirSessao(self):
        Sessao.sessoes.remove(self)

    @classmethod
    def listarSessoes(cls):
        return cls.sessoes