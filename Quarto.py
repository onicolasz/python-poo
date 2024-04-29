class Quarto:
    def __init__(self, numero, categoria, diaria):
        self._numero = numero
        self._categoria = categoria
        self._diaria = diaria
        self._consumo = []
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
        
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria
        
    @property
    def diaria(self):
        return self._diaria
    
    @diaria.setter
    def diaria(self, diaria):
        self._diaria = diaria

    def adiciona_consumo(self, consumo):
        self._consumo.append(consumo)

    def lista_consumo(self):
        print('Consumos do Quarto: \n')
        for c in self._consumos:
            print(f'Nome: {c.nome} | Preco: {c.preco}')

    def valor_total_consumo(self):
        valor_total = 0
        for c in self._consumos:
            valor_total+=c.preco
        return valor_total
    
    def limpa_consumo(self):
        self._consumos = []
        
