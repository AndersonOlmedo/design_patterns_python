from desconto import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_desconto(object):
    
    def calcula(self, orcamento):
        return Desconto_por_cinco_itens( Desconto_por_mais_de_quinhentos_reais( Sem_desconto() ) ).calcula(orcamento)

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM_1', 100.0))
    orcamento.adiciona_item(Item('ITEM_2', 50.0))
    orcamento.adiciona_item(Item('ITEM_3', 400.0))
    orcamento.adiciona_item(Item('ITEM_4', 100.0))
    orcamento.adiciona_item(Item('ITEM_5', 100.0))
    orcamento.adiciona_item(Item('ITEM_6', 100.0))
    
    calculador_de_desconto = Calculador_de_desconto()
    desconto = calculador_de_desconto.calcula(orcamento)
    print(f'O desconto eh de: {desconto}')