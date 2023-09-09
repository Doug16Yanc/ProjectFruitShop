from entities.Mercadoria import Mercadoria


class Legume(Mercadoria):
    def __init__(self, nome, codigo, quantidade, preco):
        super().__init__(nome, codigo, quantidade, preco)

        def EuCalculo(self):
            return self._preco * self._quantidade

        def somaLegume(EuCalculo):
            EuCalculo += 1


