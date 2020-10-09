class Calculador_de_imposto(object):
    
    def realiza_calculo(self, orcamento, imposto):
        print(imposto.calcula(orcamento))

if __name__ == '__main__':

    from orcamento import Orcamento
    from imposto import ICMS, ISS

    orcamento = Orcamento(500.0)
    calculador_de_imposto = Calculador_de_imposto()
    calculador_de_imposto.realiza_calculo(orcamento, ICMS())
    calculador_de_imposto.realiza_calculo(orcamento, ISS())