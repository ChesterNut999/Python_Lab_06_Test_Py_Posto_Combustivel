# MÓDULO 2 - SELECIONAR E VALIDAR TIPO DE COMBUSTIVEL

import time, sys
import Py_01_FormaDePagamento_Quantidade

# BLOCO 1 - SELECÃO DE COMBUSTIVEL E VALIDAÇAO DE ESCOLHA -----------------------------------------------------------------------
py_01 = Py_01_FormaDePagamento_Quantidade
while py_01:
    try:
        lista_combustivel = ["sair", "Gasolina", "Alcool", "Diesel", "Gas",]

        combustivel = int(input('\n' + 'ESCOLHA UM TIPO DE COMBUSTIVEL:\n'
                                '1 - para ' + lista_combustivel[1] + '\n'
                                '2 - para ' + lista_combustivel[2] + '\n'
                                '3 - para ' + lista_combustivel[3] + '\n'
                                '4 - para ' + lista_combustivel[4] + '\n'
                                '0 ** para ' + lista_combustivel[0] + ' deste terminal\n'
                                'DIGITE A OPÇÃO DESEJADA: '))

        if combustivel == 1 or combustivel == 2 or combustivel == 3 or combustivel == 4:
            print(('-' * 60) + '\n' + lista_combustivel[combustivel].upper() + ' SELECIONADO!\n'
                   'Aguarde, processando...', end=' ')
            for i in range(0, 6):
                print(i, end=' ')
                sys.stdout.flush()
                time.sleep(1)

            print('\n' + ('-' * 60) + '\n')
            break

        elif combustivel == 0:
            print('\n---------- OBRIGADO POR UTILIZAR O POSTO DE COMBUSTÍVEL ----------\n')
            break

        else:
            print(('-' * 60) + '\nOPÇÃO INVÁLIDA! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue

    except ValueError:
        print(('-' * 60) + '\nVALOR INVÁLIDO! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))

    except BaseException:
        print(('-' * 60) + '\nERRO DESCONHECIDO! CONTACTE O ADMINISTRADOR DO SISTEMA.\n' + ('-' * 60))