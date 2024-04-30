# Nícolas Barros de Souza e Guilherme Martins
from datetime import datetime
from Pousada import Pousada
from Quarto import Quarto
from Reserva import Reserva
from Produto import Produto

def main():
    # Carregar arquivo produtos
    produtos = Produto.deserializar()

    # Carregar arquivo quartos
    quartos = Quarto.deserializar()

    # Carregar arquivos das reservas
    reservas = Reserva.deserializar(quartos)

    # Criar pousada
    pousada = Pousada.deserializar(quartos, reservas, produtos)

    while(True) :
        print("\n")
        print("Menu da Pousada:")
        print("Digite 1 para Consultar disponibilidade ")
        print("Digite 2 para Consultar reserva ")
        print("Digite 3 para Realizar reserva ")
        print("Digite 4 para Cancelar reserva ")
        print("Digite 5 para Realizar Check-in ")
        print("Digite 6 para Realizar Checkout ")
        print("Digite 7 para Registrar consumo ")
        print("Digite 8 para Salvar os dados ")
        print("Digite 0 para Sair")
        print("\n")
        option = int(input('Digite sua escolha: '))
        print("\n")
        if option == 0:
            print('Finalizado.')
            break
        match option:
            # Consulta disponiblidade
            case 1:
                numero_quarto = int(input('Digite o quarto para consulta: '))
                data_inicio = input('Digite a data de inicio da consulta (no formato 2024-04-30): ')
                data_fim = input('Digite a data de fim da consulta (no formato 2024-04-30): ')
                disponibilidade = pousada.consulta_disponibilidade(datetime.strptime(data_inicio, "%Y-%m-%d"), datetime.strptime(data_fim, "%Y-%m-%d"), numero_quarto)
                if(disponibilidade == False):
                    print("\nQuarto NAO esta disponivel para reserva.")
                else:
                    print("\nQuarto esta disponivel para reserva.")
            # Pesquisa de reservas
            case 2:
                data_input = input('Digite a data de pesquisa (no formato 2024-04-30) (deixe em branco se nao quiser filtrar): ')
                cliente = input('Digite o nome de pesquisa (deixe em branco se nao quiser filtrar): ')
                quarto_input = input('Digite o quarto de pesquisa (deixe em branco se nao quiser filtrar): ')
                print('\n')
                
                # Verifica se o usuário forneceu uma data e a converte para o formato esperado
                if data_input.strip():
                    data = datetime.strptime(data_input, "%Y-%m-%d")
                else:
                    data = None
                    
                # Converte o número do quarto para inteiro, se fornecido
                quarto = int(quarto_input) if quarto_input.strip() else None
                
                # Chama a função consulta_reserva com os parâmetros fornecidos
                reservas_pesquisadas = pousada.consulta_reserva(data, cliente, quarto)
                
                # Verifica se foram encontradas reservas
                if len(reservas_pesquisadas) > 0:
                    for r in reservas_pesquisadas:
                        print('Reserva:')
                        print(r.toString())
                        print('\n')
                else:
                    print("Nao achou reservas com essa pesquisa")
            # Realizar reserva
            case 3:
                data_inicio = input('Digite a data de inicio da reserva (no formato 2024-04-30):  ')
                data_fim = input('Digite a data de fim da reserva (no formato 2024-04-30): ')
                cliente = input('Digite o nome do cliente para reserva: ')
                numero_quarto = int(input('Digite o quarto para reserva: '))
                reserva = pousada.realizar_reserva(datetime.strptime(data_inicio, "%Y-%m-%d"), datetime.strptime(data_fim, "%Y-%m-%d"), cliente, numero_quarto)
                print(f'\n{reserva}')
            # Cancelar reserva
            case 4:
                cliente = input('Digite o nome do cliente para reserva: ')
                cancelada = pousada.cancela_reserva(cliente)
                print(f'\n{cancelada}')
            # Realizar check-in
            case 5:
                cliente = input('Digite o nome do cliente para check-in: ')
                pousada.realiza_checkin(cliente)
            # Realizar checkout
            case 6:
                cliente = input('Digite o nome do cliente para checkout: ')
                pousada.realiza_checkout(cliente)
            # Registrar consumo
            case 7:
                cliente = input('Digite o nome do cliente para registrar consumo: ')
                pousada.registrar_consumo(cliente)
            # Salvar
            case 8:
                pousada.salva_dados()
            case _:
                print("Opcao {} invalida".format(option))
        

if __name__ == '__main__':
    main()