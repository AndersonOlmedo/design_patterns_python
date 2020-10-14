from abc import ABC, abstractmethod

class Imposto(ABC):
    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto
        
    def calcula_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)
        
    @abstractmethod
    def calcula(self, orcamento):
        pass
    
class ICMS(Imposto):
    
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calcula_outro_imposto(orcamento)

class ISS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calcula_outro_imposto(orcamento)