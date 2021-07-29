# MÓDULO 1 - SELECIONAR E VALIDAR MÉTODOS DE PAGAMENTO
from _datetime import datetime

print('\n' + '---------- SEJA BEM VINDO AO POSTO DE COMBUSTÍVEL ----------')

# BLOCO 1 - VALIDAÇÃO DO MEIO DE PAGAMENTO -----------------------------------------------------------------------

while True:
    try:
        lista_entrada = ["sair", "Cartão", "QR Code", "dinheiro"]

        entrada = int(input('\n' + 'ESCOLHA UMA FORMA DE PAGAMENTO:\n'
                                   '1 - para ' + lista_entrada[1] + ' (MasterCard ou Visa)\n'
                                   '2 - para ' + lista_entrada[2] + '\n'
                                   '3 - para ' + lista_entrada[3] + '\n'
                                   '0 ** para ' + lista_entrada[0] + ' deste terminal\n'
                                       'DIGITE A OPÇÃO DESEJADA: '))

        if entrada == 1 or entrada == 2 or entrada == 3:
            print(('-' * 60) + '\n' + lista_entrada[entrada].upper() + ' SELECIONADO! Aguarde, processando...\n' + ('-' * 60))
            break

        elif entrada == 0:
            print(('-' * 60) + '\nSUA SESSÃO FOI ENCERRADA! AGRADECEMOS A COMPREENSÃO.\n' + ('-' * 60))
            break

        else:
            print(('-' * 60) + '\nOPÇÃO INVÁLIDA! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue

    except ValueError:
        print(('-' * 60) + '\nVALOR INVÁLIDO! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))

# BLOCO 2 - VALIDAÇÃO DA FORMA DE PAGAMENTO -----------------------------------------------------------------------

while True:
    try:
        lista_bandeira = ["sair", "MasterCard", "Visa"]

        bandeira = int(input('\n' + 'ESCOLHA A BANDEIRA DO CARTÃO:\n'
                                    '1 - para ' + lista_bandeira[1] + '\n'
                                    '2 - para ' + lista_bandeira[2] + '\n'
                                    '0 ** para ' + lista_bandeira[0] + ' deste terminal\n'
                                    'DIGITE A OPÇÃO DESEJADA: '))

        if entrada == 1:
            if bandeira == 1 or bandeira == 2:
                print(('-' * 60) + '\n' + lista_bandeira[bandeira].upper() + ' SELECIONADA!\n'
                                   'Aguarde, processando...\n'+ ('-' * 60))
                break

            elif bandeira == 0:
                print(('-' * 60) + '\nSUA SESSÃO FOI ENCERRADA! AGRADECEMOS A COMPREENSÃO.\n' + ('-' * 60))
                break

            else:
                print(('-' * 60) + '\nOPÇÃO INVÁLIDA! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                continue

    except ValueError:
        print(('-' * 60) + '\nVALOR INVÁLIDO! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))

# BLOCO 3 - QUANTIDADE E PREÇO DO COMBUSTIVEL -----------------------------------------------------------------------
while True:
    try:
        valorCombustivel = 4.50
        print('\n' + 'INFORME A QUANTIDADE DE GALOES DE COMBÚSTIVEL'
              '\nPREÇO ' + str(valorCombustivel) + ', HOJE ' + str(datetime.now()) + ', AS ' +'\n')

        qtdCombustivel = int(input('1 a 10 - para informar a quantidade de galões\n'
                                   '0 ** para sair deste terminal\n'
                                   'DIGITE A OPÇÃO DESEJADA: '))

        if 1 <= qtdCombustivel <= 10:
            print(('-' * 60) + '\nSELECIONADA A QTD. DE {} GALÕES!\n'
                               'Aguarde, processando...'.format(qtdCombustivel) + '\n' + ('-' * 60))
            break

        elif qtdCombustivel == 0:
            print(('-' * 60) + '\nSUA SESSÃO FOI ENCERRADA! AGRADECEMOS A COMPREENSÃO..\n' + ('-' * 60))
            break

        else:
            print(('-' * 60) + '\nQUANTIDADE INVÁLIDA! POR FAVOR DIGITE NOVAMENTE.\n' + ('-' * 60))
            continue

    except ValueError:
        print(('-' * 60) + '\nVALOR INVÁLIDO! POR FAVOR ESCOLHA NOVAMENTE.\n' + ('-' * 60))

