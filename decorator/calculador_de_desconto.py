class Calculador_de_imposto(object):
    
    def calcula(self, orcamento, imposto):
        print(imposto.calcula(orcamento))

if __name__ == '__main__':

    from orcamento import Orcamento, Item
    from imposto import ICMS, ISS

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM_1', 50))
    orcamento.adiciona_item(Item('ITEM_2', 200))
    orcamento.adiciona_item(Item('ITEM_3', 250))

    calculador_de_imposto = Calculador_de_imposto()
    
    print('ICSM e ISS')
    calculador_de_imposto.calcula(orcamento, ICMS())
    calculador_de_imposto.calcula(orcamento, ISS())
    
    print('ICSM com ISS')
    calculador_de_imposto.calcula(orcamento, ICMS(ISS()))