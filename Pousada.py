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
        
    def realizar_reserva(self, data_inicio, data_fim, cliente, numero_quarto):
        disponibilidade = self.consulta_disponibilidade(data_inicio, data_fim, numero_quarto)
        if(disponibilidade == False):
            return "Quarto nao esta disponivel para reserva."
        reserva = Reserva(data_inicio, data_fim, cliente, numero_quarto, "A")
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
    
    def realiza_checkin(self, cliente):
        reservas = self._reservas
        valor_total_diarias = 0   
        for r in reservas: 
            if r.cliente == cliente and r.status = 'A':
                r.status = "I"
                diferenca = r.dia_fim - r.dia_inicio
                valor_total_diarias = r.quarto.diaria * (diferenca.days +1)
                print ("\nCheckin realizado!")  
                print("Data da reserva: do dia", r.dia_inicio, "ao dia", r.dia_fim)              
                print("Valor total das diarias:", valor_total_diarias)
                print("Informacoes do quarto:")
                print("Numero do quarto: ",r.quarto.numero," Categoria do Quarto: ", r.quarto.categoria," Valor da diária: ", r.quarto.diaria)
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
                (reserva.quarto == quarto):
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
                if reserva.quarto == quarto:
                    reservas_achadas.append(reserva)
                
        return reservas_achadas

        