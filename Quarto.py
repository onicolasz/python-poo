# Nícolas Barros de Souza e Guilherme Martins
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

    @property
    def consumo(self):
        return self._consumo
    
    @consumo.setter
    def consumo(self, consumo):
        self._consumo = consumo

    def adiciona_consumo(self, consumo):
        self._consumo.append(consumo)

    def lista_consumo(self):
        print('Consumos do Quarto: \n')
        for c in self._consumos:
            print(f'Nome: {c.nome} | Preco: {c.preco}')

    #Não faz sentido calcular o valor total de consumo no Quarto, porque no consumo do quarto guardamos o id dos produtos
    def valor_total_consumo(self):
        #valor_total = 0
        #for c in self._consumo:
        #    valor_total+=c.preco
        #return valor_total
        return 0
    
    def limpa_consumo(self):
        self._consumos = []

    def procurar_quarto_por_codigo(quartos, numero):
        for quarto in quartos:
            if quarto.numero == numero:
                return quarto
        return None

    def serializar(self):
        return f"{self._numero};{self._categoria};{self._diaria}\n"

    def deserializar():
        quartos_criados = []
        with open('quarto.txt', 'r') as arquivo:
            arquivo.readline()
            for linha in arquivo:
                dados = linha.strip().split(';')
                numero = int(dados[0])
                categoria = dados[1]
                diaria = float(dados[2])
                quarto = Quarto(numero, categoria, diaria)
                quartos_criados.append(quarto)
        return quartos_criados