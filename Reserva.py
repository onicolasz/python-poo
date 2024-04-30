# Nícolas Barros de Souza e Guilherme Martins
from datetime import datetime
from Quarto import Quarto

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

    def toString(self):
       return f'Data inicial: {self._dia_inicio} \nData final: {self._dia_fim} \nCliente: {self.cliente} \nNumero do Quarto: {self._quarto.numero}'
    
    def serializar(self):
        return f"{self._dia_inicio};{self._dia_fim};{self._cliente};{self._quarto.numero};{self._status}\n"

    def deserializar(lista_quartos):
        reservas_criadas = []
        with open('reserva.txt', 'r') as arquivo:
            arquivo.readline()
            for linha in arquivo:
                dados = linha.strip().split(';')
                dia_inicio = datetime.strptime(dados[0], "%Y-%m-%d")
                dia_fim = datetime.strptime(dados[1], "%Y-%m-%d")
                cliente = dados[2]
                quarto = Quarto.procurar_quarto_por_codigo(lista_quartos, int(dados[3]))
                status = dados[4]
                reserva = Reserva(dia_inicio, dia_fim, cliente, quarto, status)
                reservas_criadas.append(reserva)
        return reservas_criadas