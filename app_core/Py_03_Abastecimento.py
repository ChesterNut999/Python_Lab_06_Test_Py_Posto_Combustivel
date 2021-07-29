# MÓDULO 3 - CONFIRMAR DADOS E ABASTECER

import time, sys, signal
import Py_01_FormaDePagamento_Quantidade, Py_02_Selecionar_Tipo_Combustivel
from app_utils import funcao_03_contadores

py_01=Py_01_FormaDePagamento_Quantidade
py_02=Py_02_Selecionar_Tipo_Combustivel

# BLOCO 1 - TEMPO LIMITE DE SESSÃO -----------------------------------------------------------------------
contador = 0
# funcao_03_contadores.timer(contador)

# BLOCO 2 - CHECKOUT -----------------------------------------------------------------------
while contador < 30:

    print('\n' + 'CHECKOUT:\n'
          '---- Meio de pagamento:', py_01.lista_entrada[py_01.entrada], '\n'
          '---- Qtd. de galoes de combustivel:', py_01.qtdCombustivel, '\n'
          '---- Tipo de combustivel:', py_02.lista_combustivel[py_02.combustivel], '\n'
          '---- Valor Total da compra:', (py_01.qtdCombustivel * py_01.valorCombustivel))

    try:
        lista_confirmacao = ["sair", "Sim", "Não"]

        confirmacao = int(input('\n' + 'VOCE CONFIRMA O CHECKOUT?\n'
                                       '1 - para ' + lista_confirmacao[1] + '\n'
                                       '2 - para ' + lista_confirmacao[2] + '\n'
                                       '0 ** para ' + lista_confirmacao[0] + ' deste terminal e cancelar sua compra\n'
                                       'DIGITE A OPÇÃO DESEJADA: '))

        if confirmacao == 1:
            print(('-' * 60) + '\nABASTECIMENTO EM ANDAMENTO!\n'
                               'Aguarde, processando...', end=' ')
            for i in range(0, 6):
                print(i, end=' ')
                sys.stdout.flush()
                time.sleep(1)

            break

        elif confirmacao == 0:
            print(('-' * 60) + '\nSUA SESSÃO FOI ENCERRADA! AGRADECEMOS A COMPREENSÃO.\n' + ('-' * 60))
            break

        else:
            print(('-' * 60) + '\nVERIFIQUE O CHECKOUT. EM CASO DE ERRO REPITA O PROCESSO.\n' + ('-' * 60))
            continue

    except ValueError:
        print(('-' * 60) + '\nVALOR INVÁLIDO! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))

    except BaseException:
        print(('-' * 60) + '\nERRO DESCONHECIDO! CONTACTE O ADMINISTRADOR DO SISTEMA.\n' + ('-' * 60))
