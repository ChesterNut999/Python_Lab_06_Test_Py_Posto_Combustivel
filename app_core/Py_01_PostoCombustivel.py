# MÓDULO 1 - PROGRAMA
import datetime, sys, time, os
import multiprocessing.process
from multiprocessing import Process

from typing import List
from app_utils.funcao_03_checkout import contador as func3_contador
from app_utils.funcao_03_checkout import entrada_usuario as func3_entrada


# VARS
entrada = None
bandeira = None
notas = None
qtdCombustivel = None
valorCombustivel = float(20)
tipoCombustivel = None
meioPagamento = None
decisao = None

# LISTAS
lista_entrada: List[str] = ["", "Cartão", "Dinheiro", "QR Code"]
lista_bandeira: List[str] = ["Voltar", "MasterCard", "Visa"]
lista_notas = ["Voltar", "Sim", 20, 50, 100]
lista_qtdCombustivel = ["Voltar", 1, 20]
lista_TipoCombustivel: List[str] = ["Voltar", "Gasolina", "Alcool", "Diesel", "GNV"]
data = datetime.date.today()
horario = datetime.datetime.now()
lista_checkout = ["Voltar", "Sim"]
lista_decisao = ['Sair', 'Voltar']

# MÓDULO 1 - MEIOS DE PAGAMENTO ----------------------------------------------------------
os.system('clear')

print('\nSEJA BEM VINDO AO POSTO DE COMBUSTÍVEL')

while True:
    print('\n---------- MENU PRINCIPAL ----------')

    try:
        entrada = int(input('\nESCOLHA UMA FORMA DE PAGAMENTO:\n'
                            '1 - para ' + lista_entrada[0] + ' (MasterCard ou Visa)\n'
                            '2 - para ' + lista_entrada[1] + '\n'
                            '3 - para ' + lista_entrada[2] + '\n'
                            'DIGITE A OPÇÃO DESEJADA: '))

    except BaseException:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
        continue

    # SE CARTÃO, ESCOLHE BANDEIRA
    if entrada == 1:
        print('\n' + ('-' * 60) + '\n' + lista_entrada[entrada].upper() + ' SELECIONADO!\n'
              'Aguarde, processando...\n' + ('-' * 60))

        while True:
            try:
                bandeira = int(input('\nESCOLHA A BANDEIRA DO CARTÃO:\n'
                                     '1 - para ' + lista_bandeira[1] + '\n'
                                     '2 - para ' + lista_bandeira[2] + '\n'
                                     '0 -- para ' + lista_bandeira[0] + ' ao menu inicial\n'
                                     'DIGITE A OPÇÃO DESEJADA: '))

                if bandeira == 1 or bandeira == 2:
                        print('\n' + ('-' * 60) + '\n' + lista_bandeira[bandeira].upper() + '. BANDEIRA SELECIONADA!\n'
                              'Aguarde, processando...\n' + ('-' * 60))
                        break

                elif bandeira == 0:
                        print('\n' + ('-' * 60) + '\n' + lista_bandeira[bandeira].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                              'Aguarde, processando...\n' + ('-' * 60))
                        break

                else:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                    continue

            except BaseException:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                    continue

        if bandeira == 0:
            continue

    # SE DINHEIRO, PROSSEGUE OU NÃO
    elif entrada == 2:
        print('\n' + ('-' * 60) + '\n' + lista_entrada[entrada].upper() + ' SELECIONADO!\n'
              'Aguarde, processando...\n' + ('-' * 60))

        while True:
                try:
                    notas = int(input('\n====> N Ã O  H Á  T R O C O <====\n'
                                      'INSIRA SOMENTE NOTAS DE: R$' + str(int(lista_notas[2])) + ', R$' + str(int(lista_notas[3])) + ', R$' + str(int(lista_notas[4])) + '\n' +
                                      '\nDESEJA PROSSEGUIR?\n'
                                      '1 - para ' + lista_notas[1] + '\n'
                                      '0 -- para ' + lista_notas[0] + ' ao menu inicial\n'
                                      'DIGITE A OPÇÃO DESEJADA: '))

                    if notas == 1:
                            print('\n' + ('-' * 60) + '\n' + lista_notas[notas].upper() + ' SELECIONADO!\n'
                                  'Aguarde, processando...\n' + ('-' * 60))
                            break

                    elif notas == 0:
                        print('\n' + ('-' * 60) + '\n' + lista_notas[notas].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                              'Aguarde, processando...\n' + ('-' * 60))
                        break

                    else:
                        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                        continue

                except BaseException:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                    continue

        if notas == 0:
            continue

    # SE QR Code, GERA E VALIDA (NÃO IMPLEMENTADO)
    elif entrada == 3:
            print('\n' + ('-' * 60) + '\n' + lista_entrada[entrada].upper() + ' SELECIONADO!\n'
                  'Aguarde, processando...\n' + ('-' * 60))
            break

    else:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
        continue

