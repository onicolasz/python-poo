# Nícolas Barros de Souza e Guilherme Martins
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
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco

    def toString(self):
        return f'Codigo: {self._codigo}, Nome: {self._nome}, Valor: R${self._preco}'

    def serializar(self):
        return f"{self._codigo};{self._nome};{self._categoria}\n"

    def deserializar():
        produtos_criados = []
        with open('produto.txt', 'r') as arquivo:
            arquivo.readline()
            for linha in arquivo:
                dados = linha.strip().split(';')
                codigo = int(dados[0])
                nome = dados[1]
                preco = float(dados[2])
                produto = Produto(codigo, nome, preco)
                produtos_criados.append(produto)
        return produtos_criados