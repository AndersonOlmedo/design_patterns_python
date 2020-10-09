class Calculador_de_imposto(object):
    
    def realiza_calculo(self, orcamento, imposto):
        return imposto.calcula(orcamento)

if __name__ == '__main__':

    from orcamento import Orcamento
    from imposto import ICMS, ISS

    orcamento = Orcamento(500.0)
    calculador_de_imposto = Calculador_de_imposto()
    imposto_ICMS = calculador_de_imposto.realiza_calculo(orcamento, ICMS())
    imposto_ISS = calculador_de_imposto.realiza_calculo(orcamento, ISS())

    print(f'imposto ICMS: {imposto_ICMS}')
    print(f'imposto ISS: {imposto_ISS}')