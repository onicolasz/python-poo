class Reserva:
    def __init__(self, dia_inicio, dia_fim, cliente, quarto, status):
        self._dia_inicio = dia_inicio
        self._dia_fim =  dia_fim
        self._cliente = cliente
        self._quarto = quarto
        self._status = status
        
    @property
    def dia_inicio(self):
        return self._dia_inicio
    
    @dia_inicio.setter
    def dia_inicio(self, dia_inicio):
        self._dia_inicio = dia_inicio
    
    @property
    def dia_fim(self):
        return self._dia_fim
    
    @dia_fim.setter
    def dia_fim(self, dia_fim):
        self._dia_fim = dia_fim
        
    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente
        
    @property
    def quarto(self):
        return self._quarto
    
    @quarto.setter
    def quarto(self, quarto):
        self._quarto = quarto
        
    @property
    def produto(self):
        return self._produto
    
    @produto.setter
    def produto(self, produto):
        self._produto = produto
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
    