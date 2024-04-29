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
        reserva = Reserva(datetime.strptime(objReserva[0], "%Y-%m-%d"), datetime.strptime(objReserva[1], "%Y-%m-%d"), objReserva[2], quartos[0].numero, objReserva[3])
        reservas.append(reserva)
        linha3 = fileReserva.readline()

    # Criar pousada
    filePousada = open('pousada.txt', 'r')
    linha4 = filePousada.readline()
    objPousada = eval(linha4)
    pousada1 = Pousada(objPousada[0], objPousada[1], quartos, reservas, produtos)



    #data_inicio = datetime.strptime('2024-05-12', "%Y-%m-%d")
    #data_fim = datetime.strptime('2024-05-18', "%Y-%m-%d")
    #print(pousada1.consulta_disponibilidade(data_inicio, data_fim, 1))
    #print(pousada1.realizar_reserva(data_inicio, data_fim, "Joao", 1))
    #print(pousada1.consulta_disponibilidade(data_inicio, data_fim, 1))


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
            case 1:
                numero_quarto = int(input('Digite o quarto para consulta: '))
                data_inicio = input('Digite a data de inicio da consulta: ')
                data_fim = input('Digite a data de fim da consulta: ')
                pousada1.consulta_disponibilidade(data_inicio, data_fim, numero_quarto)
            case _:
                print("Opcao {} invalida".format(option))
        

if __name__ == '__main__':
    main()