# MÓDULO 4 - FINALIZAÇÃO
import sys
import time

import Py_01_FormaDePagamento_Quantidade, Py_02_Selecionar_Tipo_Combustivel, Py_03_Abastecimento
py_01 = Py_01_FormaDePagamento_Quantidade
py_02 = Py_02_Selecionar_Tipo_Combustivel
py_03 = Py_03_Abastecimento

# BLOCO 1 - FINAL DE SESSÃO -----------------------------------------------------------------------
while py_01 and py_02 and py_03:
    try:
        lista_decisao=['sair', 'voltar ao menu inicial']

        print('\n' + 'ABASTECIMENTO FINALIZADO!\n'+ ('-' * 60))

        decisao = (int(input('\nO QUE DESEJA FAZER AGORA?\n'
                     '1 - para ' + lista_decisao[1] + '\n'
                     '0 ** para ' + lista_decisao[0] + ' deste terminal\n'
                     'DIGITE A OPÇÃO DESEJADA: ')))

        if decisao == 1:
            break

        if decisao == 0:
            print(('-' * 60) + '\nSEU RECIBO ESTÁ SENDO IMPRESSO.\n'
                  'Aguarde, processando...', end=' ')

            for i in range(0, 6):
                print(i, end=' ')
                sys.stdout.flush()
                time.sleep(1)

            print('\n' + ('-' * 60) +
                  '\n\n\n---------- OBRIGADO POR UTILIZAR O POSTO DE COMBUSTÍVEL ----------\n')
            break

        else:
            continue

    except ValueError:
        print(('-' * 60) + '\nVALOR INVÁLIDO! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))

    except BaseException:
        print(('-' * 60) + '\nERRO DESCONHECIDO! CONTACTE O ADMINISTRADOR DO SISTEMA.\n' + ('-' * 60))