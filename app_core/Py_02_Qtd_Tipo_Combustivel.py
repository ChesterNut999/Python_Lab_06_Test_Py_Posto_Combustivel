# MÓDULO 2 - SELECIONAR E VALIDAR TIPO DE COMBUSTIVEL
import datetime, sys, time, runpy
from app_core import Py_01_FormaPagamento

# BLOCO 1 - SELECÃO DE QTD. E TIPO COMBUSTIVEL
qtdCombustivel = None
tipoCombustivel = None

while True:
    data = datetime.date.today()
    horario = datetime.datetime.now()
    valorCombustivel = float(10.50)

    try:
        lista_qtdCombustivel= ["Voltar", 1, 20]

        print('\nINFORME A QTD. DE GALOES DE COMBÚSTIVEL:\n'
              '--> Consulta realizada em ' + str(data.strftime('%d-%m-%Y')) + ' ás ' + str(horario.strftime('%H:%M')) + '\n'
              '--> Preço do galão (hoje): R$' + str(valorCombustivel) + '\n')

        qtdCombustivel = int(input(str(lista_qtdCombustivel[1]) + ' a ' + str(lista_qtdCombustivel[2]) + ' para informar a quantidade\n' +
                                       '0 -- para ' + str(lista_qtdCombustivel[0]) + ' ao menu inicial\n'
                                       'DIGITE A OPÇÃO DESEJADA: '))

        if qtdCombustivel >= 1 and qtdCombustivel <= 20:
            print('\n' + ('-' * 60) + '\nSELECIONADA A QTD. DE {} GALÕES!\n'
                  'Aguarde, processando...'.format(qtdCombustivel) + '\n' + ('-' * 60))

            while True:
                try:
                    lista_TipoCombustivel = ["Voltar", "Gasolina", "Alcool", "Diesel", "GNV", ]

                    tipoCombustivel = int(input('\n' + 'ESCOLHA O TIPO DE COMBUSTIVEL:\n'
                                                '1 - para ' + lista_TipoCombustivel[1] + '\n'
                                                    '2 - para ' + lista_TipoCombustivel[2] + '\n'
                                                    '3 - para ' + lista_TipoCombustivel[3] + '\n'
                                                '4 - para ' + lista_TipoCombustivel[4] + '\n'
                                                '0 -- para ' + lista_TipoCombustivel[0] + ' ao menu inicial\n'
                                                    'DIGITE A OPÇÃO DESEJADA: '))

                    if tipoCombustivel == 1 or tipoCombustivel == 2 or tipoCombustivel == 3 or tipoCombustivel == 4:
                        print('\n' + ('-' * 60) + '\n' + lista_TipoCombustivel[tipoCombustivel].upper() + '. COMBÚSTIVEL SELECIONADO! BOMBEANDO.\n'
                              'Aguarde, processando...', end=' ')

                        for i in range(0, 6):
                                print(i, end=' ')
                                sys.stdout.flush()
                                time.sleep(1)

                        print('\n' + ('-' * 60))

                        break

                    elif tipoCombustivel == 0:
                        qtdCombustivel = 0

                        print('\n' + ('-' * 60) + '\n' + lista_TipoCombustivel[tipoCombustivel].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                              'Aguarde, processando...\n' + ('-' * 60) + '\n')
                        break

                    else:
                        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                        continue

                except BaseException:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! DIGITE NOVAMENTE.\n' + ('-' * 60))
                    continue

            break

        if qtdCombustivel == 0:
            tipoCombustivel = 0

            print('\n' + ('-' * 60) + '\n' + str(lista_qtdCombustivel[qtdCombustivel].upper()) +' AO MENU INICIAL SELECIONADO!\n'
                  'Aguarde, processando...\n' + ('-' * 60))
            break

        else:
            print('\n' + ('-' * 60) + '\nQUANTIDADE INVÁLIDA! DIGITE NOVAMENTE.\n' + ('-' * 60))
            continue

    except BaseException:
        print('\n' + ('-' * 60) + '\nQUANTIDADE INVÁLIDA! DIGITE NOVAMENTE.\n' + ('-' * 60))

    if qtdCombustivel == 0 or qtdCombustivel == 0 and tipoCombustivel == 0:
        runpy.run_module(mod_name=Py_01_FormaPagamento)
    else:
        break