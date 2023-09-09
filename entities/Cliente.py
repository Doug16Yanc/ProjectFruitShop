from entities.Fruta import Fruta
from entities.Legume import Legume
from entities.Verdura import Verdura


class Cliente:
    def __init__(self, nome):
        self._nome = nome

        @property
        def nome(self):
            return self._nome
        @nome.setter
        def nome(self, nome):
            self._nome = nome



        def EuCalculo(debito):
            debito += Fruta.somaFruta() + Legume.somaLegume() + Verdura.somaVerdura()
            return debito

