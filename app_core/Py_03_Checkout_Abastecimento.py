# MÓDULO 3 - CONFIRMAR DADOS E ABASTECER
import time, sys, runpy
from app_core import Py_01_FormaPagamento as py_01
from app_core import Py_02_Qtd_Tipo_Combustivel as py_02

# BLOCO 1 - PEGAR ENTRADA E ADICONAIS
checkout = None

if py_01.entrada == 1 and py_01.bandeira == 1 or py_01.entrada == 1 and py_01.bandeira == 2:
    meioPagamento = py_01.lista_entrada[py_01.entrada] + ' | ' + py_01.lista_bandeira[py_01.bandeira]
else:
    meioPagamento = py_01.lista_entrada[py_01.entrada]

# BlOCO 2 - IMPRIMINDO CHECKOUT
while True:
    print('\n====> C H E C K O U T <====\n'
          '---- Meio de pagamento: ' + meioPagamento.upper() + '\n'
          '---- Qtd. de galoes de combustivel: ' + str(py_02.qtdCombustivel) + '\n' 
          '---- Tipo de combustivel: ' + str(py_02.lista_TipoCombustivel[py_02.tipoCombustivel].upper()) + '\n'
          '---- Valor Total da compra: R$ ' + str(float(py_02.qtdCombustivel * py_02.valorCombustivel)))

    try:
        lista_checktou = ["Voltar", "Sim", "Não"]

        checkout = int(input('\n' + 'VOCE CONFIRMA O CHECKOUT?\n'
                                       '1 - para ' + lista_checktou[1] + '\n'
                                       '2 - para ' + lista_checktou[2] + '\n'
                                       '0 -- para ' + lista_checktou[0] + ' ao menu inicial\n'
                                       'DIGITE A OPÇÃO DESEJADA: '))

        if checkout == 1:
            print('\n' + ('-' * 60) + '\nABASTECIMENTO EM ANDAMENTO!\n'
                  'Aguarde, processando...', end=' ')

            for i in range(0, 6):
                print(i, end=' ')
                sys.stdout.flush()
                time.sleep(1)

            break

        elif checkout == 2:
            print('\n' + ('-' * 60) + '\nPARA VALORES INCORRETOS VOLTE AO MENU INICIAL E REPITA O PROCESSO.\n' + ('-' * 60))
            continue

        elif checkout == 0:
            print('\n' + ('-' * 60) + '\n' + lista_checktou[checkout].upper() + ' AO MENU INICIAL SELECIONADO!\n'
            'Aguarde, processando...\n' + ('-' * 60) + '\n')

            break

        else:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue

    except BaseException:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
        continue