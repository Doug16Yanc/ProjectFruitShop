

class Mercadoria:
    def __init__(self, nome, codigo, quantidade, preco):
        self._nome = nome
        self._codigo = codigo
        self._quantidade = quantidade
        self._preco = preco

        @property
        def nome(self):
            return self._nome
        @nome.setter
        def nome(self, nome):
            self._nome = nome

        @property
        def codigo(self):
            return self._codigo

        @nome.setter
        def codigo(self, codigo):
            self._codigo = codigo

        @property
        def quantidade(self):
            return self._quantidade

        @quantidade.setter
        def quantidade(self, quantidade):
            self._quantidade = quantidade

        @property
        def preco(self):
            return self._preco

        @preco.setter
        def preco(self, preco):
            self._preco = preco










