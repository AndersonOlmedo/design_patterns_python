from abc import ABC, abstractmethod

class Estado_de_um_orcamento(ABC):
    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass
    
    @abstractmethod
    def aprova(self, orcamento):
        pass
    
    @abstractmethod
    def reprova(self, orcamento):
        pass
    
    @abstractmethod
    def finaliza(self, orcamento):
        pass

class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
    
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()
    
    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()
    
    def finaliza(self, orcamento):
        raise Exception('Orcamentos em aprovacao nao podem ser finalizados')
    
class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
    
    def aprova(self, orcamento):
        raise Exception('Orcamento aprovados nao podem ser aprovados novamente')
    
    def reprova(self, orcamento):
        raise Exception('Orcamento aprovados nao podem ser reprovados')
    
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()
    
class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')
    
    def aprova(self, orcamento):
        raise Exception('Orçamentos reprovados não podem ser aprovados')
    
    def reprova(self, orcamento):
        raise Exception('Orçamentos reprovados não podem ser reprovados novamente')
    
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()
    
class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não recebem desconto extra')
    
    def aprova(self, orcamento):
        raise Exception('Orcamentos finalizados nao podem ser aprovados')
    
    def reprova(self, orcamento):
        raise Exception('Orcamentos finalizados nao podem ser reprovados')
    
    def finaliza(self, orcamento):
        raise Exception('Orcamentos finalizados nao podem ser finalizados novamente')

class Orcamento(object):

    def __init__(self):
        self.__items = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0.0
        
    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)
        
    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto
        
    def aprova(self):
        self.estado_atual.aprova(self)
        
    def reprova(self):
        self.estado_atual.reprova(self)
        
    def finaliza(self):
        self.estado_atual.finaliza(self)

    @property
    def valor(self):
        valor = 0.0
        for item in self.__items:
            valor += item.valor
        return valor - self.__desconto_extra

    @property
    def total_items(self):
        return len(self.__items)

    def adiciona_item(self, item):
        self.__items.append(item)

class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM_1', 50))
    orcamento.adiciona_item(Item('ITEM_2', 200))
    orcamento.adiciona_item(Item('ITEM_3', 250))
    
    print(orcamento.valor)
    orcamento.aprova()
    orcamento.aplica_desconto_extra()    
    print(orcamento.valor)