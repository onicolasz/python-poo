from datetime import datetime
from Pousada import Pousada
from Quarto import Quarto
from Reserva import Reserva
from Produto import Produto

def main():
    # Carregar arquivo produtos
    fileProdutos = open('produto.txt', 'r')
    linha = fileProdutos.readline()
    produtos = []
    while linha != "":
        objProduto = eval(linha)
        produto = Produto(objProduto[0], objProduto[1], objProduto[2])
        produtos.append(produto)
        linha = fileProdutos.readline()

    # Carregar arquivo quartos
    fileQuartos = open('quarto.txt', 'r')
    linha2 = fileQuartos.readline()
    quartos = []
    while linha2 != "":
        objQuarto = eval(linha2)
        quarto = Quarto(objQuarto[0], objQuarto[1], objQuarto[2])
        quartos.append(quarto)
        linha2 = fileQuartos.readline()

    # Carregar arquivos das reservas
    fileReserva = open('reserva.txt', 'r')
    linha3 = fileReserva.readline()
    reservas = []
    while linha3 != "":
        objReserva = eval(linha3)
        reserva = Reserva(datetime.strptime(objReserva[0], "%Y-%m-%d"), datetime.strptime(objReserva[1], "%Y-%m-%d"), objReserva[2], objReserva[3], objReserva[4])
        reservas.append(reserva)
        linha3 = fileReserva.readline()

    # Criar pousada
    filePousada = open('pousada.txt', 'r')
    linha4 = filePousada.readline()
    objPousada = eval(linha4)
    pousada = Pousada(objPousada[0], objPousada[1], quartos, reservas, produtos)

    #data_inicio = datetime.strptime('2024-05-12', "%Y-%m-%d")
    #data_fim = datetime.strptime('2024-05-18', "%Y-%m-%d")
    #print(pousada.consulta_disponibilidade(data_inicio, data_fim, 1))
    #print(pousada.realizar_reserva(data_inicio, data_fim, "Joao", 1))
    #print(pousada.consulta_disponibilidade(data_inicio, data_fim, 1))


    while(True) :
        print("\n")
        print("Menu da Pousada:")
        print("Digite 1 para Consultar disponibilidade ")
        print("Digite 2 para Consultar reserva ")
        print("Digite 3 para Realizar reserva ")
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
                data_inicio = input('Digite a data de inicio da consulta: ')
                data_fim = input('Digite a data de fim da consulta: ')
                disponibilidade = pousada.consulta_disponibilidade(datetime.strptime(data_inicio, "%Y-%m-%d"), datetime.strptime(data_fim, "%Y-%m-%d"), numero_quarto)
                if(disponibilidade == False):
                    print("Quarto NAO esta disponivel para reserva.")
                print("Quarto esta disponivel para reserva.")
            # Pesquisa de reservas
            case 2:
                data_input = input('Digite a data de pesquisa (deixe em branco se nao quiser filtrar): ')
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
                        print(f'Reserva: \n Data inicial: {r.dia_inicio} \n Data final: {r.dia_fim} \n Cliente: {r.cliente} \n Numero do Quarto: {r.quarto}')
                else:
                    print("Nao achou reservas com essa pesquisa")
            # Realizar reserva
            case 3:
                data_inicio = input('Digite a data de inicio da reserva: ')
                data_fim = input('Digite a data de fim da reserva: ')
                cliente = input('Digite o nome do cliente para reserva: ')
                numero_quarto = int(input('Digite o quarto para reserva: '))
                reserva = pousada.realizar_reserva(datetime.strptime(data_inicio, "%Y-%m-%d"), datetime.strptime(data_fim, "%Y-%m-%d"), cliente, numero_quarto)
                print(reserva)
            case _:
                print("Opcao {} invalida".format(option))
        

if __name__ == '__main__':
    main()