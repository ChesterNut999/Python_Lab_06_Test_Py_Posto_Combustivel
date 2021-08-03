# MÓDULO 2 - SELECIONAR E VALIDAR TIPO DE COMBUSTIVEL
import datetime
import time, sys, runpy
from datetime import datetime
from app_core import Py_01_FormaPagamento as py001
from app_core import Py_03_Checkout_Abastecimento

# BLOCO 1 - SELECÃO DE QTD. DE COMBUSTIVEL E VALIDAÇÃO
while True:
    try:
        valorCombustivel = 10.50
        print('\nINFORME A QTD. DE GALOES DE COMBÚSTIVEL:\n'
              '--> Data: ' + str(datetime.now()) + '\n'
              '--> Hora: ' + str(datetime.now()) + '\n'
              '--> Preço do galão (hoje): R$' + str(valorCombustivel) + '\n')

        qtdCombustivel = int(input('1 a 20 - para informar a quantidade de galões\n'
                                   '0 ** para voltar ao menu inicial\n'
                                   'DIGITE A OPÇÃO DESEJADA: '))

        if qtdCombustivel >= 1 and qtdCombustivel <= 20:
            print('\n' + ('-' * 60) + '\nSELECIONADA A QTD. DE {} GALÕES!\n'
                   'Aguarde, processando...'.format(qtdCombustivel) + '\n' + ('-' * 60))
            break

        elif qtdCombustivel >= 0 and qtdCombustivel < 1:
            print('\n' + ('-' * 60) + '\nVOLTAR AO MENU INICIAL SELECIONADO!\n'
            'Aguarde, processando...\n' + ('-' * 60))

            runpy._run_module_as_main(mod_name=py001)

        else:
            print('\n' + ('-' * 60) + '\nQUANTIDADE INVÁLIDA! DIGITE NOVAMENTE.\n' + ('-' * 60))
            continue

    except BaseException:
        print('\n' + ('-' * 60) + '\nQUANTIDADE INVÁLIDA! DIGITE NOVAMENTE.\n' + ('-' * 60))
        continue

# BLOCO 2 - SELECÃO DE TIPO DE COMBUSTIVEL E VALIDAÇAO
while True:
    try:
        lista_TipoCombustivel = ["sair", "gasolina", "alcool", "diesel", "GNV", ]

        tipoCombustivel = int(input('\n' + 'ESCOLHA O TIPO DE COMBUSTIVEL:\n'
                                '1 - para ' + lista_TipoCombustivel[1] + '\n'
                                '2 - para ' + lista_TipoCombustivel[2] + '\n'
                                '3 - para ' + lista_TipoCombustivel[3] + '\n'
                                '4 - para ' + lista_TipoCombustivel[4] + '\n'
                                '0 ** para ' + lista_TipoCombustivel[0] + ' deste terminal\n'
                                'DIGITE A OPÇÃO DESEJADA: '))

        if tipoCombustivel == 1 or tipoCombustivel == 2 or tipoCombustivel == 3 or tipoCombustivel == 4:
            print('\n' + ('-' * 60) + '\n' + lista_TipoCombustivel[tipoCombustivel].upper() + ' SELECIONADO! PREPARANDO BOMBEAMENTO.\n'
                   'Aguarde, processando...', end=' ')

            for i in range(0, 6):
                print(i, end=' ')
                sys.stdout.flush()
                time.sleep(1)

            print('\n' + ('-' * 60) + '\n')
            break

        elif tipoCombustivel == 0:
            print('\nOBRIGADO POR UTILIZAR O POSTO DE COMBUSTÍVEL\n')
            break

        else:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))

    except BaseException:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))

# BLOCO 3 - INICIA A EXECUÇÃO DO PRÓXIMO ESTADO DO PROGRAMA
if __name__ == '__main__'.startswith:
    runpy.run_module(mod_name=Py_03_Checkout_Abastecimento)
