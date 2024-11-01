from cliente import Cliente
from sessao import Sessao

class Ingresso:
    def __init__(self, idIngresso: int, assento: str, valor: float, cliente:Cliente, sessao : Sessao):
        self.__idIngresso = idIngresso
        self.__assento = assento
        self.__valor = valor
        self.__cliente = cliente
        self.__sessao = sessao
       
    @property
    def idIngresso(self):
        return self.__idIngresso
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def assento(self):
        return self.__assento
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def sessao(self):
        return self.__sessao 
     
    def venderIngresso(self):
        Ingresso.ingressos.append(self)
        self.cliente.comprarIngresso(self.sessao)

    @classmethod
    def listarIngressos(cls):
        return cls.ingressos

    def cancelarIngresso(self):
        i = 0
        while i < len(Ingresso.ingressos):
            if Ingresso.ingressos[i].idIngresso == self.__idIngresso:
                Ingresso.ingressos.pop(i)
            i+=1
        #Ingresso.ingressos.remove(self)
            
cliente1 = Cliente(1,"Maria Oliveira")
sessao1 = Sessao("09", "09", "123", "23", 1, "18:00")
ingresso1 = Ingresso(idIngresso=1, assento="A10", valor=20.0, cliente=cliente1, sessao=sessao1)

#vendendo o ingresso
ingresso1.venderIngresso()

#verificando ingressos antes do cancelamento
ingressos_listados_before = Ingresso.listarIngressos()

# cancelando o ingresso
ingresso1.cancelarIngresso()

# verificando ingressos após o cancelamento
ingressos_listados_after = Ingresso.listarIngressos()

ingressos_listados_before, ingressos_listados_after