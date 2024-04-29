class Produto:
    def __init__(self, codigo, nome, preco):
        self._codigo = codigo
        self._nome = nome
        self._preco = preco

    @property
    def codigo(self):
            return self._codigo
        
    @codigo.setter
    def codigo(self, codigo):
            self._codigo = codigo
            
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def preco(self):
        return self._preco
    
    @nome.setter
    def preco(self, preco):
        self._preco = preco
        
    