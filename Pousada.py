# Nícolas Barros de Souza e Guilherme Martins
import csv
from datetime import datetime
from Quarto import Quarto
from Reserva import Reserva

class Pousada:
    def __init__(self, nome, contato, quartos, reservas, produtos):
        self._nome = nome
        self._contato = contato
        self._quartos = quartos
        self._reservas = reservas
        self._produtos = produtos
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
     
    @property   
    def contato(self):
        return self._contato
    
    @contato.setter
    def contato(self, contato):
        self.contato = contato

    @property   
    def produtos(self):
        return self._produtos
    
    @produtos.setter
    def produtos(self, produtos):
        self.produtos = produtos
        
    def realizar_reserva(self, data_inicio, data_fim, cliente, numero_quarto):
        quartoAchado = False
        for quarto in self._quartos:
            if quarto.numero == numero_quarto:
                quartoAchado = quarto
        if(quartoAchado == False):
            return "Quarto não existe"
        disponibilidade = self.consulta_disponibilidade(data_inicio, data_fim, numero_quarto)
        if(disponibilidade == False):
            return "Quarto nao esta disponivel para reserva."
        reserva = Reserva(data_inicio, data_fim, cliente, quartoAchado, "A")
        self._reservas.append(reserva)
        return "Reserva realizada com sucesso."

    def consulta_disponibilidade(self, data_inicio, data_fim, numero_quarto):
        reservas = self._reservas
        for r in reservas: 
            if r.quarto.numero == numero_quarto:
                # Se a nova reserva começa depois que a reserva atual termina
                # ou se a nova reserva termina antes que a reserva atual comece,
                # então não há conflito
                if (r._dia_fim < data_inicio) or (r._dia_inicio > data_fim):
                    continue
                else:
                    # Se a data está dentro do período de uma reserva existente,
                    # não está disponível
                    return False
        # Se não encontrou o quarto ou não há conflitos de datas com as reservas existentes,
        # então o quarto está disponível
        return True

    def cancela_reserva(self, cliente):
        reservas = self._reservas
        for r in reservas:
            if r.cliente == cliente and r.status == 'A':
                r.status = "C"
                return "Reserva Cancelada"
        return "Reserva não existente"
    
    def cancela_reserva(self, cliente):
        reservas_canceladas = 0
        reservas = self._reservas
        for r in reservas:
            # Verifica se existe alguma reserva para o nome do cliente informado, se sim, altera o status da reserva de "A" para "C"
            if r.cliente == cliente and r.status == 'A':
                r.status = 'C'
                reservas_canceladas += 1
        
        if reservas_canceladas > 0:
            return f"{reservas_canceladas} reserva(s) cancelada(s) com sucesso."
        else:
            return "Nenhuma reserva encontrada para o cliente fornecido ou já cancelada."
    
    def realiza_checkin(self, cliente):
        reservas = self._reservas
        valor_total_diarias = 0   
        for r in reservas: 
            if r.cliente == cliente and r.status == 'A':
                r.status = "I"
                diferenca = r.dia_fim - r.dia_inicio
                valor_total_diarias = r.quarto.diaria * (diferenca.days +1)
                print ("\nCheckin realizado!")  
                print("Data da reserva: do dia", r.dia_inicio, "ao dia", r.dia_fim)              
                print("Valor total das diarias:", valor_total_diarias)
                print("Informacoes do quarto:")
                print("Numero do quarto: ",r.quarto.numero," Categoria do Quarto: ", r.quarto.categoria," Valor da diaria: ", r.quarto.diaria)
                return True
        print( "Nenhuma reserva encontrada")
        return False

    def realiza_checkout(self, cliente):
        reservas = self._reservas
        valor_total_diarias = 0   
        for r in reservas: 
            if r.cliente == cliente and r.status == 'I':
                r.status = 'O'
                diferenca = r.dia_fim - r.dia_inicio
                valor_total_diarias = r.quarto.diaria * (diferenca.days +1)
                print ("\nCheckout realizado! Informacoes abaixo.")  
                print("Data da reserva: do dia", r.dia_inicio, "ao dia", r.dia_fim)   
                print("Toal de dias: ",diferenca.days+1)           
                print("Valor total das diarias:", valor_total_diarias)
                print("Consumo:")
                total_consumo = 0
                if len(r.quarto.consumo) > 0:
                    for consumo in r.quarto.consumo:
                        for p in self._produtos:
                            if p.codigo == consumo:
                                print('Produto ',p.nome,'- R$',p.preco)
                                total_consumo+=p.preco
                
                print('Valor total dos consumos: R$', total_consumo)      
                print('Valor total das diarias (c/ consumo): R$', valor_total_diarias+total_consumo)        
                r.quarto.limpa_consumo()
                return True
        print( "Nenhuma reserva encontrada")
        return False

    def consulta_reserva(self, data, cliente, quarto):
        reservas = self._reservas
        reservas_achadas = [] 
        
        for reserva in reservas:
            # Verifica se todos os parâmetros foram fornecidos
            if data and cliente and quarto:
                if (reserva.dia_inicio <= data <= reserva.dia_fim) and \
                (reserva.cliente == cliente) and \
                (reserva.quarto.numero == quarto):
                    reservas_achadas.append(reserva)
            # Verifica se apenas data e cliente foram fornecidos
            elif data and cliente:
                if (reserva.dia_inicio <= data <= reserva.dia_fim) and \
                (reserva.cliente == cliente):
                    reservas_achadas.append(reserva)
            # Verifica se apenas data foi fornecido
            elif data:
                if reserva.dia_inicio <= data <= reserva.dia_fim:
                    reservas_achadas.append(reserva)
            # Verifica se apenas cliente foi fornecido
            elif cliente:
                if reserva.cliente == cliente:
                    reservas_achadas.append(reserva)
            # Verifica se apenas quarto foi fornecido
            elif quarto:
                if reserva.quarto.numero == quarto:
                    reservas_achadas.append(reserva)
                
        return reservas_achadas

    def registrar_consumo(self, cliente):
        reservas_consultadas = self.consulta_reserva(None, cliente, None)
        achou_reserva = False
        if len(reservas_consultadas) > 0:
            for reserva in reservas_consultadas:
                if reserva.status == 'I':
                    achou_reserva = True
                    print('Produtos disponiveis: \n')
                    for p in self._produtos:
                        print(p.toString())
                    produto = int(input('Digite o codigo do produto desejado: '))
                    reserva.quarto.adiciona_consumo(produto)
                    print('Produto adicionado no consumo.')
                
        if achou_reserva == False:
            print('Não achou reservas com checkin ativo para o cliente')

    def salva_dados(self):
        dados_salvos = open("dados_salvos.csv", "w")
        writer = csv.writer(dados_salvos)
        writer.writerow(['dia_inicio', 'dia_fim', 'cliente', 'numero_quarto', 'categoria_quarto', 'diaria_quarto', 'status'])
        for r in self._reservas:
            if r.status == 'A' or r.status == 'I':
                writer.writerow([r.dia_inicio, r.dia_fim, r.cliente, r.quarto.numero, r.quarto.categoria, r.quarto.diaria, r.status])
        dados_salvos.close()
        print('Dados salvos com sucesso')

    def serializar(self):
        return f"{self._nome};{self._contato}\n"

    def deserializar(quartos, reservas, produtos):
        with open('pousada.txt', 'r') as arquivo:
            arquivo.readline()
            for linha in arquivo:
                dados = linha.strip().split(';')
                nome = dados[0]
                contato = dados[1]
                pousada = Pousada(nome, contato, quartos, reservas, produtos)
                return pousada      