# MÓDULO 2 - QUANTIDADE E TIPO DE COMBUSTIVEL ----------------------------------------------------------
    while True:
        try:
            print('\nINFORME A QTD. DE GALOES DE COMBÚSTIVEL:\n'
                  '--> Consulta realizada em ' + str(data.strftime('%d-%m-%Y')) + ' ás ' + str(horario.strftime('%H:%M')) + '\n'
                  '--> Preço do galão (hoje): R$' + str(valorCombustivel) + '\n')

            qtdCombustivel = int(input(str(lista_qtdCombustivel[1]) + ' a ' + str(lista_qtdCombustivel[2]) + ' para informar a quantidade\n' +
                                           '0 -- para ' + str(lista_qtdCombustivel[0]) + ' ao menu inicial\n'
                                           'DIGITE A OPÇÃO DESEJADA: '))

        except BaseException:
            print('\n' + ('-' * 60) + '\nQUANTIDADE INVÁLIDA! DIGITE NOVAMENTE.\n' + ('-' * 60))
            continue

        if qtdCombustivel in range(1, 21):
            print('\n' + ('-' * 60) + '\nSELECIONADA A QTD. DE {} GALÕES!\n'
                  'Aguarde, processando...'.format(qtdCombustivel) + '\n' + ('-' * 60))

            while True:
                try:
                    tipoCombustivel = int(input('\nESCOLHA O TIPO DE COMBUSTIVEL:\n'
                                                '1 - para ' + lista_TipoCombustivel[1] + '\n'
                                                '2 - para ' + lista_TipoCombustivel[2] + '\n'
                                                '3 - para ' + lista_TipoCombustivel[3] + '\n'
                                                '4 - para ' + lista_TipoCombustivel[4] + '\n'
                                                '0 -- para ' + lista_TipoCombustivel[0] + ' ao menu inicial\n'
                                                'DIGITE A OPÇÃO DESEJADA: '))

                except BaseException:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! DIGITE NOVAMENTE.\n' + ('-' * 60))
                    continue

                if tipoCombustivel in range(1, 20):
                    print('\n' + ('-' * 60) + '\n' + lista_TipoCombustivel[tipoCombustivel].upper() + '. COMBÚSTIVEL SELECIONADO! BOMBEANDO.\n'
                          'Aguarde, processando...', end=' ')

                    for i in range(1, 6):
                        print(i, end=' ')
                        sys.stdout.flush()
                        time.sleep(1)

                    print('\n' + ('-' * 60) + '\n')

                    break

                elif tipoCombustivel == 0:
                    print('\n' + ('-' * 60) + '\n' + lista_TipoCombustivel[tipoCombustivel].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                          'Aguarde, processando...\n' + ('-' * 60))

                    break

                else:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                    continue

            if tipoCombustivel >= 0:
                break

        elif qtdCombustivel == 0:
            print('\n' + ('-' * 60) + '\n' + lista_qtdCombustivel[qtdCombustivel].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                  'Aguarde, processando...\n' + ('-' * 60))
            break

        else:
            print('\n' + ('-' * 60) + '\nQUANTIDADE INVÁLIDA! DIGITE NOVAMENTE.\n' + ('-' * 60))
            continue

    if qtdCombustivel == 0 or qtdCombustivel >= 1 and tipoCombustivel == 0:
        continue

# MÓDULO 3 - CHECKOUT E ABASTECIMENTO ----------------------------------------------------------
    if entrada and bandeira == 1 or entrada == 1 and bandeira == 2:
        meiopagamento = lista_entrada[entrada] + ' | ' + lista_bandeira[bandeira]

    else:
        meiopagamento = lista_entrada[entrada]

    print('====> C H E C K O U T <====\n'
          '\n---- Meio de pagamento: ' + meiopagamento.upper() +
          '\n---- Qtd. de galoes de combustivel: ' + str(qtdCombustivel) +
          '\n---- Tipo de combustivel: ' + str(lista_TipoCombustivel[tipoCombustivel].upper()) +
          '\n---- Valor Total da compra: R$ ' + str(float(qtdCombustivel * valorCombustivel)) + '\n')

    func3_contador()

    if func3_entrada == 1:
        print('\n' + ('-' * 60) + '\nABASTECIMENTO EM ANDAMENTO!\n'
              'Aguarde, processando...', end=' ')

        for i in range(1, 6):
            print(i, end=' ')
            sys.stdout.flush()
            time.sleep(1)

    elif func3_entrada == 0:
        print('\n' + ('-' * 60) + '\n' + lista_checkout[entrada].upper() + ' AO MENU INICIAL SELECIONADO!\n'
              'Aguarde, processando...\n' + ('-' * 60))
        continue

    elif func3_entrada == "":
        print('\n' + ('-' * 60) + '\nSESSÃO EXPIRADA AUTOMATICAMENTE!\n' + ('-' * 60) +
              '\nOBRIGADO POR UTILIZAR O POSTO DE COMBUSTIVEL! VOLTE SEMPRE!\n' + ('-' * 60))
        exit(0)

# MÓDULO 4 - FINALIZAÇÃO ----------------------------------------------------------
    print('\n' + ('-' * 60) + '\nABASTECIMENTO FINALIZADO!\n' + ('-' * 60) +
          '\nSEU RECIBO ESTÁ SENDO IMPRESSO.\n'
          'Aguarde, processando...', end=' ')

    for i in range(1, 6):
        print(i, end=' ')
        sys.stdout.flush()
        time.sleep(1)

    print('\n' + ('-' * 60) + '\nOBRIGADO POR UTILIZAR O POSTO DE COMBUSTIVEL! VOLTE SEMPRE!\n' + ('-' * 60))

    while True:
        try:
            decisao = (int(input('\nO QUE DESEJA FAZER AGORA?\n'
                                 '1 - para ' + lista_decisao[1] + ' ao menu inicial\n'
                                 '0 -- para ' + lista_decisao[0] + ' deste terminal\n'
                                 'DIGITE A OPÇÃO DESEJADA: ')))

        except BaseException:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue

        if 1 == decisao:
            print('\n' + ('-' * 60) + '\n' + lista_decisao[decisao].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                  'Aguarde, processando...\n' + ('-' * 60))
            break

        elif 0 == decisao:
            break

        else:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue

    if decisao == 1:
        continue

    else:
        exit(decisao)