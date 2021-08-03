# MÓDULO 3 - CONFIRMAR DADOS E ABASTECER
import time, sys, runpy
from app_core import Py_01_FormaPagamento as py0001
from app_core import Py_02_Qtd_Tipo_Combustivel as py0002
from app_core import Py_04_Finalizacao

# BLOCO 1 - CHECKOUT
while True:
    print('\nCHECKOUT: \n')
    print('---- Meio de pagamento: ' + str(py0001.lista_entrada[py0001.entrada].upper()))
    print('---- Qtd. de galoes de combustivel:') #+ str(py0002.qtdCombustivel))
    print('---- Tipo de combustivel: ') #+ str(py0002.lista_TipoCombustivel[py0002.tipoCombustivel].upper()))
    print('---- Valor Total da compra: R$') #+ str(py0002.qtdCombustivel * py0002.valorCombustivel))

    try:
        lista_checktou = ["voltar ao menu inicial", "sim", "não"]

        chekout = int(input('\n' + 'VOCE CONFIRMA O CHECKOUT?\n'
                                       '1 - para ' + lista_checktou[1] + '\n'
                                       '2 - para ' + lista_checktou[2] + '\n'
                                       '0 ** para ' + lista_checktou[0] + '\n'
                                       'DIGITE A OPÇÃO DESEJADA: '))

        if chekout == 1:
            print('\n' + ('-' * 60) + '\nABASTECIMENTO EM ANDAMENTO!\n'
                               'Aguarde, processando...', end=' ')
            for i in range(0, 6):
                print(i, end=' ')
                sys.stdout.flush()
                time.sleep(1)
            break

        elif chekout == 2:
            print('\n' + ('-' * 60) + '\nPARA VALORES INCORRETOS VOLTE AO MENU INICIAL E REPITA O PROCESSO.\n' + ('-' * 60))
            continue

        elif chekout == 0:
            print('\n' + ('-' * 60) + '\n' + lista_checktou[chekout].upper() + ' SELECIONADO\n'
            'Aguarde, processando...\n' + ('-' * 60))

        else:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))

    except BaseException:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
        continue

# # BLOCO 3 - INICIA A EXECUÇÃO DO PRÓXIMO ESTADO
if __name__ == '__main__'.startswith:
    runpy.run_module(mod_name=Py_04_Finalizacao)
